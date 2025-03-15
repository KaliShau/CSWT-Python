from src.screens.my_ticket_edit import Ui_MyTicketEdit

from src.functions.load_table import table

from src.functions.dialog import dialog

from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

headers = ['ID', 'Дата добавления', 'Текст', 'Имя создателя', 'Фамилия создателя']

class my_ticket_edit_functions():
    def __init__(self, main_window, widgets, database_manager, user, ticket_id):

        # init
        self.my_ticket_edit = Ui_MyTicketEdit()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user
        self.ticket_id = ticket_id

        self.loadComment()
        self.loadTicket()

        # buttons
        self.my_ticket_edit.createCommentButton.clicked.connect(self.createComment)
        self.my_ticket_edit.updateTicketButton.clicked.connect(self.updateTicket)

        # config 
        self.my_ticket_edit.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.my_ticket_edit.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openMyTicketEdit(self):
         self.widgets.change(self.my_ticket_edit)

    def loadComment(self):
        data = self.database_manager.get_comments_by_ticket(self.ticket_id)

        table.load(headers, self.my_ticket_edit.tableView, data)

    def loadTicket(self):
        ticket = self.database_manager.get_ticket_by_id(self.ticket_id)

        self.my_ticket_edit.titleEditForTicket.setPlainText(ticket[3])
        self.my_ticket_edit.descEdit.setPlainText(ticket[4])

    def createComment(self):
        text = self.my_ticket_edit.titleEditForComments.toPlainText()

        self.database_manager.create_comment(text, self.ticket_id, self.user[0])
        self.loadComment()

        self.my_ticket_edit.titleEditForComments.clear()

    def updateTicket(self):
        title = self.my_ticket_edit.titleEditForTicket.toPlainText()
        desc = self.my_ticket_edit.descEdit.toPlainText()

        self.database_manager.update_ticket_client(title, desc, self.ticket_id)

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.my_ticket_edit.tableView)

        delete_action = menu.addAction('Удалить')

        index = self.my_ticket_edit.tableView.indexAt(position)

        if index.isValid():
            model = self.my_ticket_edit.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                comment_id = int(id_item.text())
                action = menu.exec(self.my_ticket_edit.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                    comment = self.database_manager.get_comment_by_id(comment_id)

                    if comment[5] != self.user[0]:
                        dialog.show('Комментарий не пренадлежит вам.')

                        return False

                    self.database_manager.delete_comment(comment_id, self.user[0])
                    self.loadComment()
                
