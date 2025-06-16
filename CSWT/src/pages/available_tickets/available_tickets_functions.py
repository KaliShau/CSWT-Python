from .available_tickets import Ui_AvailableTickets

from src.pages.my_ticket_edit.my_ticket_edit_functions import my_ticket_edit_functions

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import QMenu

from src.shared.utils.load_table import table

headers = ['ID', 'Дата добавления', 'Загаловок', 'Описание', 'Приоритет', 'Статус', 'Имя создателя', 'Фамилия создателя']


class available_tickets_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.available_tickets = Ui_AvailableTickets()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.availableTicketsButton.clicked.connect(self.openAvailableTickets)
        self.available_tickets.searchButton.clicked.connect(self.searchData)

        # config 
        self.available_tickets.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.available_tickets.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openAvailableTickets(self):
         self.widgets.change(self.available_tickets)

         self.loadTickets()

    def loadTickets(self):
        status = self.database_manager.get_status_by_name('Новая')
        data = self.database_manager.get_available_tickets(status[0])

        table.load(headers, self.available_tickets.tableView, data)
        self.available_tickets.tableView.setColumnWidth(3, 150)
        self.available_tickets.tableView.setColumnWidth(2, 150)

    def loadTicketsByTitle(self, title):
        status = self.database_manager.get_status_by_name('Новая')
        data = self.database_manager.get_available_tickets_by_title(status[0], title)

        table.load(headers, self.available_tickets.tableView, data)
        self.available_tickets.tableView.setColumnWidth(3, 150)
        self.available_tickets.tableView.setColumnWidth(2, 150)

    def searchData(self):
        title = self.available_tickets.searchEdit.toPlainText()

        if title:
            self.loadTicketsByTitle(title)
        else:
            self.loadTickets()

    def showContextMenu(self, position: QPoint): 
        menu = QMenu(self.available_tickets.tableView)

        accept_action = menu.addAction('Принять заявку')
        comments_action = menu.addAction('Комментарии')

        index = self.available_tickets.tableView.indexAt(position)

        if index.isValid():
            model = self.available_tickets.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                ticket_id = int(id_item.text())
                action = menu.exec(self.available_tickets.tableView.viewport().mapToGlobal(position))

                if action == accept_action:
                    status = self.database_manager.get_status_by_name('Назначена')

                    self.database_manager.update_ticket_by_assigned(self.user[0], ticket_id, status[0])
                    self.loadTickets()
                
                if action == comments_action:
                    self.my_ticket_edit_functions = my_ticket_edit_functions(self.main_window, self.widgets, self.database_manager, self.user, ticket_id)
                    self.my_ticket_edit_functions.my_ticket_edit.updateTicketButton.setVisible(False)
                    self.my_ticket_edit_functions.my_ticket_edit.titleEditForTicket.setReadOnly(True)
                    self.my_ticket_edit_functions.my_ticket_edit.descEdit.setReadOnly(True)

                    self.my_ticket_edit_functions.openMyTicketEdit()