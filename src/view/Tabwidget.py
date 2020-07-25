from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
import os
from LoadingWidget import LoadingWindow
from GUI_FastaViewer import GUI_FastaViewer
from mzTabTableWidget import Window
from GUI_Welcome_Tab import GUI_Welcome_Tab
from Welcome_Tab_Logic import *
from ConfigView import ConfigView
sys.path.insert(0, "../apps")
from XMLViewer import XMLViewer
from TableEditor import TableEditor
from SpecViewer import App
sys.path.append(os.getcwd()+'/../view')
from mzMLTableView import mzMLTableView
from FilesNumberHandler import Files_Number_Handler


import os

# TODO: eventuell im Nachhinein anderer Ordner (oder generisch)
sys.path.insert(0, '../FRACTIONS')
from ProteomicsLFQ_command import ProteomicsLFQ_command
Option_selected = "manualy"
class TabWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle("Protein Analyzer")
        self.tab_widget = AnalyzerTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()


class AnalyzerTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)



        # initialize tabs
        self.TabWidget = QTabWidget()
        self.Tab0 = GUI_Welcome_Tab()
        self.Tab1 = GUI_FastaViewer()
        self.Tab2 = App()
        #self.Tab3 = TableEditor()
        self.Tab3 = mzMLTableView()
        self.Tab4 = ConfigView()
        self.Tab5 = Window()

        # add tabs
        self.TabWidget.addTab(self.Tab0, "Welcome")
        self.TabWidget.addTab(self.Tab1, "Proteinsequence Viewer")
        self.TabWidget.addTab(self.Tab2, "Spectrum Viewer")
        self.TabWidget.addTab(self.Tab3, "Experimental Design")
        self.TabWidget.addTab(self.Tab4, "XML Viewer")
        self.TabWidget.addTab(self.Tab5, "PSM/Protein Viewer")


        # add tabs
        self.layout.addWidget(self.TabWidget)


        # add load Button for ProteomicsLFQ
        self.hboxlayout = QHBoxLayout()
        #putting the button on the right side corner with a Stretch
        #self.hboxlayout.addStretch(0)
        self.Loadlabel = QLabel()
        self.Loadlabel.setText("no data loaded")
        self.hboxlayout.addWidget(self.Loadlabel)

        #self.loadButton = QtWidgets.QPushButton(self)
        #self.loadButton.setText("Load Data")
        #self.loadButton.setFixedWidth(200)
        self.Output_Name = ''
        self.runButton = QtWidgets.QPushButton(self)
        self.runButton.setText("Run ProteomicsLFQ")
        self.runButton.setFixedWidth(200)

        self.hboxlayout.addWidget(self.runButton)
        self.runButton.clicked.connect(self.runProteomicsLFQ)

        #self.hboxlayout.addWidget(self.loadButton)
        self.Tab0.loadButton.clicked.connect(self.clickedLoadData)
        #print(self.Tab0.LineEdit)
        #self.Tab0.RenameButton.clicked.connect(self.get_Output_FileName(self.Tab0.LineEdit)

        self.layout.addLayout(self.hboxlayout)


        self.setLayout(self.layout)

        x = Files_Number_Handler.Dictionary_Return_Value("fasta")
        y = Files_Number_Handler.Dictionary_Return_Value("tsv")
        print(x)
        print(y)



        #creates an user dialog and asks him to choose on option
    def user_Dialog(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Information")
        messagebox.setIcon(QMessageBox.Question)
        messagebox.setText("Please choose on of the following Options")
        messagebox.addButton("automatically", QtWidgets.QMessageBox.YesRole)
        messagebox.addButton("manualy", QtWidgets.QMessageBox.NoRole)
        messagebox.setDetailedText("If you choose automatically than all"+
            "manualy selected Files will be overwritten with the files in "+
            "the folder you select. If you choose manualy than they will be "+
            "used instead")
        messagebox.buttonClicked.connect(self.option_selected)
        messagebox.exec_()

    def option_selected(self,button):
        global Option_selected
        Option_selected = button.text()








    def clickedLoadData(self):
        self.user_Dialog()
        global Option_selected
        print(Option_selected)
        #when new data is loaded all previous loaded data is cleared
        self.Tab5.clearmzTabTable()# new method to clear table
        self.Tab1.clearFastaViewer()# new methode to clear fasta viewer

        self.Tab3.SelectAllBtn()#first seltect all
        self.Tab3.RemoveBtn()#then clear all selected

        self.Tab4.clearConfigView()
        #if user has selected automatically than load everything from Directory
        if Option_selected == "automatically":

            data_path, mzML, idXML = Welcome_Tab_Logic.Load_ExperimentalData(self)
            Files_Number_Handler.Dictionary_Change_File("idXML",idXML)
            Files_Number_Handler.Dictionary_Change_File("mzML",mzML)
            Files_Number_Handler.Dictionary_Change_File("data",data_path)
            self.Tab1.loadFile(Files_Number_Handler.Dictionary_Return_Value('fasta'))
            print(Files_Number_Handler.Dictionary_Return_Value('tsv'))
            self.Tab3.loadExperimentalDesign(Files_Number_Handler.Dictionary_Return_Value('tsv'))
            self.Tab4.generateTreeModel(Files_Number_Handler.Dictionary_Return_Value('ini_path'))
            '''
            if len(fasta_path.split('/')) == 1: # if one fasta file comes from working directory only file name is saved in an array
                self.Tab1.loadFile(data_path+'/'+fasta_path)# for loading working directoy needs to be added for complete path
            else:
                self.Tab1.loadFile(fasta_path)# fasta file comes from other directory or more than one file in working directory , complete path is saved
            if len(tsv_path.split('/')) == 1:
                self.Tab3.loadExperimentalDesign(data_path+'/'+tsv_path)
            else:
                self.Tab3.loadExperimentalDesign(tsv_path)
            if len(ini_path.split('/')) == 1:
                self.Tab4.generateTreeModel(data_path+ '/'+ini_path)
            else:
                self.Tab4.generateTreeModel(ini_path)
                '''
        #If User has selected manualy than take files from dictionary
        if Option_selected == "manualy":
            idXML,mzML,data_path = Welcome_Tab_Logic.Load_ExperimentalData_Manualy(self)
            Files_Number_Handler.Dictionary_Change_File("idXML",idXML)
            Files_Number_Handler.Dictionary_Change_File("mzML",mzML)
            Files_Number_Handler.Dictionary_Change_File("data",data_path)
            #Files_Number_Handler.Dictionary_Change_Boolean("idXML")
            #Files_Number_Handler.Dictionary_Change_Boolean("mzML")
            Files_Number_Handler.Dictionary_Change_Boolean("data")

        self.Loadlabel.setText("data loaded")



    def runProteomicsLFQ(self):
        """launch proteomicsLFQ and add output to PSM/ ProteinViewer Tab"""

        fasta = Files_Number_Handler.Dictionary_Return_Value('fasta')
        tsv = Files_Number_Handler.Dictionary_Return_Value('tsv')
        ini = Files_Number_Handler.Dictionary_Return_Value('ini_path')
        mzML = Files_Number_Handler.Dictionary_Return_Value('mzML')
        idXML = Files_Number_Handler.Dictionary_Return_Value('idXML')
        print(Files_Number_Handler.Dictionary_Return_Value('mzML'),Files_Number_Handler.Dictionary_Return_Value('idXML'))
        data_path = Files_Number_Handler.Dictionary_Return_Value('data')

        fastaLoaded = Files_Number_Handler.Dictionary_Return_Boolean('fasta')
        tsvLoaded = Files_Number_Handler.Dictionary_Return_Boolean('tsv')
        iniLoaded = Files_Number_Handler.Dictionary_Return_Boolean('ini_path')
        mzMLLoaded = Files_Number_Handler.Dictionary_Return_Boolean('mzML')
        idXMLLoaded = Files_Number_Handler.Dictionary_Return_Boolean('idXML')

        # user input for the run 
        self.Tab0.get_Threads(self.Tab0.Threads)
        self.Tab0.get_Output_FileName(self.Tab0.OutputName)
        self.Tab0.get_ProteinFDR(self.Tab0.ProteinFDR)
        #self.Tab0.get_Output_FileName(self.Tab0.OutputName)

        if not fastaLoaded:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("Fasta file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not tsvLoaded:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("tsv file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not mzMLLoaded:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("mzML files are missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not idXMLLoaded:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("idXML files are missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not iniLoaded:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("config file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif self.Tab0.Output_Name == '':
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No name for the output files. Please first add a name for the output files.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
        
        elif self.Tab0.Threads_Number == '':
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No information for Threads was found. Please first insert Threads information. Default is 1.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif self.Tab0.ProteiFDR_Number == '':
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No information for ProteinFDR was found. Please first insert ProteinFDR information. Default is 0.3.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()


        elif fastaLoaded and tsvLoaded and mzMLLoaded and idXMLLoaded and iniLoaded:
            #self.Tab0.get_Threads(self.Tab0.Threads)
            #self.Tab0.get_ProteinFDR(self.Tab0.ProteinFDR)
            #print(self.Tab0.Threads_Number, self.Tab0.ProteiFDR_Number)
            # runs with init

            self.Loadlabel.setText("loading...")


            mzTab_file = Welcome_Tab_Logic.Run_ProteomicsLFQ(Welcome_Tab_Logic, data_path, mzML, idXML, fasta, tsv, ini, self.Tab0.Output_Name, self.Tab0.Threads_Number, self.Tab0.ProteiFDR_Number)
            complete_path = data_path + '/' + mzTab_file
            self.Tab5.readFile(complete_path)
            self.Loadlabel.setText("Job completed")









def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
