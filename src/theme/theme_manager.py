class theme_manager:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(theme_manager, self).__new__(self)
            
            self._instance.current_theme = 'light'

            self._instance.styles = {
                "light": """
                    QMainWindow {
                        background-color: #c7c7c7;
                        color: #e7e7e5;
                    }

                    QWidget {
                        background-color: #c9c9c9;
                    }

                    #navBar {
                        background-color: #c9c9c9;
                    }

                    QLabel {
                        color: #4a494a;
                    }

                    #centralwidget {
                        background-color: #c9c9c9;
                        color: #4a494a
                    }

                    #startWidgetLayout {
                        background-color: #c9c9c9;
                        color: #4a494a
                    }

                    #menubar {
                        background-color: #c9c9c9;
                        color: #4a494a
                    }

                    QCommandLinkButton {
                        color: #4a494a
                    }

                    QCommandLinkButton:hover {
                        background-color: #dc5049;
                    }

                    QPushButton {
                        color: #4a494a
                    }

                    QPushButton:hover {
                        background-color: #dc5049;
                    }

                    QMenu {
                        color: #4a494a;
                    }

                    QGroupBox {
                        color: #111;
                    }
                """,
                "dark": """
                    QMainWindow {
                        background-color: #1a1a1a;
                        color: #e7e7e5;
                    }

                    QLabel {
                        color: #e7e7e5;
                    }

                    #centralwidget {
                        background-color: #1a1a1a;
                        color: #e7e7e5
                    }

                    #startWidgetLayout {
                        background-color: #1a1a1a;
                        color: #e7e7e5
                    }

                    #menubar {
                        background-color: #1a1a1a;
                        color: #e7e7e5
                    }

                    QWidget {
                        background-color: #202122;
                    }

                    QCommandLinkButton {
                        color: #e7e7e5
                    }

                    QCommandLinkButton:hover {
                        background-color: #dc5049;
                    }

                    QPushButton {
                        color: #e7e7e5
                    }

                    QPushButton:hover {
                        background-color: #dc5049;
                    }

                    QMenu {
                        color: #e7e7e5;
                    }

                    QGroupBox {
                        color: #e7e7e5;
                    }
                """
            }

            return self._instance

    def set_theme(self, theme, widget):
        if theme in self.styles:
            widget.setStyleSheet(self.styles[theme])
            self.current_theme = theme

    def toggle_theme(self, widget):
        new_theme = 'dark' if self.current_theme == 'light' else 'light'
        self.set_theme(new_theme, widget)