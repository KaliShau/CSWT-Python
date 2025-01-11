from src.screens.my_create_tickets import Ui_MyCreateTickets

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMenu
from PyQt6.QtCore import QPoint, Qt

from src.functions.load_table import table

headers = ['ID', 'Дата добавления', 'Загаловок', 'Описание', 'Решение', 'Дата закрытия', 'Приоритет', 'Статус', 'Имя исполнителя', 'Фамилия исполнителя']

class my_create_tickets_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.my_create_tickets = Ui_MyCreateTickets()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user

        # buttons
        self.main_window.myCreateTicketsButton.clicked.connect(self.openMyCreateTickets)
        self.my_create_tickets.searchButton.clicked.connect(self.searchData)

        # config --
        self.my_create_tickets.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.my_create_tickets.tableView.customContextMenuRequested.connect(self.showContextMenu)

    def openMyCreateTickets(self):
         self.widgets.change(self.my_create_tickets)

         self.loadTickets()

    def loadTickets(self):
        data = self.database_manager.get_my_create_tickets(self.user[0])

        table.load(headers, self.my_create_tickets.tableView, data)
        self.my_create_tickets.tableView.setColumnWidth(3, 150)
        self.my_create_tickets.tableView.setColumnWidth(2, 150)
        self.my_create_tickets.tableView.setColumnWidth(4, 150)

    def loadTicketsByTitle(self, title):
        data = self.database_manager.get_my_create_tickets_by_title(self.user[0], title)

        table.load(headers, self.my_create_tickets.tableView, data)
        self.my_create_tickets.tableView.setColumnWidth(3, 150)
        self.my_create_tickets.tableView.setColumnWidth(2, 150)
        self.my_create_tickets.tableView.setColumnWidth(4, 150)

    def searchData(self):
        title = self.my_create_tickets.searchEdit.toPlainText()

        if title:
            self.loadTicketsByTitle(title)
        else:
            self.loadTickets()

    def showContextMenu(self, position: QPoint): # --
        menu = QMenu(self.my_create_tickets.tableView)

        delete_action = menu.addAction('Удалить')

        index = self.my_create_tickets.tableView.indexAt(position)

        if index.isValid():
            model = self.my_create_tickets.tableView.model()
            row = index.row()
            id_item = model.item(row, 0)

            if id_item:
                ticket_id = int(id_item.text())
                action = menu.exec(self.my_create_tickets.tableView.viewport().mapToGlobal(position))

                if action == delete_action:
                    status = self.database_manager.get_status_by_name('Удалено клиентом')

                    self.database_manager.delete_ticket_by_client(status[0], self.user[0], ticket_id)
                    self.loadTickets()



        
