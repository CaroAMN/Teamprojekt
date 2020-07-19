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


class GUI_Welcome_Tab(QMainWindow):


    def __init__(self):


        super().__init__()
        self.resize(1280, 720)
        self.initUI()

    def initUI(self):
        #creating the Layout, QVBoxLayout with hboxlayout in it fot the
        #different levels

        self.mainwidget = QWidget(self)
        self.main_layout = QVBoxLayout(self.mainwidget)
        self.Hboxlevel1 = QHBoxLayout()

        #Creating QLabel with welcome Text to display on first Tab

        self.Weclome_Title_Label = QLabel()
        self.Tabs_Explination_Label = QLabel()
        self.proteomicsLFQ_Title_Label = QLabel()
        self.proteomicsLFQ_Load_Explination_Label = QLabel()
        self.proteomicsLFQ_Run_Explination_Label = QLabel()

        welcome_Title = "Welcome to the Experimental Viewer"
        Tabs_Explination = """
        This Application offers the folowing Options:

        Proteinsequence Viewer: Check the loaded Proteins with all their informations from a .fasta file.

        Spectrum Viewer.......

        Experimental Design.......

        XML Viewer................

        PSM/Protein Viewer..............
                        """
        proteomicsLFQ_Title =   " ProteomicsLFQ "
        proteomicsLFQ_Load_Explination="""
        If you have experimental Data saved on this Hardware
        please select the Folder in which the Data is saved
        """
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
        self.Tabs_Explination_Label.setFont(QFont("Sanserif",13))
        self.proteomicsLFQ_Title_Label.setFont(QFont("Sanserif",15))
        self.proteomicsLFQ_Load_Explination_Label.setFont(QFont("Sanserif",13))
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
        self.main_layout.addWidget(self.proteomicsLFQ_Run_Explination_Label)
        #self.Hboxlevel1.addWidget(self.Load_ExperimentalData_Button)
        #self.Hboxlevel1.addWidget(self.Run_ProteomicsLFQ_Button)
        self.Hboxlevel1.addStretch(1)
        self.main_layout.addLayout(self.Hboxlevel1)


        self.mainwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.mainwidget)
        self.setWindowTitle('Welcome Screen')

        self.show()



#def main():
#
 #   app = QApplication(sys.argv)
  #  ex = GUI_Welcome_Tab()
   # sys.exit(app.exec_())


#if __name__ == '__main__':
 #   main()
