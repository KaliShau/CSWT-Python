from src.screens.sign_in import Ui_SignIn

from src.functions.dialog import dialog

class sign_in_functions():
    def __init__(self, main_window, widgets, database_manager, visible, setUser):

        # init
        self.sign_in = Ui_SignIn()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.visible = visible
        self.setUser = setUser

        self.sign_in.errorLabel.setVisible(False)

        # buttons
        self.main_window.signInButton.clicked.connect(self.openSignIn)
        self.sign_in.signInButton.clicked.connect(self.signIn)

    def openSignIn(self):
         self.widgets.change(self.sign_in)

    def signIn(self):
        self.database_manager.connect()

        username = self.sign_in.loginEdit.toPlainText()
        password = self.sign_in.passwordEdit.toPlainText()

        if not username or not password:
            self.sign_in.errorLabel.setVisible(True)
            self.sign_in.errorLabel.setText('Все поля должны быть заполнены.')

            return False
        
        user = self.database_manager.sign_in(username, password)

        if not user:
            self.sign_in.errorLabel.setVisible(True)
            self.sign_in.errorLabel.setText('Неверный логин или пароль.')

            return False

        role = self.database_manager.get_role_by_id(user[9])

        self.setUser(user)

        if self.visible.check_role(role):
            self.widgets.change(self.main_window.startWidgetLayout)
            self.main_window.startLabel.setVisible(False)

            dialog.show(f'Вход успешно выполнен! Добро пожаловать {user[5]} {user[6]}')
