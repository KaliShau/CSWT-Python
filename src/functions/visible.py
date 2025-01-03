from src.screens.main_window import Ui_MainWindow

class visible():
    def __init__(self, main_window: Ui_MainWindow):
        self.main_window = main_window
        self.client()


    def auth(self):
        self.main_window.workBox.setVisible(False)
        self.main_window.reportsBox.setVisible(False)
        self.main_window.adminBox.setVisible(False)

        # profile menu
        self.main_window.action_2.setVisible(False)
        self.main_window.action_3.setVisible(False)
        self.main_window.action_5.setVisible(False)

    def admin(self):
        self.main_window.authBox.setVisible(False)
    
    def client(self):
        self.main_window.authBox.setVisible(False)
        self.main_window.listTicketsButton.setVisible(False)
        self.main_window.myAssignedTicketsButton.setVisible(False)
        self.main_window.reportsBox.setVisible(False)
        self.main_window.adminBox.setVisible(False)
    