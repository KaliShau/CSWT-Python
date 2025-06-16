from .users import Ui_Users

from src.shared.utils.load_table import table
from src.shared.utils.dialog import dialog

from src.pages.update_user.update_user_functions import update_user_functions

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

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

        # config 
        self.users.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.users.tableView.customContextMenuRequested.connect(self.showContextMenu)

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

        self.users.loginEdit.clear()
        self.users.passwordEdit.clear()
        self.users.firstNameEdit.clear()
        self.users.lastNameEdit.clear()
        self.users.phoneNumberEdit.clear()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.users.tableView)

        delete_action = menu.addAction('Удалить')
        ticket_edit_action = menu.addAction('Редактировать')

        index = self.users.tableView.indexAt(position)

        if index.isValid():
            model = self.users.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                user_id = int(id_item.text())
                action = menu.exec(self.users.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                    role = self.database_manager.get_role_by_name('Deleted')

                    self.database_manager.delete_user(user_id, role[0])
                    self.loadUsers()
                
                if action == ticket_edit_action:
                    self.update_user_functions = update_user_functions(self.main_window, self.widgets, self.database_manager, user_id)

                    self.update_user_functions.openUpdateUser()