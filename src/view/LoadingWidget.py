# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow,
                             QAction, qApp,
                             QHBoxLayout, QVBoxLayout, QMessageBox,
                             QLineEdit, QTableWidget, QTableWidgetItem,
                             QGridLayout, QScrollArea, QPlainTextEdit,
                             QDesktopWidget, QLabel, QRadioButton,
                             QGroupBox, QSizePolicy, QCheckBox, QFileDialog,
                             QTextEdit, QTextBrowser, QProgressBar)


class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "loading"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 200

        self.vBox = QVBoxLayout()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        #progress bar
        #self.progressBar = QProgressBar()
        #self.progressBar.setValue(0)
        #self.vBox.addWidget(self.progressBar)

        self.datalabel = QLabel()
        self.datalabel.setText("Loading...")

        #self.vBox.addWidget(self.datalabel)

        self.setLayout(self.vBox)
        self.show()
