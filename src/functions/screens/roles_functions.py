from src.screens.roles import Ui_Roles

from src.functions.load_table import table
from src.functions.dialog import dialog

from src.functions.screens.update_role_functions  import update_role_functions

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

headers = ['ID', 'Дата создания', 'Дата обновления', 'Название', 'Описание']

class roles_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.roles = Ui_Roles()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.rolesButton.clicked.connect(self.openRoles)
        self.roles.searchButton.clicked.connect(self.searchData)
        self.roles.createButton.clicked.connect(self.createRole)

        # config 
        self.roles.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.roles.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openRoles(self):
        self.widgets.change(self.roles)

        self.loadRoles()

    def loadRoles(self):
        data = self.database_manager.get_roles()

        table.load(headers, self.roles.tableView, data)


    def loadRolesByTitle(self, search_term):
        data = self.database_manager.get_roles_search(search_term)

        table.load(headers, self.roles.tableView, data)

    def searchData(self):
        search_term = self.roles.searchEdit.toPlainText()

        if search_term:
            self.loadRolesByTitle(search_term)
        else:
            self.loadRoles()

    def createRole(self):
        title = self.roles.titleEdit.toPlainText()
        desc = self.roles.descEdit.toPlainText()

        if not title or not desc:
            dialog.show('Поля не заполнены.')

            return False
        
        self.database_manager.create_role(title, desc)

        self.loadRoles()

        self.roles.titleEdit.clear()
        self.roles.descEdit.clear()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.roles.tableView)

        delete_action = menu.addAction('Удалить')
        role_edit_action = menu.addAction('Редактировать')

        index = self.roles.tableView.indexAt(position)

        if index.isValid():
            model = self.roles.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                role_id = int(id_item.text())
                action = menu.exec(self.roles.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                    self.database_manager.delete_role(role_id)
                    self.loadRoles()
                
                if action == role_edit_action:
                    self.update_role_functions = update_role_functions(self.main_window, self.widgets, self.database_manager, role_id)

                    self.update_role_functions.openUpdateRole()