
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
from FilesNumberHandler import Files_Number_Handler
from GUI_FastaViewer import *
sys.path.append(os.getcwd() + '/../controller')
from filehandler import FileHandler as fh  # noqa E402
sys.path.append(os.getcwd() + '/../model')
from tableDataFrame import TableDataFrame as Tdf  # noqa E402



class Welcome_Tab_Logic:


    def Load_ExperimentalData(self):
        """load .tsv and .fasta files (part-automatically)"""



        ExperimentalData_Folder_Path = QFileDialog.getExistingDirectory(self, "Select Directory")
        fasta_files, tsv_files, mzML_files, idXML_files, ini_files = Files_Number_Handler.Identify_Files_Numbers(ExperimentalData_Folder_Path)
        Working_directory = ExperimentalData_Folder_Path



        if Files_Number_Handler.Check_If_Less_Than_One(fasta_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no fasta files in your selected folder. Please chose a fasta file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()
            Welcome_Tab_Logic.Select_Fasta_File(self)


        if Files_Number_Handler.Check_If_Less_Than_One(tsv_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no tsv files in your selected folder. Please try again with a different folder")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()
            Welcome_Tab_Logic.Select_Tsv_File(self)

        if Files_Number_Handler.Check_If_Less_Than_One(ini_files):
            run = 'ProteomicsLFQ -write_ini Config.ini'
            os.chdir(Working_directory)
            os.system(run)
            Files_Number_Handler.Dictionary_Change_File('ini_path', Working_directory + '/Config.ini')
            Files_Number_Handler.Dictionary_Change_Boolean('ini_path')
            iniLoaded = Files_Number_Handler.Dictionary_Return_Boolean('ini_path')
            ini = Files_Number_Handler.Dictionary_Return_Value('ini_path')



        if Files_Number_Handler.Check_If_More_Than_One(fasta_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many fasta files to automatically load them. Please select exactly one.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            Welcome_Tab_Logic.Select_Fasta_File(self)

        if Files_Number_Handler.Check_If_One(fasta_files):
            Files_Number_Handler.Dictionary_Change_File('fasta', Working_directory+'/'+fasta_files[0])
            Files_Number_Handler.Dictionary_Change_Boolean('fasta')


        if Files_Number_Handler.Check_If_More_Than_One(tsv_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many tsv files to automatically load them. Please select exactly one.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            Welcome_Tab_Logic.Select_Tsv_File(self)

        if Files_Number_Handler.Check_If_One(tsv_files):
            Files_Number_Handler.Dictionary_Change_File('tsv', Working_directory+'/'+tsv_files[0])
            Files_Number_Handler.Dictionary_Change_Boolean('tsv')


        if  Files_Number_Handler.Check_If_More_Than_One(ini_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many ini files to automatically load them. Please select exactly one.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            Welcome_Tab_Logic.Select_ini_File(self)

        if Files_Number_Handler.Check_If_One(ini_files):
            Files_Number_Handler.Dictionary_Change_File('ini_path', Working_directory+'/'+ini_files[0])
            Files_Number_Handler.Dictionary_Change_Boolean('ini_path')

        return   Working_directory, mzML_files, idXML_files


    #this method is to load the idXML,mzML and Folder path for the manualy option

    def Load_ExperimentalData_Manualy(self):
        ExperimentalData_Folder_Path = QFileDialog.getExistingDirectory(self, "Select Directory")
        idXML_files,mzML_files = Files_Number_Handler.Identify_Files_Numbers_Manualy(ExperimentalData_Folder_Path)
        Working_directory = ExperimentalData_Folder_Path
        return idXML_files,mzML_files,Working_directory


    def Run_ProteomicsLFQ(self,Working_directory, mzML, idXML, fasta, tsv, ini, output_name, threads, fdr): # runs with ini file

        os.chdir(Working_directory)
        LFQ_command = "ProteomicsLFQ -in "
        for i in mzML:
            LFQ_command += str(i) +""" """

        LFQ_command += "-ids "
        for i in idXML:
            LFQ_command += str(i)+" "

        LFQ_command += "    -design " + tsv + "    -fasta " + fasta
        LFQ_command += " -ini " + ini
        LFQ_command += " -out_cxml " + output_name + ".consensusXML.tmp -out_msstats " + output_name + ".csv.tmp -out " + output_name + ".mzTab.tmp -threads " + threads + " -proteinFDR " + fdr
        os.system(LFQ_command)
        mzTab_file = 'BSA.mzTab.tmp'
        return mzTab_file






    def file_path_mzTab():
        try:
            # generic path to just created mzTab

            path_to_mzTab = os.getcwd()[2:]
            open(path_to_mzTab + r"\BSA.mzTab.tmp")
            path = path_to_mzTab + r"\BSA.mzTab.tmp"
            return path
        except:
            return "error"


    def Select_Fasta_File(self):

        Fasta_File =  QFileDialog.getOpenFileName()
        Fasta_File_Path = Fasta_File[0]

        if Fasta_File_Path.endswith(".fasta"):

            Files_Number_Handler.Dictionary_Change_File('fasta', Fasta_File_Path)
            Files_Number_Handler.Dictionary_Change_Boolean('fasta')

        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected wrong File, File must be fasta file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()






    def Select_Tsv_File(self):

        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]

        if ExperimentalData_File_Path.endswith(".tsv"):
            Files_Number_Handler.Dictionary_Change_File('tsv', ExperimentalData_File_Path)

            Files_Number_Handler.Dictionary_Change_Boolean('tsv')
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected worng File, File must be tsv file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()

    def Select_ini_File(self):
        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]

        if ExperimentalData_File_Path.endswith(".ini"):

            Files_Number_Handler.Dictionary_Change_File('ini_path', ExperimentalData_File_Path)
            Files_Number_Handler.Dictionary_Change_Boolean('ini_path')
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected worng File, File must be ini file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()
