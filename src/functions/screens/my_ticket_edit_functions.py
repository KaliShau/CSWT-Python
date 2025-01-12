from src.screens.my_ticket_edit import Ui_MyTicketEdit

from src.functions.load_table import table

from src.functions.dialog import dialog

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
