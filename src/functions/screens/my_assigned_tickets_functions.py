from src.screens.my_assigned_tickets import Ui_MyAssignedTickets

class my_assigned_tickets_functions():
    def __init__(self, main_window, widgets):

        # init
        self.my_assigned_tickets = Ui_MyAssignedTickets()
        self.main_window = main_window
        self.widgets = widgets

        # buttons
        self.main_window.myAssignedTicketsButton.clicked.connect(self.openMyAssignedTickets)

    def openMyAssignedTickets(self):
         self.widgets.change(self.my_assigned_tickets)

