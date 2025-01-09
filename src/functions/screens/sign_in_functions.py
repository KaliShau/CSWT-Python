from src.screens.sign_in import Ui_SignIn

class sign_in_functions():
    def __init__(self, main_window, widgets):

        # init
        self.sign_in = Ui_SignIn()
        self.main_window = main_window
        self.widgets = widgets

        # buttons
        self.main_window.signInButton.clicked.connect(self.openSignIn)

    def openSignIn(self):
         self.widgets.change(self.sign_in)

