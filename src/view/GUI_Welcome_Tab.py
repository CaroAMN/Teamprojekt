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
        This Application offers the folowing Options

        Proteinsequence Viewer........

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
        Once you jave selected your data you
        can runt the ProteomicsLFQ Algorithm with the Run ProteomicsLFQ Button """
        #assignt Strings to Label as Text
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
        self.Load_ExperimentalData_Button = QPushButton()
        self.Load_ExperimentalData_Button.setText("Load Data")
        self.Load_ExperimentalData_Button.clicked.connect(self.Load_ExperimentalData)

        #Button to run ProteomicsLFQ
        self.Run_ProteomicsLFQ_Button = QPushButton()
        self.Run_ProteomicsLFQ_Button.setText("Run ProteomicsLFQ")
        self.Run_ProteomicsLFQ_Button.clicked.connect(self.Run_ProteomicsLFQ)

        #adding everything to Layouts
        self.main_layout.addWidget(self.Weclome_Title_Label)
        self.main_layout.addWidget(self.Tabs_Explination_Label)
        self.main_layout.addWidget(self.proteomicsLFQ_Title_Label)
        self.main_layout.addWidget(self.proteomicsLFQ_Load_Explination_Label)
        self.main_layout.addWidget(self.proteomicsLFQ_Run_Explination_Label)
        self.Hboxlevel1.addWidget(self.Load_ExperimentalData_Button)
        self.Hboxlevel1.addWidget(self.Run_ProteomicsLFQ_Button)
        self.Hboxlevel1.addStretch(1)
        self.main_layout.addLayout(self.Hboxlevel1)


        self.mainwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.mainwidget)
        self.setWindowTitle('Welcome Screen')

        self.show()


    def Load_ExperimentalData(self):
        #TODO: mabye have to make the arrays global var to be able to use them
        #for further iplementation
        #the file that the user chose is always going to be on the index 0 in
        #its correspinding array
        fasta_files = []
        tsv_files = []
        ExperimentalData_Folder_Path = QFileDialog.getExistingDirectory(self, "Select Directory")
        fasta_files,tsv_files = Files_Number_Handler.Identify_Files_Numbers(ExperimentalData_Folder_Path)
        if Files_Number_Handler.Check_If_Less_Than_One(fasta_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no fasta files in the folder you selected, please try again with different Folder")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()

        if Files_Number_Handler.Check_If_Less_Than_One(tsv_files):
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("There were no tsv files in the folder you selected, please try again with different Folder")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()

        if Files_Number_Handler.Check_If_More_Than_One(fasta_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many fasta files in your Folder please select only one")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            self.Select_Fasta_File(fasta_files)

        if Files_Number_Handler.Check_If_More_Than_One(tsv_files):
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("There are too many tsv files in your Folder please select only one")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            self.Select_Tsv_File(tsv_files)


    def Run_ProteomicsLFQ(self):
        #TODO: run the ProteomicsLFQ_command
        print("Running ProteomicsLFQ_command worked")
    #opens QFileDialog and user must select file if file wrong type display
    #error message
    def Select_Fasta_File(self,File_Array):
        #TODO make it recursive so if the User selects the wrong file it
        #shows the error message and open Select_Fasta_File again until the
        #user makes the right choice
        #PROBLEM if user presses Cancel it still stays in recursion
        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]
        if ExperimentalData_File_Path.endswith(".fasta"):
            File_Array[0] = ExperimentalData_File_Path
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected worng File, File must be fasta file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()



    def Select_Tsv_File(self,File_Array):
        #TODO make it recursive so if the User selects the wrong file it
        #shows the error message and open Select_Tsv_File again until the 
        #user makes the right choice
        #PROBLEM if user presses Cancel it still stays in recursion
        ExperimentalData_File =  QFileDialog.getOpenFileName()
        ExperimentalData_File_Path = ExperimentalData_File[0]
        if ExperimentalData_File_Path.endswith(".tsv"):
            File_Array[0] = ExperimentalData_File_Path
        else:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Information)
            self.error.setText("You have selected worng File, File must be tsv file")
            self.error.setWindowTitle("Error")
            error = self.error.exec_()
def main():

    app = QApplication(sys.argv)
    ex = GUI_Welcome_Tab()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
