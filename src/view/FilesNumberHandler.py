import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow,
                             QAction, qApp,
                             QHBoxLayout, QVBoxLayout, QMessageBox,
                             QLineEdit, QTableWidget, QTableWidgetItem,
                             QGridLayout, QPlainTextEdit,
                             QDesktopWidget, QLabel, QRadioButton,
                             QGroupBox, QSizePolicy, QCheckBox, QFileDialog,
                             QTextEdit, QTextBrowser)
from PyQt5.QtGui import QFont, QColor

class Files_Number_Handler():
    #gets a folder path as an argument and searches for files that end with
    #.fasta or .tsv and saves them in the corresponding Array
    def Identify_Files_Numbers(folder_path):
        fasta_files=[]
        tsv_files = []
        fileslist = os.listdir(folder_path)
        for file in fileslist:
            if file.endswith(".fasta"):
                fasta_files.append(file)

            if file.endswith(".tsv"):
                tsv_files.append(file)
        return fasta_files,tsv_files
    #checks if array contains only on element, it is important because if
    #more than 1 user needs to select the on file he wants to use
    def Check_If_More_Than_One(arraytotest):
        if len(arraytotest)>1:
            return True
        else :
            return False

    def Check_If_Less_Than_One(arraytotest):
        if len(arraytotest)==0:
            return True
        else :
            return False
