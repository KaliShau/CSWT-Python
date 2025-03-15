from src.screens.create_ticket import Ui_CreateTicket

class create_ticket_functions():
    def __init__(self, main_window, widgets, database_manager, user):

        # init
        self.create_ticket = Ui_CreateTicket()
        self.main_window = main_window
        self.widgets = widgets
        self.user = user
        self.database_manager = database_manager

        # buttons
        self.main_window.createTicketButton.clicked.connect(self.openCreateTicket)
        self.create_ticket.addButton.clicked.connect(self.createTicket)

    def openCreateTicket(self):
        self.widgets.change(self.create_ticket)
        self.getPriorities()

    def getPriorities(self):
        self.create_ticket.priorityComboBox.clear()

        priorities = self.database_manager.get_priorities()
        priority_names = [item[3] for item in priorities]

        self.create_ticket.priorityComboBox.addItems(priority_names)
        
    def createTicket(self):
        title = self.create_ticket.titleEdit.toPlainText()
        desc = self.create_ticket.descEdit.toPlainText()

        priority = self.database_manager.get_priority_by_name(self.create_ticket.priorityComboBox.currentText())
        status = self.database_manager.get_status_by_name('Новая')

        self.database_manager.create_ticket(title, desc, self.user[0], priority[0], status[0])

        self.create_ticket.titleEdit.clear()
        self.create_ticket.descEdit.clear()

