from src.screens.main_window import Ui_MainWindow

class widgets():
    def __init__(self, main_window: Ui_MainWindow, sign_in, sign_up, create_ticket, my_create_tickets, my_assigned_tickets, available_tickets, db_config):

        # widgets
        self.main_window = main_window
        self.sign_in = sign_in
        self.sign_up = sign_up
        self.create_ticket = create_ticket
        self.my_create_tickets = my_create_tickets
        self.my_assigned_tickets = my_assigned_tickets
        self.available_tickets = available_tickets
        self.db_config = db_config

        # connect buttons
        self.main_window.signInButton.clicked.connect(self.openSignIn)
        self.main_window.signUpButton.clicked.connect(self.openSignUp)
        self.main_window.createTicketButton.clicked.connect(self.openCreateTicket)
        self.main_window.myTicketsButton.clicked.connect(self.openMyCreateTickets)
        self.main_window.myAssignedTicketsButton.clicked.connect(self.openMyAssignedTickets)
        self.main_window.availableTicketsButton.clicked.connect(self.openAvailableTickets)
        self.main_window.action.triggered.connect(self.openDbConfig)
        

    def change(self, widget):
        layout = self.main_window.navigationLayout.layout()
        layout.itemAt(0).widget().setParent(None)
        layout.addWidget(widget)

    def openSignIn(self):
        self.change(self.sign_in)

    def openSignUp(self):
        self.change(self.sign_up)

    def openCreateTicket(self):
        self.change(self.create_ticket)

    def openMyCreateTickets(self):
        self.change(self.my_create_tickets)

    def openMyAssignedTickets(self):
        self.change(self.my_assigned_tickets)

    def openAvailableTickets(self):
        self.change(self.available_tickets)

    def openDbConfig(self):
        self.change(self.db_config)


