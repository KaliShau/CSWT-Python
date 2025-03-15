from src.screens.sign_up import Ui_SignUp

from src.functions.dialog import dialog

class sign_up_functions():
    def __init__(self, main_window, widgets, database_manager, visible, setUser):

        # init
        self.sign_up = Ui_SignUp()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.visible = visible
        self.setUser = setUser

        self.sign_up.errorLabel.setVisible(False)

        # buttons
        self.main_window.signUpButton.clicked.connect(self.openSignUp)
        self.sign_up.signInButton.clicked.connect(self.signUp)

    def openSignUp(self):
         self.widgets.change(self.sign_up)

    def signUp(self):

        username = self.sign_up.loginEdit.toPlainText()
        firstname = self.sign_up.firstNameEdit.toPlainText()
        lastname = self.sign_up.lastNameEdit.toPlainText()
        number = self.sign_up.phoneNumberEdit.toPlainText()

        password = self.sign_up.passwordEdit.toPlainText()
        confirmPassword = self.sign_up.confirmPasswordEdit.toPlainText()

        if not username or not firstname or not lastname or not number or not password or not confirmPassword:
            self.sign_up.errorLabel.setVisible(True)
            self.sign_up.errorLabel.setText('Все поля должны быть заполнены.')

            return False

        if password != confirmPassword:
            self.sign_up.errorLabel.setVisible(True)
            self.sign_up.errorLabel.setText('Пароль и подтверждение пароля должны совпадать.')

            return False

        self.database_manager.connect()
        checkUser = self.database_manager.get_user_by_username((username,))

        if checkUser:
            self.sign_up.errorLabel.setVisible(True)
            self.sign_up.errorLabel.setText('Недопустимый логин или пароль.')

            return False

        role = self.database_manager.get_role_by_name('Client')
        self.database_manager.sign_up(username, firstname, lastname, number, password, role[0])

        user = self.database_manager.sign_in(username, password)

        if not user:
            self.sign_up.errorLabel.setVisible(True)
            self.sign_up.errorLabel.setText('Недопустимый логин или пароль.')

            return False

        role = self.database_manager.get_role_by_id(user[9])

        self.setUser(user)

        if self.visible.check_role(role):
            self.widgets.change(self.main_window.startWidgetLayout)
            self.main_window.startLabel.setVisible(False)

            dialog.show(f'Регистрация успешно выполнена! Добро пожаловать {user[5]} {user[6]}')


        