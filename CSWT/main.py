import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.pages.main_window.main_window import Ui_MainWindow

from src.shared.utils.visible import  visible
from src.shared.utils.widgets import widgets
from src.shared.utils.config import config

from src.core.db.database_manager import database_manager

from src.pages.db_config.db_config_functions import db_config_functions
from src.pages.sign_in.sign_in_functions import sign_in_functions
from src.pages.sign_up.sign_up_functions import sign_up_functions
from src.pages.available_tickets.available_tickets_functions import available_tickets_functions
from src.pages.create_ticket.create_ticket_functions import create_ticket_functions
from src.pages.my_create_tickets.my_create_tickets_functions import my_create_tickets_functions
from src.pages.my_assigned_tickets.my_assigned_tickets_functions import my_assigned_tickets_functions
from src.pages.users.users_functions import users_functions
from src.pages.roles.roles_functions import roles_functions
from src.pages.departments.departments_functions import departments_functions
from src.pages.update_user.update_user_functions import update_user_functions
from src.pages.priorities.priorities_functions import priorities_functions

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
        self.sign_up_functions = sign_up_functions(self.main_window, self.widgets, self.database_manager, self.visible, self.setUser)
        self.sign_in_functions = sign_in_functions(self.main_window, self.widgets, self.database_manager, self.visible, self.setUser)

        if not self.user:
            return False

        self.my_create_tickets_functions = my_create_tickets_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.available_tickets_functions = available_tickets_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.create_ticket_functions = create_ticket_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.my_assigned_tickets_functions = my_assigned_tickets_functions(self.main_window, self.widgets, self.database_manager, self.user)
        
        self.users_functions = users_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.roles_functions = roles_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.departments_functions = departments_functions(self.main_window, self.widgets, self.database_manager, self.user)
        self.priorities_functions = priorities_functions(self.main_window, self.widgets, self.database_manager, self.user)
        
        self.main_window.action_5.triggered.connect(self.sign_out)
        self.main_window.action_2.triggered.connect(self.openUpdateProfile)



    def setUser(self, user):
        self.user = user
        self.init_functions_widgets()

    def closeEvent(self, event):
        self.database_manager.disconnect()
        event.accept()

    def sign_out(self):

        self.database_manager.disconnect()
        self.user = None
        self.visible.auth()
        self.widgets.change(self.main_window.startWidgetLayout)
        self.main_window.startLabel.setVisible(True)

        self.init_functions_widgets()

    def openUpdateProfile(self):
        self.update_user_functions = update_user_functions(self.main_window, self.widgets, self.database_manager, self.user[0])

        self.update_user_functions.openUpdateProfile()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppTracker()
    window.show()

    sys.exit(app.exec())