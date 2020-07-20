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


import os

# TODO: eventuell im Nachhinein anderer Ordner (oder generisch)
sys.path.insert(0, '../FRACTIONS')
from ProteomicsLFQ_command import ProteomicsLFQ_command

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

        self.loadButton = QtWidgets.QPushButton(self)
        self.loadButton.setText("Load Data")
        self.loadButton.setFixedWidth(200)

        self.runButton = QtWidgets.QPushButton(self)
        self.runButton.setText("Run ProteomicsLFQ")
        self.runButton.setFixedWidth(200)

        self.hboxlayout.addWidget(self.runButton)
        self.runButton.clicked.connect(self.runProteomicsLFQ)

        self.hboxlayout.addWidget(self.loadButton)
        self.loadButton.clicked.connect(self.clickedLoadData)

        self.layout.addLayout(self.hboxlayout)


        self.setLayout(self.layout)

        self.data_path = ''
        self.mzML_files =[]
        self.idXML_files = []
        self.tsv_path = ''
        self.fasta_path = ''
        self.ini_path = ''

        self.fastaLoaded = 0
        self.tsvLoaded = 0
        self.mzMLLoaded = 0
        self.idXMLLoaded = 0
        self.iniLoaded = 0


    # global load button
    def clickedLoadData(self):
        #when new data is loaded all previous loaded data is cleared
        self.Tab5.clearmzTabTable()# new method to clear table
        self.Tab1.clearFastaViewer()# new methode to clear fasta viewer

        self.Tab3.SelectAllBtn()#first seltect all
        self.Tab3.RemoveBtn()#then clear all selected

        self.Tab4.clearConfigView()

        fasta_path, tsv_path, data_path, mzML, idXML, ini_path, fastaLoaded, tsvLoaded, mzMLLoaded, idXMLLoaded, iniLoaded = Welcome_Tab_Logic.Load_ExperimentalData(self)

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

        self.data_path = data_path
        self.mzML_files = mzML
        self.idXML_files = idXML
        self.fasta_path = fasta_path
        self.tsv_path = tsv_path
        self.ini_path = ini_path

        self.fastaLoaded = fastaLoaded
        self.tsvLoaded = tsvLoaded
        self.mzMLLoaded = mzMLLoaded
        self.idXMLLoaded = idXMLLoaded
        self.iniLoaded = iniLoaded

        self.Loadlabel.setText("data loaded")
        print(mzML)
        print(idXML)



    def runProteomicsLFQ(self):
        """launch proteomicsLFQ and add output to PSM/ ProteinViewer Tab"""
        if not bool(self.fastaLoaded):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("Fasta file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
        elif not bool(self.tsvLoaded):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("tsv file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not bool(self.mzMLLoaded):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("mzML files are missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif not bool(self.idXMLLoaded):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("idXML files are missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()


        elif not bool(self.iniLoaded):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("config file is missing")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()

        elif bool(self.fastaLoaded) and bool(self.tsvLoaded) and bool(self.mzMLLoaded) and bool(self.idXMLLoaded) and bool(self.iniLoaded):
            # runs with init

            self.Loadlabel.setText("loading...")

            mzTab_file = Welcome_Tab_Logic.Run_ProteomicsLFQ(Welcome_Tab_Logic,self.data_path, self.mzML_files, self.idXML_files, self.fasta_path, self.tsv_path, self.ini_path)
            complete_path = self.data_path + '/' + mzTab_file
            self.Tab5.readFile(complete_path)
            self.Loadlabel.setText("Job completed")









def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
