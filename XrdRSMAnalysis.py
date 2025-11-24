import pickle
from ui.main import Ui_mainui

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QLineEdit
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm
import math
import os
import sympy as sym
from matplotlib.backend_bases import MouseButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from copy import deepcopy
import pickle


def load_select_dict():
    try:
        with open('.systems/select_dict.pkl', 'rb') as file:
            sel_dict = pickle.load(file)
    except Exception as e:
        sel_dict = {
            "GexSi1-x / Si (001)": ("5.431", '1.540598', '5.431', '5.431 + 0.1992*x + 0.02733 * x**2',
                                    '165.8 - 37.3 * x', '63.9 - 15.6 * x', '-2', '-2', '4', '0', '0', '1'),
            "GexSi1-x / Si (111)": ("5.431", '1.540598', '5.431', '5.431 + 0.1992*x + 0.02733 * x**2',
                                    '165.8 - 37.3 * x', '63.9 - 15.6 * x', '2', '2', '4', '1', '1', '1'),
            "Ge1-xSix / Ge (001)": ("5.431", '1.540598', '5.6575', '5.65753 - 0.25386*x + 0.02733 * x**2',
                                    '128.5 + 37.3 * x', '48.3 + 15.6 * x', '-2', '-2', '4', '0', '0', '1'),
            "Ge1-xSix / Ge (111)": ("5.431", '1.540598', '5.6575', '5.65753 - 0.25386*x + 0.02733 * x**2',
                                    '128.5 + 37.3 * x', '48.3 + 15.6 * x', '2', '2', '4', '1', '1', '1'),
            "InxGa1-xAs / Si (001)": ("5.431", '1.540598', "5.431", '0.405 * x + 5.6533',
                                      '11.9 - 3.56 * x', '5.34 - 0.8 * x', '-2', '-2', '4', '0', '0', '1'),
        }
    return sel_dict


def save_select_dict(sel_dict):
    with open('.systems/select_dict.pkl', 'wb') as file:
        pickle.dump(sel_dict, file)


def log_with_zero(var):
    if var > 0:
        return math.log10(var)
    elif var < 0:
        raise ValueError("log 值不能小于零")
    else:
        return var


