import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.screens.main_window import Ui_MainWindow
from src.screens.sign_in import Ui_SignIn
from src.screens.sign_up import Ui_SignUp
from src.screens.create_ticket import Ui_CreateTicket
from src.screens.my_create_tickets import Ui_MyCreateTickets

from src.functions.visible import  visible
from src.functions.widgets import widgets

class AppTracker(QMainWindow):
    def __init__(self):
        super(AppTracker, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        # init widgets
        self.sign_in = Ui_SignIn()
        self.sign_up = Ui_SignUp()
        self.create_ticket = Ui_CreateTicket()
        self.my_create_tickets = Ui_MyCreateTickets()

        # init functions
        self.visible = visible(self.main_window)
        self.widgets = widgets(self.main_window, self.sign_in, self.sign_up, self.create_ticket, self.my_create_tickets)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppTracker()
    window.show()

    sys.exit(app.exec())