from src.screens.update_ticket import Ui_UpdateTicket

from src.functions.dialog import dialog


class update_ticket_functions():
    def __init__(self, main_window, widgets, database_manager, user, ticket_id):

        # init
        self.update_ticket = Ui_UpdateTicket()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager
        self.user = user
        self.ticket_id = ticket_id

        self.loadTicket()

        # buttons
        self.update_ticket.updateTicketButton.clicked.connect(self.updateTicket)

    def openUpdateTicket(self):
         self.widgets.change(self.update_ticket)

    def loadTicket(self):
        ticket = self.database_manager.get_ticket_by_id(self.ticket_id)

        self.update_ticket.titleEditForTicket.setPlainText(ticket[3])
        self.update_ticket.descEdit.setPlainText(ticket[4])
        self.update_ticket.solutionEdit.setPlainText(ticket[5])

        self.currentPriority(ticket)
        self.currentStatus(ticket)

    def currentPriority(self, ticket):
        priorities = self.database_manager.get_priorities()
        priority_names = [item[3] for item in priorities]

        self.update_ticket.priorityComboBox.addItems(priority_names)

        current_priority = self.database_manager.get_priority_by_id(ticket[8])
        current_priority_name = current_priority[3]

        index = priority_names.index(current_priority_name) if current_priority_name in priority_names else -1

        if index != -1:
            self.update_ticket.priorityComboBox.setCurrentIndex(index)

    def currentStatus(self, ticket):
        statuses = self.database_manager.get_statuses()
        statuses_names = [item[3] for item in statuses]

        self.update_ticket.statusComboBox.addItems(statuses_names)

        current_status = self.database_manager.get_status_by_id(ticket[9])
        current_status_name = current_status[3]

        index = statuses_names.index(current_status_name) if current_status_name in statuses_names else -1

        if index != -1:
            self.update_ticket.statusComboBox.setCurrentIndex(index)

    def updateTicket(self):
        title = self.update_ticket.titleEditForTicket.toPlainText()
        desc = self.update_ticket.descEdit.toPlainText()
        solution = self.update_ticket.solutionEdit.toPlainText()
        priority = self.database_manager.get_priority_by_name(self.update_ticket.priorityComboBox.currentText())
        status = self.database_manager.get_status_by_name(self.update_ticket.statusComboBox.currentText())

        if self.update_ticket.statusComboBox.currentText() == 'Решена':
            ticket = self.database_manager.get_ticket_by_id(self.ticket_id)
            status_ticket = self.database_manager.get_status_by_id(ticket[9])

            if status_ticket[3] != self.update_ticket.statusComboBox.currentText(): 
                self.database_manager.closed_at_ticket(self.ticket_id)
                

        self.database_manager.update_ticket(title, desc, solution, priority[0], status[0], self.ticket_id)
