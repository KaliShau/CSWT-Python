from src.screens.update_department import Ui_UpdateDepartment

from src.functions.dialog import dialog
from src.functions.load_table import table

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

class update_department_functions():
    def __init__(self, main_window, widgets, database_manager, department_id):

        # init
        self.update_department = Ui_UpdateDepartment()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.department_id = department_id

        # buttons
        self.update_department.updateTicketButton.clicked.connect(self.updateDepartment)

    def openUpdateDepartment(self):
        self.widgets.change(self.update_department)

        self.loadDepartment()

    def loadDepartment(self):
        department = self.database_manager.get_department_by_id(self.department_id)

        self.update_department.titleEdit.setPlainText(department[3])
        self.update_department.descEdit.setPlainText(department[4])

    
    def updateDepartment(self):
        title = self.update_department.titleEdit.toPlainText()
        desc = self.update_department.descEdit.toPlainText()

        if not title or not desc:
            dialog.show('Заполните поля.')

            return False
        
        self.database_manager.update_department(title, desc, self.department_id)