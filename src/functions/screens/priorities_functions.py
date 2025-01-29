from src.screens.priorities import Ui_Priorities

from src.functions.load_table import table
from src.functions.dialog import dialog

# from src.functions.screens.update_role_functions  import update_role_functions

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

headers = ['ID', 'Дата создания', 'Дата обновления', 'Название', 'Описание']

class priorities_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.priorities = Ui_Priorities()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.prioritiesButton.clicked.connect(self.openPriorities)
        self.priorities.searchButton.clicked.connect(self.searchData)
        self.priorities.createButton.clicked.connect(self.createPriority)

        # config 
        self.priorities.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.priorities.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openPriorities(self):
        self.widgets.change(self.priorities)

        self.loadPriorities()

    def loadPriorities(self):
        data = self.database_manager.get_priorities()

        table.load(headers, self.priorities.tableView, data)


    def loadPrioritiesByTitle(self, search_term):
        data = self.database_manager.get_priorities_search(search_term)

        table.load(headers, self.priorities.tableView, data)

    def searchData(self):
        search_term = self.priorities.searchEdit.toPlainText()

        if search_term:
            self.loadPrioritiesByTitle(search_term)
        else:
            self.loadPriorities()

    def createPriority(self):
        title = self.priorities.titleEdit.toPlainText()
        desc = self.priorities.descEdit.toPlainText()

        if not title or not desc:
            dialog.show('Поля не заполнены.')

            return False
        
        self.database_manager.create_priority(title, desc)

        self.loadPriorities()

        self.priorities.titleEdit.clear()
        self.priorities.descEdit.clear()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.priorities.tableView)

        delete_action = menu.addAction('Удалить')
        priority_edit_action = menu.addAction('Редактировать')

        index = self.priorities.tableView.indexAt(position)

        if index.isValid():
            model = self.priorities.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                priority_id = int(id_item.text())
                action = menu.exec(self.priorities.tableView.viewport().mapToGlobal(position))

                # if action == delete_action:
                #     self.database_manager.delete_role(role_id)
                #     self.loadRoles()
                
                # if action == role_edit_action:
                #     self.update_role_functions = update_role_functions(self.main_window, self.widgets, self.database_manager, role_id)

                #     self.update_role_functions.openUpdateRole()