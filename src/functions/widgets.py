class widgets():
    def __init__(self, main_window):

        # init
        self.main_window = main_window

    def change(self, widget):
        layout = self.main_window.navigationLayout.layout()
        layout.itemAt(0).widget().setParent(None)
        layout.addWidget(widget)