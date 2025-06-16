from .my_assigned_tickets import Ui_MyAssignedTickets

from src.shared.utils.load_table import table

from src.pages.my_ticket_edit.my_ticket_edit_functions import my_ticket_edit_functions
from src.pages.update_ticket.update_ticket_functions import update_ticket_functions

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import QMenu

headers = ['ID', 'Дата добавления', 'Загаловок', 'Описание', 'Решение', 'Дата завершения', 'Приоритет', 'Статус', 'Имя создателя', 'Фамилия создателя']

class my_assigned_tickets_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.my_assigned_tickets = Ui_MyAssignedTickets()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.myAssignedTicketsButton.clicked.connect(self.openMyAssignedTickets)
        self.my_assigned_tickets.searchButton.clicked.connect(self.searchData)

        # config 
        self.my_assigned_tickets.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.my_assigned_tickets.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openMyAssignedTickets(self):
         self.widgets.change(self.my_assigned_tickets)

         self.loadTickets()

    def loadTickets(self):
        data = self.database_manager.get_my_assigned_tickets(self.user[0])

        table.load(headers, self.my_assigned_tickets.tableView, data)
        self.my_assigned_tickets.tableView.setColumnWidth(3, 150)
        self.my_assigned_tickets.tableView.setColumnWidth(2, 150)
        self.my_assigned_tickets.tableView.setColumnWidth(4, 150)

    def loadTicketsByTitle(self, title):
        data = self.database_manager.get_my_assigned_tickets_by_title(self.user[0], title)

        table.load(headers, self.my_assigned_tickets.tableView, data)
        self.my_assigned_tickets.tableView.setColumnWidth(3, 150)
        self.my_assigned_tickets.tableView.setColumnWidth(2, 150)
        self.my_assigned_tickets.tableView.setColumnWidth(4, 150)

    def searchData(self):
        title = self.my_assigned_tickets.searchEdit.toPlainText()

        if title:
            self.loadTicketsByTitle(title)
        else:
            self.loadTickets()
    

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.my_assigned_tickets.tableView)

        comments_action = menu.addAction('Комментарии')
        edit_action = menu.addAction('Редактировать')

        index = self.my_assigned_tickets.tableView.indexAt(position)

        if index.isValid():
            model = self.my_assigned_tickets.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                ticket_id = int(id_item.text())
                action = menu.exec(self.my_assigned_tickets.tableView.viewport().mapToGlobal(position))
                
                if action == comments_action:
                    self.my_ticket_edit_functions = my_ticket_edit_functions(self.main_window, self.widgets, self.database_manager, self.user, ticket_id)
                    self.my_ticket_edit_functions.my_ticket_edit.updateTicketButton.setVisible(False)
                    self.my_ticket_edit_functions.my_ticket_edit.titleEditForTicket.setReadOnly(True)
                    self.my_ticket_edit_functions.my_ticket_edit.descEdit.setReadOnly(True)

                    self.my_ticket_edit_functions.openMyTicketEdit()
                
                if action == edit_action:
                    self.update_ticket_functions = update_ticket_functions(self.main_window, self.widgets, self.database_manager, self.user, ticket_id)

                    self.update_ticket_functions.openUpdateTicket()