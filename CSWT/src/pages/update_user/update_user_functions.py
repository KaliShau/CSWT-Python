from .update_user import Ui_UpdateUser

from src.shared.utils.dialog import dialog
from src.shared.utils.load_table import table

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

headers = ['ID', 'Дата добавления', 'Дата обновления', 'Название', 'Описание']

class update_user_functions():
    def __init__(self, main_window, widgets, database_manager, user_id):

        # init
        self.update_user = Ui_UpdateUser()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user_id = user_id

        # buttons
        self.update_user.addDepartmentButton.clicked.connect(self.addDepartment)
        self.update_user.updateTicketButton.clicked.connect(self.updateUser)

        # config
        self.update_user.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.update_user.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openUpdateUser(self):
         self.widgets.change(self.update_user)

         self.loadUser()

    def openUpdateProfile(self):
        self.widgets.change(self.update_user)
        self.update_user.roleLabel.setVisible(False)
        self.update_user.roleComboBox.setVisible(False)

        self.loadUser()

    def loadUser(self):
        user = self.database_manager.get_user_by_id(self.user_id)

        self.update_user.usernameEdit.setPlainText(user[3])
        self.update_user.passwordEdit.setPlainText(user[4])
        self.update_user.firstnameEdit.setPlainText(user[5])
        self.update_user.lastnameEdit.setPlainText(user[6])
        self.update_user.emailEdit.setPlainText(user[7])
        self.update_user.phoneNumberEdit.setPlainText(user[8])

        self.loadDepartmentsForTable()
        self.currentRole(user)
        self.loadDepartmentsForComboBox()

    def currentRole(self, user):
        roles = self.database_manager.get_roles()
        roles_names = [item[3] for item in roles]

        self.update_user.roleComboBox.addItems(roles_names)

        current_role = self.database_manager.get_role_by_id(user[9])
        current_role_name = current_role[3]

        index = roles_names.index(current_role_name) if current_role_name in roles_names else -1

        if index != -1:
            self.update_user.roleComboBox.setCurrentIndex(index)

    def loadDepartmentsForTable(self):
        departments = self.database_manager.get_departments_by_user_id(self.user_id)

        table.load(headers, self.update_user.tableView, departments)

    def loadDepartmentsForComboBox(self):
        self.update_user.departmentsComboBox.clear()
        departments = self.database_manager.get_departments_not_in_user(self.user_id)
        departments_names = [item[1] for item in departments]

        self.update_user.departmentsComboBox.addItems(departments_names)

    def addDepartment(self):
        department_name = self.update_user.departmentsComboBox.currentText()

        if department_name:
            department = self.database_manager.get_department_by_name(department_name)

            self.database_manager.add_department(self.user_id, department[0])
            self.loadDepartmentsForTable()
            self.loadDepartmentsForComboBox()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.update_user.tableView)

        delete_action = menu.addAction('Удалить')

        index = self.update_user.tableView.indexAt(position)

        if index.isValid():
            model = self.update_user.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                department_id = int(id_item.text())
                action = menu.exec(self.update_user.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                        self.database_manager.delete_user_department(self.user_id, department_id)
                        self.loadDepartmentsForTable()
                        self.loadDepartmentsForComboBox()
    
    def updateUser(self):
        username = self.update_user.usernameEdit.toPlainText()
        password = self.update_user.passwordEdit.toPlainText()
        firstname = self.update_user.firstnameEdit.toPlainText()
        lastname = self.update_user.lastnameEdit.toPlainText()
        email = self.update_user.emailEdit.toPlainText()
        number = self.update_user.phoneNumberEdit.toPlainText()
        role = self.database_manager.get_role_by_name(self.update_user.roleComboBox.currentText())

        if not username or not password or not firstname or not lastname or not number or not role:
            dialog.show('Заполните поля.')

            return False

        if not email:
            email = None
        
        self.database_manager.update_user(username, password, firstname, lastname, email, number, role[0], self.user_id)