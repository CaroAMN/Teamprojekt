from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer
from mzTabTableWidget import Window
sys.path.insert(0, "../apps")
from XMLViewer import XMLViewer
from TableEditor import TableEditor
from SpecViewer import App

import os

# TODO: eventuell im Nachhinein anderer Ordner (oder generisch)
sys.path.insert(0, '../FRACTIONS')
from ProteomicsLFQ import ProteomicsLFQ


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

        # add load Button for ProteomicsLFQ
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Load ProteomicsLFQ")
        self.pushButton.clicked.connect(self.runProteomicsLFQ)
        self.layout.addWidget(self.pushButton)

        # initialize tabs
        self.TabWidget = QTabWidget()
        self.Tab1 = GUI_FastaViewer()
        self.Tab2 = App()
        self.Tab3 = TableEditor()
        self.Tab4 = XMLViewer()
        self.Tab5 = Window()

        # add tabs
        self.TabWidget.addTab(self.Tab1, "Proteinsequence Viewer")
        self.TabWidget.addTab(self.Tab2, "Spectrum Viewer")
        self.TabWidget.addTab(self.Tab3, "Experimental Design")
        self.TabWidget.addTab(self.Tab4, "XML Viewer")
        self.TabWidget.addTab(self.Tab5, "PSM/Protein Viewer")

        # add tabs
        self.layout.addWidget(self.TabWidget)
        self.setLayout(self.layout)
    
    # launch pyopenms-mztab.py 
    def runProteomicsLFQ(self):
        # TODO: entweder hier direkt ausführen oder in der anderen Methode.        
        # Relevant ist hierbei, dass man im korrekten Verzeichnis ist. 
        os.chdir("""C:/Users/Alex/Desktop/TeamProjekt-ganzes-Team/src/FRACTIONS""")
        os.system("""ProteomicsLFQ -in BSA1_F1.mzML BSA1_F2.mzML BSA2_F1.mzML BSA2_F2.mzML BSA3_F1.mzML BSA3_F2.mzML -ids BSA1_F1.idXML BSA1_F2.idXML BSA2_F1.idXML BSA2_F2.idXML BSA3_F1.idXML BSA3_F2.idXML -design BSA_design.tsv -fasta 18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta -Alignment:max_rt_shift 0 -targeted_only true -transfer_ids false -mass_recalibration false -out_cxml BSA.consensusXML.tmp -out_msstats BSA.csv.tmp -out BSA.mzTab.tmp -threads 1 -proteinFDR 0.3""")

        #ProteomicsLFQ.run_console_ProteomicsLFQ()





def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
