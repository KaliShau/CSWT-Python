from src.screens.dialog import Ui_Dialog

class dialog():
    def show(text):
        dialog = Ui_Dialog()
        dialog.textLabel.setText(text)
        dialog.show()
        dialog.exec()