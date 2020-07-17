
import sys
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
from FilesNumberHandler import Files_Number_Handler
from GUI_FastaViewer import *



class Welcome_Tab_Logic:

    def Load_ExperimentalData(self):
        """load .tsv and .fasta files (part-automatically)"""

        #TODO: mabye have to make the arrays global var to be able to use them
        #for further iplementation
        #the file that the user chose is always going to be on the index 0 in
        #its correspinding array
        fasta_files = []
        tsv_files = []

        # declaration before setting those values
        self.fasta_path = ''
        self.tsv_path = ''

        ExperimentalData_Folder_Path = QFileDialog.getExistingDirectory(self, "Select Directory")
        fasta_files, tsv_files = Files_Number_Handler.Identify_Files_Numbers(ExperimentalData_Folder_Path)

        if Files_Number_Handler.Check_If_Less_Than_One(fasta_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no fasta files in your selected folder. Please try again with a different folder")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()

        if Files_Number_Handler.Check_If_Less_Than_One(tsv_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no tsv files in your selected folder. Please try again with a different folder")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()

        if Files_Number_Handler.Check_If_More_Than_One(fasta_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many fasta files to automatically load them. Please select exactly one.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            self.Select_Fasta_File()
        else:
            self.fasta_path = fasta_files[0]

        if Files_Number_Handler.Check_If_More_Than_One(tsv_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many tsv files to automatically load them. Please select exactly one.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            self.Select_Tsv_File()
        else:
            self.tsv_path = tsv_files[0]

        # TODO: make experimental data visible in fasta and experimental viewer 

        return ExperimentalData_Folder_Path + '/' + self.fasta_path, ExperimentalData_Folder_Path + '/' + self.tsv_path




    def Run_ProteomicsLFQ(self):
        #TODO: run the ProteomicsLFQ_command
        #print("Running ProteomicsLFQ_command worked")
    #opens QFileDialog and user must select file if file wrong type display
    #error message
        pass


    def Select_Fasta_File(self):
        #TODO make it recursive so if the User selects the wrong file it
        #shows the error message and open Select_Fasta_File again until the
        #user makes the right choice
        #PROBLEM if user presses Cancel it still stays in recursion
        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]

        if ExperimentalData_File_Path.endswith(".fasta"):
            self.fasta_path = ExperimentalData_File_Path
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected wrong File, File must be fasta file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()




    def Select_Tsv_File(self):
        #TODO make it recursive so if the User selects the wrong file it
        #shows the error message and open Select_Tsv_File again until the 
        #user makes the right choice
        #PROBLEM if user presses Cancel it still stays in recursion
        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]

        if ExperimentalData_File_Path.endswith(".tsv"):
            self.tsv_path = ExperimentalData_File_Path
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected worng File, File must be tsv file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()







