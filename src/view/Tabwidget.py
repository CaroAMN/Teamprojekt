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
        self.Tab1 = GUI_FastaViewer()
        self.Tab2 = App()
        self.Tab3 = TableEditor()
        self.Tab4 = XMLViewer()
        self.Tab5 = QWidget()

        #add tabs
        self.TabWidget.addTab(self.Tab1,"Proteinsequence Viewer")
        self.TabWidget.addTab(self.Tab2,"Spectrum Viewer")
        self.TabWidget.addTab(self.Tab3,"Experimental Design")
        self.TabWidget.addTab(self.Tab4,"XML Viewer")
        self.TabWidget.addTab(self.Tab5, "PSM/Protein Viewer")


        #add tabs
        self.layout.addWidget(self.TabWidget)
        self.setLayout(self.layout)




def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
