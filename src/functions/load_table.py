from PyQt6.QtGui import QStandardItemModel, QStandardItem

class table():
    def load(headers, table, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)

        if data:
            for row_number, rov_data in enumerate(data):
                for col_number, cell_data in enumerate(rov_data):
                    item = QStandardItem(str(cell_data))
                    model.setItem(row_number, col_number, item)

        table.setModel(model)
        table.resizeColumnsToContents()