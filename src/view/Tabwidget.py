from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer
from mzTabTableWidget import Window
sys.path.insert(0, "../apps")
from SpecViewer import App
from TableEditor import TableEditor
from XMLViewer import XMLViewer


class TabWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        protein_viewer = GUI_FastaViewer()
        spec_viewer = App()
        experimentalDesign = TableEditor()
        xmlViewer = XMLViewer()
        mzmlWidget = Window()

        tabwidget = QTabWidget()
        tabwidget.addTab(protein_viewer, "Protein viewer")
        tabwidget.addTab(spec_viewer, "Spectrum Viewer")
        tabwidget.addTab(experimentalDesign, "Experimental Design")
        tabwidget.addTab(xmlViewer, "XML Viewer")
        tabwidget.addTab(mzmlWidget, "PSM/Protein Viewer")
        layout.addWidget(tabwidget, 0, 0)

def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
