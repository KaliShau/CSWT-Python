import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.screens.main_window import Ui_MainWindow

class AppTracker(QMainWindow):
    def __init__(self):
        super(AppTracker, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppTracker()
    window.show()

    sys.exit    (app.exec())