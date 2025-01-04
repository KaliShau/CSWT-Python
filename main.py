import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.screens.main_window import Ui_MainWindow
from src.screens.sign_in import Ui_SignIn
from src.screens.sign_up import Ui_SignUp
from src.screens.create_ticket import Ui_CreateTicket
from src.screens.my_create_tickets import Ui_MyCreateTickets
from src.screens.my_assigned_tickets import Ui_MyAssignedTickets
from src.screens.available_tickets import Ui_AvailableTickets
from src.screens.db_config import Ui_DbConfig

from src.functions.visible import  visible
from src.functions.widgets import widgets
from src.functions.config import config

from src.functions.db_config_functions import db_config_functions

class AppTracker(QMainWindow):
    def __init__(self):
        super(AppTracker, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        # config
        self.config = config()
        self.config.create_config()

        # init widgets
        self.sign_in = Ui_SignIn()
        self.sign_up = Ui_SignUp()
        self.create_ticket = Ui_CreateTicket()
        self.my_create_tickets = Ui_MyCreateTickets()
        self.my_assigned_tickets = Ui_MyAssignedTickets()
        self.available_tickets = Ui_AvailableTickets()
        self.db_config = Ui_DbConfig(self.config.load_config())

        # init functions
        self.widgets = widgets(self.main_window, self.sign_in, self.sign_up, self.create_ticket, self.my_create_tickets, self.my_assigned_tickets, self.available_tickets, self.db_config)
        self.visible = visible(self.main_window)

        self.db_config_functions = db_config_functions(self.config, self.db_config)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppTracker()
    window.show()

    sys.exit(app.exec())