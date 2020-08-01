from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
import os
from GUI_FastaViewer import GUI_FastaViewer
from mzTabTableWidget import Window
from GUI_Welcome_Tab import GUI_Welcome_Tab
from Welcome_Tab_Logic import *
from Tab_SpectrumViewer import Tab_SpectrumViewer
from ConfigView import ConfigView
sys.path.insert(0, "../apps")
from XMLViewer import XMLViewer
from TableEditor import TableEditor
from SpecViewer import App
sys.path.append(os.getcwd()+'/../view')
from mzMLTableView import mzMLTableView
from FilesNumberHandler import Files_Number_Handler





sys.path.insert(0, '../FRACTIONS')
from ProteomicsLFQ_command import ProteomicsLFQ_command
Option_selected = "manualy"
class TabWindow(QMainWindow):
    """
    This class is used to create the window and set the basic attributes of
    the window such as size and title

    Attributes
    ----------
    self : QMainWindow
        The QmainWindow is modified in the _init_ method

    Methods
    -------
    _init_()
        sets the inital attributes of the Window such as title and size
     """

    def __init__(self):
        super().__init__()
        self.resize(1200,720)
        self.setWindowTitle("Protein Analyzer")
        self.tab_widget = AnalyzerTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()


class AnalyzerTabWidget(QWidget):
    """
    This class is used to create the layout, design and also the functionality of
    the window and its buttons and applications

    Attributes
    ----------
    layout : QVBoxLayout
        a vertical layout for the window

    TabWidget : QTabWidget
        a TabWidget which will contain all the different tabs

    hboxlayout : QHBoxLayout
        a horizontal layout for the window

    Loadlabel : QLabel
        a label that gives the user information

    Output_Name : str
        a string that contains the output name of the file
        createt from the Algorithm

    runButton : QPushButton
        a button that is connected to a method

    messagebox : QMessageBox
        a message box to show information to the user

    Option_selected : str
        a string that shows which button the user clicked

    fasta : str
        a string containg the path to the file

    tsv : str
        a string containg the path to the file

    ini : str
        a string containg the path to the file

    mzML : str
        a string containg the path to the file

    idXML : str
        a string containg the path to the file

    data_path : str
        a string containg the path to the file

    fastaLoaded : boolean
        a boolean showing if the file has been loaded

    tsvLoaded : boolean
        a boolean showing if the file has been loaded

    iniLoaded : boolean
        a boolean showing if the file has been loaded

    mzMLLoaded : boolean
        a boolean showing if the file has been loaded

    idXMLLoaded : boolean
        a boolean showing if the file has been loaded

    User_Warning : QMessageBox
        a message box to show information to the user
    run : str
        a string needed for ProteimicsLFQ

    Methods
    -------

    _init_()
        sets all internal attributes of a window such as layout and buttons

    user_Dialog
        creates a QMessageBox to be shown to the user

    option_selected
        gets the option which the user has selected from the QMessageBox

    clickedLoadData
        loads the data automatically or manually

    runProteomicsLFQ
        runs the ProteimicsLFQ Algorithm
    """

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        # initialize tabs

        self.TabWidget = QTabWidget()
        self.Tab0 = GUI_Welcome_Tab()
        self.Tab1 = GUI_FastaViewer()
        self.Tab2 = Tab_SpectrumViewer()
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
        self.layout.addWidget(self.TabWidget)



        self.hboxlayout = QHBoxLayout()
        self.Loadlabel = QLabel()
        self.Loadlabel.setText("no data loaded")
        self.hboxlayout.addWidget(self.Loadlabel)

        #creating Run Button for the ProteimicsLFQ Algorithm

        self.Output_Name = ''
        self.runButton = QtWidgets.QPushButton(self)
        self.runButton.setText("Run ProteomicsLFQ")
        self.runButton.setFixedWidth(200)

        self.hboxlayout.addWidget(self.runButton)
        self.runButton.clicked.connect(self.runProteomicsLFQ)

        self.Tab0.loadButton.clicked.connect(self.clickedLoadData)
        self.layout.addLayout(self.hboxlayout)
        self.setLayout(self.layout)

        #creates a user dialog and ask the user to choose on option

    def user_Dialog(self):
        """
        creates a Messagebox to get user input

        Parameters
        ---------
        none

        Returns
        -------
        none
        """
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Information")
        messagebox.setIcon(QMessageBox.Question)
        messagebox.setText("Please choose one of the following Options")
        messagebox.addButton("automatically", QtWidgets.QMessageBox.YesRole)
        messagebox.addButton("manualy", QtWidgets.QMessageBox.NoRole)
        messagebox.setDetailedText("If you choose automatically than all"+
            "manually selected Files will be overwritten with the files in "+
            "the folder you select. If you choose manually than they will be "+
            "used instead")
        messagebox.buttonClicked.connect(self.option_selected)
        messagebox.exec_()

    def option_selected(self,button):
        """
        gets the option which the user has selected from the QMessageBox

        Parameters
        ---------
        button : QPushButton
            the button which the user clicked

        Returns
        -------
        none
        """

        global Option_selected
        Option_selected = button.text()








    def clickedLoadData(self):

        """
        loads the data automatically or manually

        Parameters
        ---------
        none

        Returns
        -------
        none
        """

        self.user_Dialog()
        global Option_selected


        #when new data is loaded, clear all previous loaded data

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
            self.Tab3.loadExperimentalDesign(Files_Number_Handler.Dictionary_Return_Value('tsv'))
            self.Tab4.generateTreeModel(Files_Number_Handler.Dictionary_Return_Value('ini_path'))
            self.Tab2.Load_mzML()


        #If User has selected manualy, than take files from dictionary

        if Option_selected == "manualy":
            idXML,mzML,data_path = Welcome_Tab_Logic.Load_ExperimentalData_Manualy(self)
            Files_Number_Handler.Dictionary_Change_File("idXML",idXML)
            Files_Number_Handler.Dictionary_Change_File("mzML",mzML)
            Files_Number_Handler.Dictionary_Change_File("data",data_path)
            Files_Number_Handler.Dictionary_Change_Boolean("data")
            self.Tab2.Load_mzML()

        self.Loadlabel.setText("data loaded")



    def runProteomicsLFQ(self):
        """
        runs the ProteimicsLFQ Algorithm

        Parameters
        ---------
        none

        Returns
        -------
        none
        """

        self.Loadlabel.setText("loading...")
        """launch proteomicsLFQ and add output to PSM/ ProteinViewer Tab"""

        fasta = Files_Number_Handler.Dictionary_Return_Value('fasta')
        tsv = Files_Number_Handler.Dictionary_Return_Value('tsv')
        ini = Files_Number_Handler.Dictionary_Return_Value('ini_path')
        mzML = Files_Number_Handler.Dictionary_Return_Value('mzML')
        idXML = Files_Number_Handler.Dictionary_Return_Value('idXML')
        data_path = Files_Number_Handler.Dictionary_Return_Value('data')

        fastaLoaded = Files_Number_Handler.Dictionary_Return_Boolean('fasta')
        tsvLoaded = Files_Number_Handler.Dictionary_Return_Boolean('tsv')
        iniLoaded = Files_Number_Handler.Dictionary_Return_Boolean('ini_path')
        mzMLLoaded = Files_Number_Handler.Dictionary_Return_Boolean('mzML')
        idXMLLoaded = Files_Number_Handler.Dictionary_Return_Boolean('idXML')

        # user input for the run ProteomicsLFQ Algorithm

        self.Tab0.get_Threads(self.Tab0.Threads)
        self.Tab0.get_Output_FileName(self.Tab0.OutputName)
        self.Tab0.get_ProteinFDR(self.Tab0.ProteinFDR)


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
            run = 'ProteomicsLFQ -write_ini Config.ini'
            os.chdir(data_path)
            os.system(run)
            Files_Number_Handler.Dictionary_Change_File('ini_path', data_path + '/Config.ini')
            Files_Number_Handler.Dictionary_Change_Boolean('ini_path')
            iniLoaded = Files_Number_Handler.Dictionary_Return_Boolean('ini_path')
            ini = Files_Number_Handler.Dictionary_Return_Value('ini_path')
            self.Tab4.generateTreeModel(Files_Number_Handler.Dictionary_Return_Value('ini_path'))


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
            self.Loadlabel.setText('starting job')





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
