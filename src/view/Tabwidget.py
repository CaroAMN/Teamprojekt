from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer
#from mzTabTableWidget import Window
sys.path.insert(0, "../apps")
from SpecViewer import App
from TableEditor import TableEditor
from XMLViewer import XMLViewer


class TabWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle("Protein Analyzer")
        self.tab_widget = AnalyzerTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()


class AnalyzerTabWidget(QWidget):
    def __init__(self,parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #initialize tabs
        self.TabWidget = QTabWidget()
        self.Tab1 = QWidget()
        self.Tab2 = QWidget()
        self.Tab3 = QWidget()
        self.Tab4 = QWidget()
        self.Tab5 = QWidget()

        #add tabs
        self.TabWidget.addTab(self.Tab1,"Proteinsequence Viewer")
        self.TabWidget.addTab(self.Tab2,"Spectrum Viewer")
        self.TabWidget.addTab(self.Tab3,"Experimental Design")
        self.TabWidget.addTab(self.Tab4,"XML Viewer")
        self.TabWidget.addTab(self.Tab5, "PSM/Protein Viewer")

        #Tab1
        self.Tab1.layout = QVBoxLayout(self)
        self.protein_viewer = GUI_FastaViewer()
        self.Tab1.layout.addWidget(self.protein_viewer)
        self.Tab1.setLayout(self.Tab1.layout)

        self.Tab2.layout = QVBoxLayout(self)
        self.spec_viewer = App()
        self.Tab2.layout.addWidget(self.spec_viewer)
        self.Tab2.setLayout(self.Tab2.layout)

        self.Tab3.layout = QVBoxLayout(self)
        self.experimentalDesign = TableEditor()
        self.Tab3.layout.addWidget(self.experimentalDesign)
        self.Tab3.setLayout(self.Tab3.layout)

        self.Tab4.layout = QVBoxLayout(self)
        self.xmlViewer = XMLViewer()
        self.Tab4.layout.addWidget(self.xmlViewer)
        self.Tab4.setLayout(self.Tab4.layout)




        #add tabs
        self.layout.addWidget(self.TabWidget)
        self.setLayout(self.layout)




def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
