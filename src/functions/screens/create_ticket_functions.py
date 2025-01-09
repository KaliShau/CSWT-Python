from src.screens.create_ticket import Ui_CreateTicket

class create_ticket_functions():
    def __init__(self, main_window, widgets, user):

        # init
        self.create_ticket = Ui_CreateTicket()
        self.main_window = main_window
        self.widgets = widgets
        self.user = user

        # buttons
        self.main_window.createTicketButton.clicked.connect(self.openCreateTicket)
        self.create_ticket.addButton.clicked.connect(self.ddd)

    def openCreateTicket(self):
         self.widgets.change(self.create_ticket)

    def ddd(self):
        print(self.user)