from src.screens.my_create_tickets import Ui_MyCreateTickets

class my_create_tickets_functions():
    def __init__(self, main_window, widgets):

        # init
        self.my_create_tickets = Ui_MyCreateTickets()
        self.main_window = main_window
        self.widgets = widgets

        # buttons
        self.main_window.myCreateTicketsButton.clicked.connect(self.openMyCreateTickets)

    def openMyCreateTickets(self):
         self.widgets.change(self.my_create_tickets)

