from src.screens.main_window import Ui_MainWindow

class visible():
    def __init__(self, main_window: Ui_MainWindow):
        self.main_window = main_window
        self.auth()

    def check_role(self, user):
        role = user[9]

        if role == 1:
            self.admin()

        if role == 2:
            self.ASU_staff()

        if role == 3:
            self.client()

    def auth(self):
        self.main_window.workBox.setVisible(False)
        self.main_window.reportsBox.setVisible(False)
        self.main_window.adminBox.setVisible(False)
        self.main_window.authBox.setVisible(True)

        # profile menu
        self.main_window.action_2.setVisible(False)
        self.main_window.action_3.setVisible(False)
        self.main_window.action_5.setVisible(False)
        self.main_window.action.setVisible(True)

        # buttons
        self.main_window.availableTicketsButton.setVisible(False)
        self.main_window.myAssignedTicketsButton.setVisible(False)

    def admin(self):
        self.main_window.workBox.setVisible(True)
        self.main_window.reportsBox.setVisible(True)
        self.main_window.adminBox.setVisible(True)
        self.main_window.authBox.setVisible(False)

        # profile menu
        self.main_window.action_2.setVisible(True)
        self.main_window.action_3.setVisible(True)
        self.main_window.action_5.setVisible(True)
        self.main_window.action.setVisible(False)
        

        # buttons
        self.main_window.availableTicketsButton.setVisible(True)
        self.main_window.myAssignedTicketsButton.setVisible(True)
    
    def client(self):
        self.main_window.workBox.setVisible(True)
        self.main_window.reportsBox.setVisible(False)
        self.main_window.adminBox.setVisible(False)
        self.main_window.authBox.setVisible(False)

        # profile menu
        self.main_window.action_2.setVisible(True)
        self.main_window.action_3.setVisible(True)
        self.main_window.action_5.setVisible(True)
        self.main_window.action.setVisible(False)

        # buttons
        self.main_window.availableTicketsButton.setVisible(False)
        self.main_window.myAssignedTicketsButton.setVisible(False)

    def ASU_staff(self):
        self.main_window.workBox.setVisible(True)
        self.main_window.reportsBox.setVisible(True)
        self.main_window.adminBox.setVisible(False)
        self.main_window.authBox.setVisible(False)

        # profile menu
        self.main_window.action_2.setVisible(True)
        self.main_window.action_3.setVisible(True)
        self.main_window.action_5.setVisible(True)
        self.main_window.action.setVisible(False)

        # buttons
        self.main_window.availableTicketsButton.setVisible(True)
        self.main_window.myAssignedTicketsButton.setVisible(True)
    