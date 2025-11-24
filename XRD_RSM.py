from PySide6.QtWidgets import QApplication
from XrdRSMAnalysis import XrdRSM

if __name__ == '__main__':
    app = QApplication([])
    stats = XrdRSM()
    stats.show()

    app.exec()

