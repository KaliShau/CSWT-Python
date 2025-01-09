import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.screens.main_window import Ui_MainWindow

from src.functions.visible import  visible
from src.functions.widgets import widgets
from src.functions.config import config

from src.db.database_manager import database_manager

from src.functions.screens.db_config_functions import db_config_functions
from src.functions.screens.sign_in_functions import sign_in_functions
from src.functions.screens.sign_up_functions import sign_up_functions
from src.functions.screens.available_tickets_functions import available_tickets_functions
from src.functions.screens.create_ticket_functions import create_ticket_functions
from src.functions.screens.my_create_tickets_functions import my_create_tickets_functions
from src.functions.screens.my_assigned_tickets_functions import my_assigned_tickets_functions

class AppTracker(QMainWindow):
    def __init__(self):
        super(AppTracker, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        # config
        config().create_config()
        self.user = None

        # init functions
        self.widgets = widgets(self.main_window)
        self.visible = visible(self.main_window)
        self.database_manager = database_manager()

        self.init_functions_widgets()

    def init_functions_widgets(self):
        self.db_config_functions = db_config_functions(self.main_window, self.widgets, self.database_manager)
        self.sign_in_functions = sign_in_functions(self.main_window, self.widgets)
        self.sign_up_functions = sign_up_functions(self.main_window, self.widgets, self.database_manager, self.visible, self.setUser)
        self.available_tickets_functions = available_tickets_functions(self.main_window, self.widgets)
        self.create_ticket_functions = create_ticket_functions(self.main_window, self.widgets, self.user)
        self.my_create_tickets_functions = my_create_tickets_functions(self.main_window, self.widgets)
        self.my_assigned_tickets_functions = my_assigned_tickets_functions(self.main_window, self.widgets)

    def setUser(self, user):
        self.user = user
        self.init_functions_widgets()

    def closeEvent(self, event):
        self.database_manager.disconnect()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppTracker()
    window.show()

    sys.exit(app.exec())