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
from Welcome_Tab_Logic import Welcome_Tab_Logic
#from Tabwidget import AnalyzerTabWidget


class GUI_Welcome_Tab(QMainWindow):


    def __init__(self):


        super().__init__()
        self.resize(1280, 720)
        self.initUI()

    def initUI(self):
        #creating the Layout, QVBoxLayout with hboxlayout in it fot the
        #different levels
        self.Output_Name = ''
        self.Threads_Number = ''
        self.ProteiFDR_Number = ''
        self.mainwidget = QWidget(self)
        self.main_layout = QVBoxLayout(self.mainwidget)
        self.main_layout.setSpacing(10)
        self.Hboxlevel1 = QHBoxLayout()

        #Creating QLabel with welcome Text to display on first Tab

        self.Weclome_Title_Label = QLabel()
        self.Tabs_Explination_Label = QLabel()
        self.proteomicsLFQ_Title_Label = QLabel()
        self.proteomicsLFQ_Load_Explination_Label = QLabel()
        self.proteomicsLFQ_Run_Explination_Label = QLabel()

        self.loadButton = QtWidgets.QPushButton(self)
        self.loadButton.setText("Load Data")
        self.loadButton.setFixedWidth(200)
        #self.loadButton.clicked.connect(AnalyzerTabWidget.clickedLoadData)

        """
        self.LineEdit = QLineEdit(self)
        self.RenameButton = QtWidgets.QPushButton(self)
        self.RenameButton.clicked.connect(lambda: self.get_Output_FileName(self.LineEdit))
        self.RenameButton.setText('Set Name')
        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(10)
        self.hbox.addWidget(self.LineEdit)
        self.hbox.addWidget(self.RenameButton)
        self.hbox.addStretch(1)"""

        self.OutputName = QLineEdit(self)
        #self.OutputName.setText("")
        self.OutputName_Label = QLabel(self)
        self.OutputName_Label.setText('Name for Output Files')
        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(10)
        self.hbox.addWidget(self.OutputName)
        self.hbox.addWidget(self.OutputName_Label)
        self.hbox.addStretch(1)

        self.Threads = QLineEdit(self)
        self.Threads.setText('1')
        self.Threads_Label = QLabel(self)
        self.Threads_Label.setText('Threads')
        self.hbox2 = QHBoxLayout()
        self.hbox2.setSpacing(10)
        self.hbox2.addWidget(self.Threads)
        self.hbox2.addWidget(self.Threads_Label)
        self.hbox2.addStretch(1)

        self.ProteinFDR = QLineEdit(self)
        self.ProteinFDR.setText('0.3')
        self.ProteinFDR_Label = QLabel(self)
        self.ProteinFDR_Label.setText('Protein FDR')
        self.hbox3 = QHBoxLayout()
        self.hbox3.setSpacing(10)
        self.hbox3.addWidget(self.ProteinFDR)
        self.hbox3.addWidget(self.ProteinFDR_Label)
        self.hbox3.addStretch(1)


        welcome_Title = "OpenMS ProteomicsLFQ QApplication  "
        Tabs_Explination = """
        This Application offers the folowing Options:

        Proteinsequence Viewer: Displays all information of the loaded Fasta file.

        Spectrum Viewer: Displays the identified spectra.

        Experimental Design: Display and edit the content of your tsv or csv file or load your mzML files to create a tsv and csv file.

        XML Viewer: Displays a provided configuration file.

        PSM/Protein Viewer: Displays the output mzTab file after successful running the ProteomicsLFQ.
                        """
        proteomicsLFQ_Title =   " ProteomicsLFQ "
        proteomicsLFQ_Load_Explination ="""You can load your data automatically by selecting a folder containing all necessary files (.fasta, .ini, .tsv/.csv, .mzML, .idXML)
        or load your data and select the other files manually ( .fasta, .ini, .tsv/csv) through the different tabs"""
        proteomicsLFQ_Run_Explination ="""
        Once you have selected your data you
        can run the ProteomicsLFQ Algorithm with the Run ProteomicsLFQ Button """
        #assignt Strings to Label as Text

        #TODO Creat select folder button
        #TODO creat text line for coosing output name
        #TODO data load label needs to show which files are missing, data loaded when all files are provided


        self.Weclome_Title_Label.setText(welcome_Title)
        self.Tabs_Explination_Label.setText(Tabs_Explination)

        self.proteomicsLFQ_Title_Label.setText(proteomicsLFQ_Title)
        self.proteomicsLFQ_Load_Explination_Label.setText(proteomicsLFQ_Load_Explination)
        self.proteomicsLFQ_Run_Explination_Label.setText(proteomicsLFQ_Run_Explination)
        # seting font for Labels
        self.Weclome_Title_Label.setFont(QFont("Sanserif",20))
        self.Tabs_Explination_Label.setFont(QFont("Sanserif",10))
        self.proteomicsLFQ_Title_Label.setFont(QFont("Sanserif",13))
        self.proteomicsLFQ_Load_Explination_Label.setFont(QFont("Sanserif",10))
        self.proteomicsLFQ_Run_Explination_Label.setFont(QFont("Sanserif",13))
        #creating Buttons

        #Button to load experimental Data
        #self.Load_ExperimentalData_Button = QPushButton()
        #self.Load_ExperimentalData_Button.setText("Load Data")
        #self.Load_ExperimentalData_Button.clicked.connect(Welcome_Tab_Logic.Load_ExperimentalData)

        #Button to run ProteomicsLFQ
        #self.Run_ProteomicsLFQ_Button = QPushButton()
        #self.Run_ProteomicsLFQ_Button.setText("Run ProteomicsLFQ")
        #self.Run_ProteomicsLFQ_Button.clicked.connect(Welcome_Tab_Logic.Run_ProteomicsLFQ)

        #adding everything to Layouts
        self.main_layout.addWidget(self.Weclome_Title_Label)
        self.main_layout.addWidget(self.Tabs_Explination_Label)

        self.main_layout.addWidget(self.proteomicsLFQ_Title_Label)
        self.main_layout.addWidget(self.proteomicsLFQ_Load_Explination_Label)
        self.main_layout.addWidget(self.loadButton)
        self.main_layout.addLayout(self.hbox)
        self.main_layout.addLayout(self.hbox2)
        self.main_layout.addLayout(self.hbox3)
        self.main_layout.addWidget(self.proteomicsLFQ_Run_Explination_Label)
        #self.Hboxlevel1.addWidget(self.Load_ExperimentalData_Button)
        #self.Hboxlevel1.addWidget(self.Run_ProteomicsLFQ_Button)
        self.Hboxlevel1.addStretch(1)
        self.main_layout.addLayout(self.Hboxlevel1)



        self.mainwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.mainwidget)
        self.setWindowTitle('Welcome Screen')

        self.show()

    def get_Output_FileName(self, QLineEdit):
        self.Output_Name = QLineEdit.text()

    def get_Threads(self, QLineEdit):
        self.Threads_Number = QLineEdit.text()

    def get_ProteinFDR(self, QLineEdit):
        self.ProteiFDR_Number = QLineEdit.text()



#def main():
#
 #   app = QApplication(sys.argv)
  #  ex = GUI_Welcome_Tab()
   # sys.exit(app.exec_())


#if __name__ == '__main__':
 #   main()
