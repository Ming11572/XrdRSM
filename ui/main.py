# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_mainui(object):
    def setupUi(self, mainui):
        if not mainui.objectName():
            mainui.setObjectName(u"mainui")
        mainui.resize(345, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainui.sizePolicy().hasHeightForWidth())
        mainui.setSizePolicy(sizePolicy)
        mainui.setMinimumSize(QSize(345, 650))
        mainui.setMaximumSize(QSize(345, 650))
        self.verticalLayout_3 = QVBoxLayout(mainui)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.import_button = QPushButton(mainui)
        self.import_button.setObjectName(u"import_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.import_button)

        self.export_button = QPushButton(mainui)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.export_button)

        self.savePic_button = QPushButton(mainui)
        self.savePic_button.setObjectName(u"savePic_button")
        self.savePic_button.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.savePic_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.calib_button = QPushButton(mainui)
        self.calib_button.setObjectName(u"calib_button")
        self.calib_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.calib_button.sizePolicy().hasHeightForWidth())
        self.calib_button.setSizePolicy(sizePolicy1)
        self.calib_button.setCheckable(False)
        self.calib_button.setChecked(False)
        self.calib_button.setAutoDefault(False)

        self.horizontalLayout_9.addWidget(self.calib_button)

        self.cb_plot_log = QCheckBox(mainui)
        self.cb_plot_log.setObjectName(u"cb_plot_log")

        self.horizontalLayout_9.addWidget(self.cb_plot_log)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.addPeak_button = QPushButton(mainui)
        self.addPeak_button.setObjectName(u"addPeak_button")
        self.addPeak_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.addPeak_button.sizePolicy().hasHeightForWidth())
        self.addPeak_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.addPeak_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.x_label = QLabel(mainui)
        self.x_label.setObjectName(u"x_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy2)
        self.x_label.setMinimumSize(QSize(30, 0))
        self.x_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.x_label)

        self.x_slide = QSlider(mainui)
        self.x_slide.setObjectName(u"x_slide")
        self.x_slide.setEnabled(False)
        self.x_slide.setMaximum(100)
        self.x_slide.setValue(100)
        self.x_slide.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.x_slide)

        self.zmax_label = QLabel(mainui)
        self.zmax_label.setObjectName(u"zmax_label")
        sizePolicy2.setHeightForWidth(self.zmax_label.sizePolicy().hasHeightForWidth())
        self.zmax_label.setSizePolicy(sizePolicy2)
        self.zmax_label.setMinimumSize(QSize(30, 0))
        self.zmax_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.zmax_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(mainui)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.logging = QPlainTextEdit(mainui)
        self.logging.setObjectName(u"logging")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        self.logging.setFont(font)
        self.logging.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.logging)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(mainui)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.xmin_SpinBox = QDoubleSpinBox(mainui)
        self.xmin_SpinBox.setObjectName(u"xmin_SpinBox")
        self.xmin_SpinBox.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.xmin_SpinBox.sizePolicy().hasHeightForWidth())
        self.xmin_SpinBox.setSizePolicy(sizePolicy4)
        self.xmin_SpinBox.setDecimals(3)
        self.xmin_SpinBox.setMinimum(-1.000000000000000)
        self.xmin_SpinBox.setMaximum(1.000000000000000)
        self.xmin_SpinBox.setSingleStep(0.001000000000000)

        self.horizontalLayout_4.addWidget(self.xmin_SpinBox)

        self.label_12 = QLabel(mainui)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.xmax_SpinBox = QDoubleSpinBox(mainui)
        self.xmax_SpinBox.setObjectName(u"xmax_SpinBox")
        self.xmax_SpinBox.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.xmax_SpinBox.sizePolicy().hasHeightForWidth())
        self.xmax_SpinBox.setSizePolicy(sizePolicy4)
        self.xmax_SpinBox.setDecimals(3)
        self.xmax_SpinBox.setMinimum(-1.000000000000000)
        self.xmax_SpinBox.setMaximum(1.000000000000000)
        self.xmax_SpinBox.setSingleStep(0.001000000000000)

        self.horizontalLayout_4.addWidget(self.xmax_SpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_14 = QLabel(mainui)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.ymin_SpinBox = QDoubleSpinBox(mainui)
        self.ymin_SpinBox.setObjectName(u"ymin_SpinBox")
        self.ymin_SpinBox.setEnabled(False)
        self.ymin_SpinBox.setDecimals(3)
        self.ymin_SpinBox.setMinimum(-1.000000000000000)
        self.ymin_SpinBox.setMaximum(1.000000000000000)
        self.ymin_SpinBox.setSingleStep(0.001000000000000)

        self.horizontalLayout_5.addWidget(self.ymin_SpinBox)

        self.label_13 = QLabel(mainui)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.ymax_SpinBox = QDoubleSpinBox(mainui)
        self.ymax_SpinBox.setObjectName(u"ymax_SpinBox")
        self.ymax_SpinBox.setEnabled(False)
        self.ymax_SpinBox.setDecimals(3)
        self.ymax_SpinBox.setMinimum(-1.000000000000000)
        self.ymax_SpinBox.setMaximum(1.000000000000000)
        self.ymax_SpinBox.setSingleStep(0.001000000000000)

        self.horizontalLayout_5.addWidget(self.ymax_SpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(mainui)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.sb_zmin = QDoubleSpinBox(mainui)
        self.sb_zmin.setObjectName(u"sb_zmin")
        self.sb_zmin.setEnabled(False)
        self.sb_zmin.setDecimals(3)
        self.sb_zmin.setMinimum(-1.000000000000000)
        self.sb_zmin.setMaximum(1.000000000000000)
        self.sb_zmin.setSingleStep(0.001000000000000)

        self.horizontalLayout_11.addWidget(self.sb_zmin)

        self.label_19 = QLabel(mainui)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_19)

        self.sb_zmax = QDoubleSpinBox(mainui)
        self.sb_zmax.setObjectName(u"sb_zmax")
        self.sb_zmax.setEnabled(False)
        self.sb_zmax.setDecimals(3)
        self.sb_zmax.setMinimum(-1.000000000000000)
        self.sb_zmax.setMaximum(100000.000000000000000)
        self.sb_zmax.setSingleStep(0.001000000000000)

        self.horizontalLayout_11.addWidget(self.sb_zmax)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pb_new = QPushButton(mainui)
        self.pb_new.setObjectName(u"pb_new")

        self.horizontalLayout_10.addWidget(self.pb_new)

        self.pb_save = QPushButton(mainui)
        self.pb_save.setObjectName(u"pb_save")

        self.horizontalLayout_10.addWidget(self.pb_save)

        self.pb_delete = QPushButton(mainui)
        self.pb_delete.setObjectName(u"pb_delete")

        self.horizontalLayout_10.addWidget(self.pb_delete)

        self.pb_reload = QPushButton(mainui)
        self.pb_reload.setObjectName(u"pb_reload")

        self.horizontalLayout_10.addWidget(self.pb_reload)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(mainui)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_16 = QLabel(mainui)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_16)

        self.label_5 = QLabel(mainui)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(mainui)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(mainui)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(mainui)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(mainui)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(mainui)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label = QLabel(mainui)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.select_comboBox = QComboBox(mainui)
        self.select_comboBox.setObjectName(u"select_comboBox")

        self.verticalLayout_2.addWidget(self.select_comboBox)

        self.le_a_ref = QLineEdit(mainui)
        self.le_a_ref.setObjectName(u"le_a_ref")

        self.verticalLayout_2.addWidget(self.le_a_ref)

        self.le_kalp1 = QLineEdit(mainui)
        self.le_kalp1.setObjectName(u"le_kalp1")

        self.verticalLayout_2.addWidget(self.le_kalp1)

        self.le_as0 = QLineEdit(mainui)
        self.le_as0.setObjectName(u"le_as0")

        self.verticalLayout_2.addWidget(self.le_as0)

        self.le_af0 = QLineEdit(mainui)
        self.le_af0.setObjectName(u"le_af0")

        self.verticalLayout_2.addWidget(self.le_af0)

        self.le_c11 = QLineEdit(mainui)
        self.le_c11.setObjectName(u"le_c11")

        self.verticalLayout_2.addWidget(self.le_c11)

        self.le_c12 = QLineEdit(mainui)
        self.le_c12.setObjectName(u"le_c12")

        self.verticalLayout_2.addWidget(self.le_c12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.le_d_h = QLineEdit(mainui)
        self.le_d_h.setObjectName(u"le_d_h")

        self.horizontalLayout_8.addWidget(self.le_d_h)

        self.le_d_k = QLineEdit(mainui)
        self.le_d_k.setObjectName(u"le_d_k")

        self.horizontalLayout_8.addWidget(self.le_d_k)

        self.le_d_l = QLineEdit(mainui)
        self.le_d_l.setObjectName(u"le_d_l")

        self.horizontalLayout_8.addWidget(self.le_d_l)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.le_s_h = QLineEdit(mainui)
        self.le_s_h.setObjectName(u"le_s_h")

        self.horizontalLayout_7.addWidget(self.le_s_h)

        self.le_s_k = QLineEdit(mainui)
        self.le_s_k.setObjectName(u"le_s_k")

        self.horizontalLayout_7.addWidget(self.le_s_k)

        self.le_s_l = QLineEdit(mainui)
        self.le_s_l.setObjectName(u"le_s_l")

        self.horizontalLayout_7.addWidget(self.le_s_l)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(mainui)

        self.calib_button.setDefault(False)


        QMetaObject.connectSlotsByName(mainui)
    # setupUi

    def retranslateUi(self, mainui):
        mainui.setWindowTitle(QCoreApplication.translate("mainui", u"Xrd RSM analysis", None))
        self.import_button.setText(QCoreApplication.translate("mainui", u"Import", None))
        self.export_button.setText(QCoreApplication.translate("mainui", u"Export", None))
        self.savePic_button.setText(QCoreApplication.translate("mainui", u"Save Picture", None))
        self.calib_button.setText(QCoreApplication.translate("mainui", u"CalibSub", None))
        self.cb_plot_log.setText(QCoreApplication.translate("mainui", u"plog_log", None))
        self.addPeak_button.setText(QCoreApplication.translate("mainui", u"AddPeak", None))
        self.x_label.setText(QCoreApplication.translate("mainui", u"0", None))
        self.zmax_label.setText(QCoreApplication.translate("mainui", u"100", None))
        self.label_15.setText(QCoreApplication.translate("mainui", u"Outputs:", None))
        self.label_11.setText(QCoreApplication.translate("mainui", u"Xmin", None))
        self.label_12.setText(QCoreApplication.translate("mainui", u"Xmax", None))
        self.label_14.setText(QCoreApplication.translate("mainui", u"Ymin", None))
        self.label_13.setText(QCoreApplication.translate("mainui", u"Ymax", None))
        self.label_18.setText(QCoreApplication.translate("mainui", u"Zmin", None))
        self.label_19.setText(QCoreApplication.translate("mainui", u"Zmax", None))
        self.pb_new.setText(QCoreApplication.translate("mainui", u"\u65b0\u589e", None))
        self.pb_save.setText(QCoreApplication.translate("mainui", u"\u4fdd\u5b58", None))
        self.pb_delete.setText(QCoreApplication.translate("mainui", u"\u5220\u9664", None))
        self.pb_reload.setText(QCoreApplication.translate("mainui", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.label_4.setText(QCoreApplication.translate("mainui", u"\u4f53\u7cfb\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("mainui", u"\u5e94\u53d8\u5f1b\u8c6b\u53c2\u8003\u503c(\u00c5)", None))
        self.label_5.setText(QCoreApplication.translate("mainui", u"X\u5c04\u7ebf\u6ce2\u957f(\u00c5)", None))
        self.label_6.setText(QCoreApplication.translate("mainui", u"\u886c\u5e95\u6676\u683c\u5e38\u6570(\u00c5)", None))
        self.label_7.setText(QCoreApplication.translate("mainui", u"\u5916\u5ef6\u5c42\u6676\u683c\u5e38\u6570(\u00c5)", None))
        self.label_8.setText(QCoreApplication.translate("mainui", u"C11(GPa)", None))
        self.label_9.setText(QCoreApplication.translate("mainui", u"C12(GPa)", None))
        self.label_10.setText(QCoreApplication.translate("mainui", u"\u884d\u5c04\u6676\u9762HKL ", None))
        self.label.setText(QCoreApplication.translate("mainui", u"\u8868\u9762HKL", None))
        self.le_a_ref.setText(QCoreApplication.translate("mainui", u"5.431", None))
        self.le_kalp1.setText(QCoreApplication.translate("mainui", u"1.540598", None))
        self.le_as0.setText(QCoreApplication.translate("mainui", u"5.431", None))
        self.le_af0.setText(QCoreApplication.translate("mainui", u"5.431 + 0.1992*x + 0.02733 * x**2", None))
        self.le_c11.setText(QCoreApplication.translate("mainui", u"165.8 - 37.3 * x", None))
        self.le_c12.setText(QCoreApplication.translate("mainui", u"63.9 - 15.6 * x", None))
        self.le_d_h.setText(QCoreApplication.translate("mainui", u"-2", None))
        self.le_d_k.setText(QCoreApplication.translate("mainui", u"-2", None))
        self.le_d_l.setText(QCoreApplication.translate("mainui", u"4", None))
        self.le_s_h.setText(QCoreApplication.translate("mainui", u"0", None))
        self.le_s_k.setText(QCoreApplication.translate("mainui", u"0", None))
        self.le_s_l.setText(QCoreApplication.translate("mainui", u"1", None))
    # retranslateUi

