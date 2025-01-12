from src.screens.my_assigned_tickets import Ui_MyAssignedTickets

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

    def openMyAssignedTickets(self):
         self.widgets.change(self.my_assigned_tickets)


    # def loadTickets(self):
    #     status = self.database_manager.get_status_by_name('Новая')
    #     data = self.database_manager.get_available_tickets(status[0])

    #     table.load(headers, self.available_tickets.tableView, data)
    #     self.available_tickets.tableView.setColumnWidth(3, 150)
    #     self.available_tickets.tableView.setColumnWidth(2, 150)

    # def loadTicketsByTitle(self, title):
    #     status = self.database_manager.get_status_by_name('Новая')
    #     data = self.database_manager.get_available_tickets_by_title(status[0], title)

    #     table.load(headers, self.available_tickets.tableView, data)
    #     self.available_tickets.tableView.setColumnWidth(3, 150)
    #     self.available_tickets.tableView.setColumnWidth(2, 150)

    # def searchData(self):
    #     title = self.available_tickets.searchEdit.toPlainText()

    #     if title:
    #         self.loadTicketsByTitle(title)
    #     else:
    #         self.loadTickets()