from PyQt5QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class TestTable(QWidget):

    def __init__(self):
        super().__init__()

    def creatTabel(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.serRowCount(3)
        self.tableWidget.setColumnCount(7)

        self.VBoxLayout = QVBoxLayout()
        self.VBoxLayout.add(self.tableWidget)
        self.setLayout(self.VBoxLayout)