class XrdRSM(FigureCanvas, Ui_mainui):

    def __init__(self):
        super(XrdRSM, self).__init__()
        self.setupUi(self)
        self.flag_cb_plot_checked = False

        # 加载Main.ui文件
        qui_file = QFile('ui/main.ui')
        qui_file.open(QFile.ReadOnly)
        qui_file.close()
        # self = QUiLoader().load(qui_file)
        self.select_dict: dict = load_select_dict()
        self.default_key_ls = ["GexSi1-x / Si (001)", "GexSi1-x / Si (111)", "Ge1-xSix / Ge (001)",
                               "Ge1-xSix / Ge (111)", "InxGa1-xAs / Si (001)"]
        self.select_comboBox.addItems(self.select_dict.keys())
        # self.select_comboBox.addItem("GexSi1-x / Si (001)")
        # self.select_comboBox.addItem("GexSi1-x / Si (111)")
        # self.select_comboBox.addItem("Ge1-xSix / Ge (001)")
        # self.select_comboBox.addItem("Ge1-xSix / Ge (111)")
        # self.select_comboBox.addItem("InxGa1-xAs / Si (001)")
        self.select_comboBox.setCurrentIndex(0)
        self.select_comboBox.currentTextChanged.connect(self.combox_changed)
        # self.select_comboBox.currentIndexChanged.connect(self.combox_changed)

        # 初始化私有变量
        self.import_path = r'F:\datas'
        self.qx = np.mat([[]])
        self.qz = np.mat([[]])
        self.omega = np.mat([[]])
        self.theta = np.mat([[]])
        self.intensity = np.mat([[]])
        self.xmin = -1
        self.xmax = 1
        self.ymin = -1
        self.ymax = 1
        self.scan_type = -1
        self.filename = ''
        self.R_si = None  # 用于计算弛豫， 相对于Si
        # # 计算相关
        self.para_changed()

        # 画图相关变量
        self.color_array = ['g', 'r', 'c', 'm', 'k']
        self.color_index = 0
        self.x_sel = 0
        self.y_sel = 0
        self.z_min = 0
        self.sb_zmin.setSingleStep(1)
        self.z_max = 1000
        self.sel_cross1 = None
        self.sel_cross2 = None
        self.zoomed = False
        self.relaxation_line = None
        plt.ion()
        self.fig = plt.figure(1, [8, 8])
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.font_tick_label = {'family': 'Times New Roman', 'weight': 'normal', 'size': 18}
        self.font_axis_label = {'family': 'Times New Roman', 'weight': 'normal', 'size': 24}
        self.font_title = {'family': 'Times New Roman', 'weight': 'bold', 'size': 24, 'color': 'red'}
        self.font_text = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
        # 创建fig控件鼠标响应
        self.fig.canvas.mpl_connect('button_press_event', self.zoom_in)
        # 连接QT控件和Slot
        self.import_button.clicked.connect(self.import_datas)
        self.export_button.clicked.connect(self.export_text)
        self.savePic_button.clicked.connect(self.save_picture)
        self.calib_button.clicked.connect(self.calib_sub_peak)
        self.addPeak_button.clicked.connect(self.cal_peak)
        self.x_slide.valueChanged.connect(self.draw_relaxation_line)
        self.xmin_SpinBox.valueChanged.connect(self.xmin_changed)
        self.ymin_SpinBox.valueChanged.connect(self.ymin_changed)
        self.xmax_SpinBox.valueChanged.connect(self.xmax_changed)
        self.ymax_SpinBox.valueChanged.connect(self.ymax_changed)
        self.sb_zmin.editingFinished.connect(self.zmin_changed)
        self.sb_zmax.editingFinished.connect(self.zmax_changed)

        self.le_kalp1.editingFinished.connect(self.para_changed)
        self.le_as0.editingFinished.connect(self.para_changed)
        self.le_af0.editingFinished.connect(self.para_changed)
        self.le_c11.editingFinished.connect(self.para_changed)
        self.le_c12.editingFinished.connect(self.para_changed)
        self.le_d_h.editingFinished.connect(self.para_changed)
        self.le_d_k.editingFinished.connect(self.para_changed)
        self.le_d_l.editingFinished.connect(self.para_changed)
        self.le_s_h.editingFinished.connect(self.para_changed)
        self.le_s_k.editingFinished.connect(self.para_changed)
        self.le_s_l.editingFinished.connect(self.para_changed)
        self.pb_new.clicked.connect(self.new_combox_item)
        self.pb_save.clicked.connect(self.save_combox_item)
        self.pb_delete.clicked.connect(self.delete_combox_item)
        self.pb_reload.clicked.connect(self.return_defalut)
        self.cb_plot_log.stateChanged.connect(self.plot_log_changed)

        self.combox_changed("GexSi1-x / Si (001)")

    def para_changed(self):
        # 计算相关
        self.as0 = float(self.le_as0.text())
        self.kapl1 = float(self.le_kalp1.text())
        self.hkl_f = np.array([float(self.le_d_k.text()), float(self.le_d_k.text()), float(self.le_d_l.text())])
        self.hkl_0 = np.array([float(self.le_s_h.text()), float(self.le_s_k.text()), float(self.le_s_l.text())])
        self.cos_phi = np.dot(self.hkl_f, self.hkl_0) / np.sqrt(self.hkl_f.dot(self.hkl_f) * self.hkl_0.dot(self.hkl_0))
        self.sin_phi = np.sqrt(1 - self.cos_phi ** 2)
        self.d_hkl = self.as0 / np.sqrt(self.hkl_f.dot(self.hkl_f))
        self.qx_s0 = -1 * self.sin_phi / self.d_hkl
        self.qz_s0 = self.cos_phi / self.d_hkl
        self.phi0 = math.acos(self.cos_phi) / math.pi * 180
        self.theta0 = math.asin(self.kapl1 / 2 / self.d_hkl) / math.pi * 360
        self.omega0 = self.phi0 + self.theta0 / 2

        # print(self.theta0, self.omega0)
        self.haven_calib_sub = False

        x = sym.Symbol("x")
        self.af0 = eval(self.le_af0.text())
        af0_N = self.af0.evalf(subs={x: 1})
        self.qx_f0 = -1 * self.sin_phi / af0_N * np.sqrt(self.hkl_f.dot(self.hkl_f))
        self.qz_f0 = self.cos_phi / af0_N * np.sqrt(self.hkl_f.dot(self.hkl_f))
        c11 = eval(self.le_c11.text())
        c12 = eval(self.le_c12.text())
        self.ratioC = 2 * c12 / c11
        self.logging.setPlainText('qx_sub = %.5f, qz_sub = %.5f' % (self.qx_s0, self.qz_s0))
        self.logging.appendPlainText('del_qx = %.4f, del_qz = %.4f' % (0, 0))
        if self.omega.size != 0:
            self.cal_qx_qz()

    def import_datas(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开源文件', self.import_path, '*.xrdml')
        if len(fname) == 0:
            print('select no files')
            return
        self.import_path = fname

        self.filename = os.path.splitext(fname)[0]
        print(self.filename)
        dom = xml.dom.minidom.parse(fname)
        root = dom.documentElement
        data = root.getElementsByTagName('positions')
        intensity = root.getElementsByTagName('counts')

        xrd_meas = root.getElementsByTagName('xrdMeasurement')[0]
        meas_type = xrd_meas.getAttribute('measurementType')
        # print(meas_type)
        if meas_type == "Scan":
            self.import_scan_data(data, intensity)
            self.scan_type = 0
            self.cb_plot_log.setText('plot_log')
            # self.cb_plot_log.setEnabled(True)
        elif meas_type == "Area measurement":
            self.import_area_data(data, intensity)
            self.scan_type = 1
            self.cb_plot_log.setText('2θ-ω')
            # self.cb_plot_log.setEnabled(False)

    def import_scan_data(self, data, intensity):
        theta_str = 1
        theta_end = 2

        ome_str = 1
        ome_end = 2

        for i in data:
            # print(i.getAttribute('axis'))
            if i.getAttribute('axis') == "2Theta":
                try:
                    theta = i.getElementsByTagName("startPosition")
                    theta_str = theta[0].firstChild.data
                    theta_str = float(theta_str)
                    theta = i.getElementsByTagName("endPosition")
                    theta_end = theta[0].firstChild.data
                    theta_end = float(theta_end)
                except IndexError:
                    theta = i.getElementsByTagName("commonPosition")
                    theta = theta[0].firstChild.data
                    theta_str = float(theta)
                    theta_end = float(theta)

            if i.getAttribute('axis') == "Omega":
                try:
                    ome = i.getElementsByTagName("startPosition")
                    ome_str = ome[0].firstChild.data
                    ome_str = float(ome_str)
                    ome = i.getElementsByTagName("endPosition")
                    ome_end = ome[0].firstChild.data
                    ome_end = float(ome_end)
                except IndexError:
                    ome = i.getElementsByTagName("commonPosition")
                    ome = ome[0].firstChild.data
                    ome_str = float(ome)
                    ome_end = float(ome)

        intensity_data = intensity[0].firstChild.data

        intensity_data = [float(x) for x in intensity_data.split()]
        n = len(intensity_data)

        self.theta = np.linspace(theta_str, theta_end, n)
        self.omega = np.linspace(ome_str, ome_end, n)
        self.intensity = np.array(intensity_data)

        self.xmin = np.min(self.omega)
        self.xmax = np.max(self.omega)
        self.ymin = np.min(self.intensity)
        self.ymax = np.max(self.intensity)
        self.export_button.setEnabled(True)
        self.plot_scan_data()
        # npdatas = np.vstack([ome, theta, np.array(intensity_data)])
        # df = pd.DataFrame(npdatas.T, columns=['omega', 'theta', 'Intensity'])
        #
        # df.to_csv(f"{os.path.splitext(filename)[0]}.csv", index=False)
        # df.to_csv(f"{os.path.splitext(filename)[0]}.txt", index=False)
        # print("All done!")

    def plot_scan_data(self, x=None, y=None):
        self.fig.clf()
        self.ax = self.fig.add_subplot(1, 1, 1)
        if self.flag_cb_plot_checked:
            x = [i for i in self.omega]
            y = [log_with_zero(i) for i in self.intensity]
            self.ax.plot(x, y)
        else:
            self.ax.plot(self.omega, self.intensity)
        # if (x is None) or (y is None):
        #     self.ax.plot(self.omega, self.intensity)
        # else:
        #     self.ax.plot(x, y)
        # self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.fig.show()

    def plot_log_changed(self, cb_id):
        if cb_id == 0:
            self.flag_cb_plot_checked = False
            # self.plot_scan_data()
        else:
            self.flag_cb_plot_checked = True

        if self.scan_type == 0:
            self.plot_scan_data()

        elif self.scan_type == 1:
            if cb_id == 0:
                self.xmin_SpinBox.setMaximum(1)
                self.xmin_SpinBox.setMinimum(-1)
                self.xmin_SpinBox.setSingleStep(0.001)

                self.xmax_SpinBox.setMaximum(1)
                self.xmax_SpinBox.setMinimum(-1)
                self.xmax_SpinBox.setSingleStep(0.001)

                self.ymin_SpinBox.setMaximum(1)
                self.ymin_SpinBox.setMinimum(-1)
                self.ymin_SpinBox.setSingleStep(0.001)

                self.ymax_SpinBox.setMaximum(1)
                self.ymax_SpinBox.setMinimum(-1)
                self.ymax_SpinBox.setSingleStep(0.001)
            else:
                self.xmin_SpinBox.setMaximum(180)
                self.xmin_SpinBox.setMinimum(-180)
                self.xmin_SpinBox.setSingleStep(0.1)

                self.xmax_SpinBox.setMaximum(180)
                self.xmax_SpinBox.setMinimum(-180)
                self.xmax_SpinBox.setSingleStep(0.1)

                self.ymin_SpinBox.setMaximum(180)
                self.ymin_SpinBox.setMinimum(-180)
                self.ymin_SpinBox.setSingleStep(0.1)

                self.ymax_SpinBox.setMaximum(180)
                self.ymax_SpinBox.setMinimum(-180)
                self.ymax_SpinBox.setSingleStep(0.1)

            self.draw_contourf()

    def import_area_data(self, data, intensity):
        theta_str = 1
        theta_end = 2
        counts = 0

        self.omega = np.mat([[]])
        self.theta = np.mat([[]])
        self.intensity = np.mat([[]])

        for i in data:
            if i.getAttribute('axis') == "2Theta":
                theta = i.getElementsByTagName("startPosition")
                theta_str = theta[0].firstChild.data
                theta_str = float(theta_str)
                theta = i.getElementsByTagName("endPosition")
                theta_end = theta[0].firstChild.data
                theta_end = float(theta_end)

            if i.getAttribute('axis') == "Omega":
                omega = i.getElementsByTagName("commonPosition")
                intensity_line = intensity[counts].firstChild.data
                intensity_line = [float(x) for x in intensity_line.split()]
                n = len(intensity_line)

                if len(omega) == 0:
                    omega_start = i.getElementsByTagName("startPosition")
                    omega_start = float(omega_start[0].firstChild.data)
                    omega_end = i.getElementsByTagName("endPosition")
                    omega_end = float(omega_end[0].firstChild.data)
                    omega = np.linspace(omega_start, omega_end, n)
                else:
                    omega = omega[0].firstChild.data
                    omega = float(omega)
                    omega = omega * np.ones(n)

                if self.omega.size == 0:
                    self.omega = omega
                    self.theta = np.linspace(theta_str, theta_end, n)
                    self.intensity = np.mat(intensity_line)
                else:
                    self.omega = np.row_stack((self.omega, omega))
                    self.theta = np.row_stack((self.theta, np.linspace(theta_str, theta_end, n)))
                    self.intensity = np.row_stack((self.intensity, np.mat(intensity_line)))
                # print(counts)
                counts += 1

        self.sb_zmax.blockSignals(True)
        self.sb_zmin.blockSignals(True)
        self.z_max = np.max(np.max(self.intensity))
        # print(self.z_max)
        self.sb_zmax.setMaximum(self.z_max * 10)
        self.sb_zmax.setSingleStep(1)
        self.sb_zmax.setValue(self.z_max)

        self.sb_zmin.setMaximum(self.z_max)
        self.sb_zmin.setValue(self.z_min)
        self.sb_zmax.blockSignals(False)
        self.sb_zmin.blockSignals(False)

        self.cal_qx_qz()

    def refresh_axis_lim(self):
        if self.flag_cb_plot_checked:
            self.xmin = math.floor(np.min(self.omega))
            self.xmax = math.ceil(np.max(self.omega))
            self.ymin = int(np.min(self.theta))
            self.ymax = math.ceil(np.max(self.theta))
        else:
            self.xmin = math.floor(np.min(self.qx) / 0.005) * 0.005
            self.xmax = math.ceil(np.max(self.qx) / 0.005) * 0.005
            self.ymin = int(np.min(self.qz) / 0.005) * 0.005
            self.ymax = math.ceil(np.max(self.qz) / 0.005) * 0.005

        self.xmin_SpinBox.blockSignals(True)
        self.xmax_SpinBox.blockSignals(True)
        self.ymin_SpinBox.blockSignals(True)
        self.ymax_SpinBox.blockSignals(True)
        self.xmin_SpinBox.setValue(self.xmin)
        self.xmax_SpinBox.setValue(self.xmax)
        self.ymin_SpinBox.setValue(self.ymin)
        self.ymax_SpinBox.setValue(self.ymax)
        self.xmin_SpinBox.blockSignals(False)
        self.xmax_SpinBox.blockSignals(False)
        self.ymin_SpinBox.blockSignals(False)
        self.ymax_SpinBox.blockSignals(False)

    def cal_qx_qz(self):
        self.qx = (np.cos(self.omega * np.pi / 180) - np.cos((self.theta - self.omega) * np.pi / 180)) / self.kapl1
        self.qz = (np.sin(self.omega * np.pi / 180) + np.sin((self.theta - self.omega) * np.pi / 180)) / self.kapl1
        self.draw_contourf()
        self.export_button.setEnabled(True)
        self.savePic_button.setEnabled(True)
        self.calib_button.setEnabled(False)
        self.addPeak_button.setEnabled(False)
        self.haven_calib_sub = False
        self.x_slide.setEnabled(False)
        self.xmin_SpinBox.setEnabled(True)
        self.xmax_SpinBox.setEnabled(True)
        self.ymin_SpinBox.setEnabled(True)
        self.ymax_SpinBox.setEnabled(True)
        self.sb_zmax.setEnabled(True)
        self.sb_zmin.setEnabled(True)

    def draw_contourf(self, refresh_axis=True):
        self.fig.clf()
        self.ax = self.fig.add_subplot(1, 1, 1)

        if refresh_axis:
            self.refresh_axis_lim()
        # with open(r'G:\data analysis\temp.pkl', 'wb') as file:
        #     pickle.dump(self.intensity, file)
        temp_z = deepcopy(self.intensity)
        temp_z[self.intensity < self.z_min] = np.nan

        if self.flag_cb_plot_checked:
            ac = self.ax.contourf(self.omega, self.theta, temp_z,
                                  np.logspace(np.floor(np.log10(np.min(self.intensity[self.intensity > 1e-5]))),
                                              np.ceil(np.log10(np.max(self.intensity))), 64),
                                  locator=ticker.LogLocator(),
                                  cmap=cm.jet)
            self.ax.set_xlabel('ω', self.font_axis_label)
            self.ax.set_ylabel('2θ', self.font_axis_label)

        else:
            ac = self.ax.contourf(self.qx, self.qz, temp_z,
                                  np.logspace(np.floor(np.log10(np.min(self.intensity[self.intensity > 1e-5]))),
                                              np.ceil(np.log10(np.max(self.intensity))), 64),
                                  locator=ticker.LogLocator(),
                                  cmap=cm.jet)

            self.ax.set_xlabel('q_x', self.font_axis_label)
            self.ax.set_ylabel('q_z', self.font_axis_label)
        self.fig.colorbar(ac, label='Intensity')
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.zoomed = False
        # 添加轴标和title

        self.ax.set_title(os.path.basename(self.filename), self.font_title)
        self.fig.show()

    def xmin_changed(self):
        self.xmin = self.xmin_SpinBox.value()
        # print(self.xmin)
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.zoomed = False
        # if not self.flag_cb_plot_checked:
        #     self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        #     self.zoomed = False

    def xmax_changed(self):
        self.xmax = self.xmax_SpinBox.value()
        # print(self.xmin)
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.zoomed = False
        # if not self.flag_cb_plot_checked:
        #     self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        #     self.zoomed = False

    def ymin_changed(self):
        self.ymin = self.ymin_SpinBox.value()
        # print(self.ymin)
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.zoomed = False
        # if not self.flag_cb_plot_checked:
        #     self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        #     self.zoomed = False

    def ymax_changed(self):
        self.ymax = self.ymax_SpinBox.value()
        # print(self.ymin)
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.zoomed = False
        # if not self.flag_cb_plot_checked:
        #     self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        #     self.zoomed = False

    def zmin_changed(self):
        self.z_min = self.sb_zmin.value()
        self.draw_contourf(refresh_axis=False)

    def zmax_changed(self):
        self.z_max = self.sb_zmax.value()
        self.draw_contourf(refresh_axis=False)

    def zoom_in(self, event):
        if event.inaxes != self.ax:
            return
        if self.qx.size == 0:
            return

        if event.button == MouseButton.LEFT:
            self.x_sel = event.xdata
            self.y_sel = event.ydata
            x_width = self.xmax - self.xmin
            y_width = self.ymax - self.ymin
            if not self.zoomed:
                self.ax.axis([self.x_sel - x_width / 10, self.x_sel + x_width / 10,
                              self.y_sel - y_width / 10, self.y_sel + y_width / 10])
                self.zoomed = True
            if self.sel_cross1:
                self.sel_cross1.remove()
                self.sel_cross2.remove()

            self.sel_cross1, = self.ax.plot([self.x_sel - x_width / 50, self.x_sel + x_width / 50],
                                            [self.y_sel, self.y_sel], linewidth=1, color='k')
            self.sel_cross2, = self.ax.plot([self.x_sel, self.x_sel],
                                            [self.y_sel - y_width / 50, self.y_sel + y_width / 50],
                                            linewidth=1, color='k')
            self.calib_button.setEnabled(True)
            if not self.haven_calib_sub:
                self.addPeak_button.setEnabled(False)
                self.x_slide.setEnabled(False)
        elif event.button == MouseButton.RIGHT:
            if self.sel_cross1:
                self.sel_cross1.remove()
                self.sel_cross2.remove()
                self.sel_cross1 = None
                self.sel_cross2 = None
            self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            self.zoomed = False
        elif event.button == MouseButton.MIDDLE:
            if self.zoomed:
                x_width = self.xmax - self.xmin
                y_width = self.ymax - self.ymin
                self.ax.axis([self.x_sel - x_width / 25, self.x_sel + x_width / 25,
                              self.y_sel - y_width / 25, self.y_sel + y_width / 25])

    def calib_sub_peak(self):
        if self.flag_cb_plot_checked:
            del_omega = self.omega0 - self.x_sel
            del_theta = self.theta0 - self.y_sel

            self.omega = self.omega + del_omega
            self.theta = self.theta + del_theta

            self.qx = (np.cos(self.omega * np.pi / 180) - np.cos((self.theta - self.omega) * np.pi / 180)) / self.kapl1
            self.qz = (np.sin(self.omega * np.pi / 180) + np.sin((self.theta - self.omega) * np.pi / 180)) / self.kapl1

            self.logging.setPlainText('ω_sub = %.5f, θ_sub = %.5f' % (self.omega0, self.theta0))
            self.logging.appendPlainText('δω = %.4f, δθ = %.4f' % (del_omega, del_theta))

        else:
            del_qx = self.qx_s0 - self.x_sel
            del_qz = self.qz_s0 - self.y_sel
            self.qx = self.qx + del_qx
            self.qz = self.qz + del_qz

            self.logging.setPlainText('qx_sub = %.5f, qz_sub = %.5f' % (self.qx_s0, self.qz_s0))
            self.logging.appendPlainText('del_qx = %.4f, del_qz = %.4f' % (del_qx, del_qz))

        self.draw_contourf()
        # print([del_qx, del_qz])

        self.addPeak_button.setEnabled(True)
        self.x_slide.setEnabled(True)
        self.haven_calib_sub = True
        # self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.draw_relaxation_line()
        self.zoomed = False

    def cal_peak(self):
        x = sym.Symbol("x")
        if self.flag_cb_plot_checked:
            angle1 = (self.y_sel - self.x_sel) / 180 * np.pi
            angle2 = self.x_sel/180*np.pi

            x_sel = (np.cos(angle2) - np.cos(angle1)) / self.kapl1
            y_sel = (np.sin(angle2) + np.sin(angle1)) / self.kapl1
        else:
            x_sel = self.x_sel
            y_sel = self.y_sel

        af_para = -1 * self.sin_phi / x_sel * np.sqrt(self.hkl_f.dot(self.hkl_f))
        af_ver = self.cos_phi / y_sel * np.sqrt(self.hkl_f.dot(self.hkl_f))
        # print(self.cos_phi * np.sqrt(self.hkl_f.dot(self.hkl_f)))
        af0_cal = (af_ver + self.ratioC * af_para) / (1 + self.ratioC)
        X_ge_sym = sym.solve(af0_cal - self.af0)
        for j in X_ge_sym:
            if 0 <= abs(j) <= 1.1:
                x_film = abs(j)
                break
        af0_N = self.af0.evalf(subs={x: x_film})
        R = (af_para - self.R_si) / (af0_N - self.R_si)
        # print(af0_N)
        x_width = self.xmax - self.xmin
        y_width = self.ymax - self.ymin
        self.ax.plot([self.x_sel - x_width / 16, self.x_sel + x_width / 16], [self.y_sel, self.y_sel],
                     linewidth=1, color=self.color_array[self.color_index])
        self.ax.plot([self.x_sel, self.x_sel], [self.y_sel - y_width / 16, self.y_sel + y_width / 16],
                     linewidth=1, color=self.color_array[self.color_index])
        add_test = ('x=%.3f, R=%.1f%%' % (x_film, R * 100))

        logging_str = f"Peak: sel_qs={x_sel:.4f}, sel_qz={y_sel:.4f}, \n" \
                      f"    x含量为：{x_film:.3f}, 未畸变晶格：{af0_N:.4f} \n" \
                      f"    af_//：{af_para:.4f}， 相比Si弛豫R： {R * 100:.1f}%"
        self.logging.appendPlainText(logging_str)

        if self.x_sel < self.xmin + x_width / 2:
            add_text_x = self.x_sel + x_width / 20
        else:
            add_text_x = self.x_sel - x_width / 2
        self.ax.text(add_text_x, self.y_sel, add_test, self.font_text, color=self.color_array[self.color_index])
        if self.color_index < len(self.color_array) - 1:
            self.color_index += 1
        else:
            self.color_index = 0

    def draw_relaxation_line(self):
        x_value = float(self.x_slide.value()) / 100
        # print([self.qx_f0, self.qz_f0])
        # print(x_value)
        if self.relaxation_line:
            self.relaxation_line.remove()

        qx_tmi = self.qx_s0 * (1 - x_value) + x_value * self.qx_f0
        qz_tmi = self.qz_s0 * (1 - x_value) + x_value * self.qz_f0
        # print(qx_tmi)
        # print(qz_tmi)
        self.relaxation_line, = self.ax.plot([self.qx_s0, qx_tmi],
                                             [self.qz_s0, qz_tmi],
                                             linewidth=2, linestyle='--', color='k')

    def export_text(self):
        save_name, _ = QFileDialog.getSaveFileName(self, '导出xrd数据', self.filename + '.txt', '*.txt')
        # print(save_name)
        if self.scan_type == 0:
            row = len(self.omega)
            with open(save_name, 'w') as txt:
                txt.write('  omega  \t  2theta  \t  intensity \n')
                for i in range(row):
                    temp = '%.12f  \t  %.12f  \t  %.12f \n' % (self.omega[i], self.theta[i], self.intensity[i])
                    txt.write(temp)
        elif self.scan_type == 1:
            row, col = self.omega.shape
            with open(save_name, 'w') as txt:
                txt.write('  omega  \t  2theta  \t qx  \t qz  \t intensity \n')
                for i in range(row):
                    for j in range(col):
                        temp = '%.12f  \t  %.12f \t  %.12f  \t  %.12f \t  %.12f \n' % (
                        self.omega[i, j], self.theta[i, j], self.qx[i, j],self.qz[i, j],self.intensity[i, j])
                        txt.write(temp)
        self.logging.appendPlainText(save_name + ' save succeed')

    def save_picture(self):
        save_name, _ = QFileDialog.getSaveFileName(self, '保存图片', self.filename + '.tif', '*.tif')
        print(save_name)
        plt.savefig(save_name, dpi=600)
        self.logging.appendPlainText(save_name + ' save succeed')

    def combox_changed(self, curr_text):
        self.le_kalp1.blockSignals(True)
        self.le_as0.blockSignals(True)
        self.le_af0.blockSignals(True)
        self.le_c11.blockSignals(True)
        self.le_c12.blockSignals(True)
        self.le_d_h.blockSignals(True)
        self.le_d_k.blockSignals(True)
        self.le_d_l.blockSignals(True)
        self.le_s_h.blockSignals(True)
        self.le_s_k.blockSignals(True)
        self.le_s_l.blockSignals(True)

        res = self.select_dict[curr_text]
        self.R_si = float(res[0])

        self.le_kalp1.setText(res[1])
        self.le_as0.setText(res[2])
        self.le_af0.setText(res[3])
        self.le_c11.setText(res[4])
        self.le_c12.setText(res[5])
        self.le_d_h.setText(res[6])
        self.le_d_k.setText(res[7])
        self.le_d_l.setText(res[8])
        self.le_s_h.setText(res[9])
        self.le_s_k.setText(res[10])
        self.le_s_l.setText(res[11])

        self.para_changed()

        self.le_kalp1.blockSignals(False)
        self.le_as0.blockSignals(False)
        self.le_af0.blockSignals(False)
        self.le_c11.blockSignals(False)
        self.le_c12.blockSignals(False)
        self.le_d_h.blockSignals(False)
        self.le_d_k.blockSignals(False)
        self.le_d_l.blockSignals(False)
        self.le_s_h.blockSignals(False)
        self.le_s_k.blockSignals(False)
        self.le_s_l.blockSignals(False)

    def new_combox_item(self):
        new_name, flat_ok = QInputDialog.getText(self, 'Name', '请输入保存名称', QLineEdit.EchoMode.Normal, '')
        if flat_ok:
            if new_name == '':
                QMessageBox.warning(self, 'error', '名称不能为空')
            elif new_name in self.select_dict.keys():
                QMessageBox.warning(self, 'error', f"{new_name} 已经存在，不同重复添加")
            else:
                curr_key = self.select_comboBox.currentText()
                self.select_dict[new_name] = self.select_dict[curr_key]
                self.select_comboBox.addItem(new_name)
                self.select_comboBox.setCurrentText(new_name)

    def delete_combox_item(self):
        curr_key = self.select_comboBox.currentText()
        ret = QMessageBox.warning(self, '确认', f"确认删除 {curr_key}?",
                                  QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
                                  QMessageBox.StandardButton.Ok)

        if ret == QMessageBox.StandardButton.Ok:
            if curr_key in self.default_key_ls:
                QMessageBox.warning(self, 'error', f"{curr_key} 为默认类型，无法删除")
            else:
                self.select_comboBox.blockSignals(True)
                self.select_dict.pop(curr_key)
                self.select_comboBox.clear()
                self.select_comboBox.addItems(self.select_dict.keys())
                self.select_comboBox.blockSignals(False)

                self.select_comboBox.setCurrentIndex(0)
                print(f'delete {curr_key}')

        else:
            print('abort')

    def save_combox_item(self):
        res = (self.le_a_ref.text(),
               self.le_kalp1.text(),
               self.le_as0.text(),
               self.le_af0.text(),
               self.le_c11.text(),
               self.le_c12.text(),
               self.le_d_h.text(),
               self.le_d_k.text(),
               self.le_d_l.text(),
               self.le_s_h.text(),
               self.le_s_k.text(),
               self.le_s_l.text())
        res_text = ',\n'.join(i for i in res)
        curr_key = self.select_comboBox.currentText()
        ret = QMessageBox.warning(self, '确认', f"确认保存 {curr_key}为 \n {res_text}",
                                  QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel,
                                  QMessageBox.StandardButton.Save)
        if ret == QMessageBox.StandardButton.Save:
            self.select_dict[curr_key] = res
            save_select_dict(self.select_dict)
            print("保存成功")

    def return_defalut(self):
        ret = QMessageBox.warning(self, '确认', f"确认恢复默认状态，所有自定义参数将会被删除",
                                  QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
                                  QMessageBox.StandardButton.Ok)
        if ret == QMessageBox.StandardButton.Ok:
            sel_dict = {
                "GexSi1-x / Si (001)": ("5.431", '1.540598', '5.431', '5.431 + 0.1992*x + 0.02733 * x**2',
                                        '165.8 - 37.3 * x', '63.9 - 15.6 * x', '-2', '-2', '4', '0', '0', '1'),
                "GexSi1-x / Si (111)": ("5.431", '1.540598', '5.431', '5.431 + 0.1992*x + 0.02733 * x**2',
                                        '165.8 - 37.3 * x', '63.9 - 15.6 * x', '2', '2', '4', '1', '1', '1'),
                "Ge1-xSix / Ge (001)": ("5.431", '1.540598', '5.6575', '5.65753 - 0.25386*x + 0.02733 * x**2',
                                        '128.5 + 37.3 * x', '48.3 + 15.6 * x', '-2', '-2', '4', '0', '0', '1'),
                "Ge1-xSix / Ge (111)": ("5.431", '1.540598', '5.6575', '5.65753 - 0.25386*x + 0.02733 * x**2',
                                        '128.5 + 37.3 * x', '48.3 + 15.6 * x', '2', '2', '4', '1', '1', '1'),
                "InxGa1-xAs / Si (001)": ("5.431", '1.540598', "5.431", '0.405 * x + 5.6533',
                                          '11.9 - 3.56 * x', '5.34 - 0.8 * x', '-2', '-2', '4', '0', '0', '1'),
            }
            # self.select_dict = sel_dict
            self.select_comboBox.blockSignals(True)
            self.select_dict = sel_dict
            self.select_comboBox.clear()
            self.select_comboBox.addItems(self.select_dict.keys())
            self.select_comboBox.blockSignals(False)
            save_select_dict(sel_dict)
            self.select_comboBox.setCurrentIndex(0)
            self.combox_changed("GexSi1-x / Si (001)")
