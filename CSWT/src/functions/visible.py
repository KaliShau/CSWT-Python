from src.functions.dialog import dialog

class visible():
    def __init__(self, main_window):
        self.main_window = main_window
        self.auth()

    def check_role(self, role):

        role_name = role[3]

        if role_name == 'Admin':
            self.admin()

            return True

        if role_name == 'ASU_staff':
            self.ASU_staff()

            return True

        if role_name == 'Client':
            self.client()

            return True
            
        dialog.show('Ваша роль не найдена. Обратиться к администратору.')
        return False

    def auth(self):
        self.main_window.workBox.setVisible(False)
        self.main_window.reportsBox.setVisible(False)
        self.main_window.adminBox.setVisible(False)
        self.main_window.authBox.setVisible(True)

        # menu
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

        # menu
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

        # menu
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

        # menu
        self.main_window.action_2.setVisible(True)
        self.main_window.action_3.setVisible(True)
        self.main_window.action_5.setVisible(True)
        self.main_window.action.setVisible(False)

        # buttons
        self.main_window.availableTicketsButton.setVisible(True)
        self.main_window.myAssignedTicketsButton.setVisible(True)
    