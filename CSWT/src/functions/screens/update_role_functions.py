from src.screens.update_role import Ui_UpdateRole

from src.functions.dialog import dialog
from src.functions.load_table import table

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

class update_role_functions():
    def __init__(self, main_window, widgets, database_manager, role_id):

        # init
        self.update_role = Ui_UpdateRole()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.role_id = role_id

        # buttons
        self.update_role.updateTicketButton.clicked.connect(self.updateRole)

    def openUpdateRole(self):
        self.widgets.change(self.update_role)

        self.loadRole()

    def loadRole(self):
        role = self.database_manager.get_role_by_id(self.role_id)

        self.update_role.titleEdit.setPlainText(role[3])
        self.update_role.descEdit.setPlainText(role[4])

    
    def updateRole(self):
        title = self.update_role.titleEdit.toPlainText()
        desc = self.update_role.descEdit.toPlainText()

        if not title or not desc:
            dialog.show('Заполните поля.')

            return False
        
        self.database_manager.update_role(title, desc, self.role_id)