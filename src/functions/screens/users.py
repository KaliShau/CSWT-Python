from src.screens.users import Ui_Users

from src.functions.load_table import table
from src.functions.dialog import dialog

headers = ['ID', 'Дата создания', 'Дата обновления', 'Логин', 'Пароль', 'Имя', 'Фамилия', 'Email', 'Номер телефона', 'Роль', 'Отделы']

class users_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.users = Ui_Users()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.usersButton.clicked.connect(self.openUsers)
        self.users.searchButton.clicked.connect(self.searchData)
        self.users.createButton.clicked.connect(self.create_user)

    def openUsers(self):
        self.widgets.change(self.users)

        self.loadUsers()
        self.getRoles()

    def getRoles(self):
        roles = self.database_manager.get_roles()
        roles_names = [item[3] for item in roles]

        self.users.rolesComboBox.clear()
        self.users.rolesComboBox.addItems(roles_names)


    def loadUsers(self):
        data = self.database_manager.get_users()

        table.load(headers, self.users.tableView, data)


    def loadUsersByTitle(self, search_term):
        data = self.database_manager.get_users_search(search_term)

        table.load(headers, self.users.tableView, data)

    def searchData(self):
        search_term = self.users.searchEdit.toPlainText()

        if search_term:
            self.loadUsersByTitle(search_term)
        else:
            self.loadUsers()

    def create_user(self):
        username = self.users.loginEdit.toPlainText()
        password = self.users.passwordEdit.toPlainText()
        firstname = self.users.firstNameEdit.toPlainText()
        lastname = self.users.lastNameEdit.toPlainText()
        number = self.users.phoneNumberEdit.toPlainText()
        role = self.database_manager.get_role_by_name(self.users.rolesComboBox.currentText())

        if not username or not firstname or not lastname or not number or not password or not role:
            dialog.show('Поля не заполнены.')

            return False
        
        self.database_manager.sign_up(username, firstname, lastname, number, password, role[0])

        self.loadUsers()
        dialog.show('Пользователь успешно добавлен.')

        username = self.users.loginEdit.clear()
        password = self.users.passwordEdit.clear()
        firstname = self.users.firstNameEdit.clear()
        lastname = self.users.lastNameEdit.clear()
        number = self.users.phoneNumberEdit.clear()
