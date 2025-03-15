from src.screens.departments import Ui_Departments

from src.functions.load_table import table
from src.functions.dialog import dialog

from src.functions.screens.update_department_functions  import update_department_functions

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

headers = ['ID', 'Дата создания', 'Дата обновления', 'Название', 'Описание']

class departments_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.departments = Ui_Departments()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.departamentsButton.clicked.connect(self.openDepartments)
        self.departments.searchButton.clicked.connect(self.searchData)
        self.departments.createButton.clicked.connect(self.createDepartment)

        # config 
        self.departments.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.departments.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openDepartments(self):
        self.widgets.change(self.departments)

        self.loadDepartments()

    def loadDepartments(self):
        data = self.database_manager.get_departments()

        table.load(headers, self.departments.tableView, data)


    def loadDepartmentsByTitle(self, search_term):
        data = self.database_manager.get_departments_search(search_term)

        table.load(headers, self.departments.tableView, data)

    def searchData(self):
        search_term = self.departments.searchEdit.toPlainText()

        if search_term:
            self.loadDepartmentsByTitle(search_term)
        else:
            self.loadDepartments()

    def createDepartment(self):
        title = self.departments.titleEdit.toPlainText()
        desc = self.departments.descEdit.toPlainText()

        if not title or not desc:
            dialog.show('Поля не заполнены.')

            return False
        
        self.database_manager.create_department(title, desc)

        self.loadDepartments()

        self.departments.titleEdit.clear()
        self.departments.descEdit.clear()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.departments.tableView)

        delete_action = menu.addAction('Удалить')
        department_edit_action = menu.addAction('Редактировать')

        index = self.departments.tableView.indexAt(position)

        if index.isValid():
            model = self.departments.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                department_id = int(id_item.text())
                action = menu.exec(self.departments.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                    self.database_manager.delete_department(department_id)
                    self.loadDepartments()
                
                if action == department_edit_action:
                    self.update_department_functions = update_department_functions(self.main_window, self.widgets, self.database_manager, department_id)

                    self.update_department_functions.openUpdateDepartment()