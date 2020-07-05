from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer
from mzTabTableWidget import Window
sys.path.insert(0, "../apps")
from SpecViewer import App
from TableEditor import TableEditor
from XMLViewer import XMLViewer


class TabWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.initUI()


    def initUI(self):

        self.layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("Protein Analyzer")

        self.protein_viewer = GUI_FastaViewer()
        self.spec_viewer = App()
        self.experimentalDesign = TableEditor()
        self.xmlViewer = XMLViewer()
        self.mzmlWidget = Window()

        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(self.protein_viewer, "Protein viewer")
        self.tabwidget.addTab(self.spec_viewer, "Spectrum Viewer")
        self.tabwidget.addTab(self.experimentalDesign, "Experimental Design")
        self.tabwidget.addTab(self.xmlViewer, "XML Viewer")
        self.tabwidget.addTab(self.mzmlWidget, "PSM/Protein Viewer")
        self.layout.addWidget(self.tabwidget, 0, 0)
        self.show()

def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
