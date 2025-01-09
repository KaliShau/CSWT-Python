from src.screens.available_tickets import Ui_AvailableTickets

class available_tickets_functions():
    def __init__(self, main_window, widgets):

        # init
        self.available_tickets = Ui_AvailableTickets()
        self.main_window = main_window
        self.widgets = widgets

        # buttons
        self.main_window.availableTicketsButton.clicked.connect(self.openAvailableTickets)

    def openAvailableTickets(self):
         self.widgets.change(self.available_tickets)

