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
        self.Tab4 = XMLViewer()
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
        self.loadButton.clicked.connect(self.loadFastaAndTSVButton)

        self.layout.addLayout(self.hboxlayout)


        self.setLayout(self.layout)

        self.data_path = ''
        self.mzML_files =[]
        self.idXML_files = []
        self.tsv_path = ''
        self.fasta_path = ''


    # global load button
    def loadFastaAndTSVButton(self):
        fasta_path, tsv_path, data_path, mzML, idXML = Welcome_Tab_Logic.Load_ExperimentalData(self.Tab0)
        self.Tab1.loadFile(data_path+'/'+fasta_path)
        # ab hier würden wir den tsv_path nutzen, aber mzMLTableView.py ist buggy
        self.Tab3.loadExperimentalDesign(data_path+'/'+tsv_path)
        self.data_path = data_path
        self.mzML_files = mzML
        self.idXML_files = idXML
        self.fasta_path = fasta_path
        self.tsv_path = tsv_path
        print(mzML)
        print(idXML)



    def runProteomicsLFQ(self):
        """launch proteomicsLFQ and add output to PSM/ ProteinViewer Tab"""

        self.Loadlabel.setText("loading...")

        # launch cmd
        #ProteomicsLFQ_command.run_console_ProteomicsLFQ()
        mzTab_file = Welcome_Tab_Logic.Run_ProteomicsLFQ(Welcome_Tab_Logic,self.data_path, self.mzML_files, self.idXML_files, self.fasta_path, self.tsv_path)
        complete_path = self.data_path + '/' + mzTab_file
        self.Tab5.readFile(complete_path)

        #self.TabWidget.removeTab(4)
        #self.Tab5 = Window()
        #self.TabWidget.addTab(self.Tab5, "PSM/Protein Viewer")
        self.Loadlabel.setText("data loaded")





def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
