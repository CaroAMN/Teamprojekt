from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer
from mzMLTableView import mzMLTableView
from ConfigView import ConfigView
sys.path.insert(0, "../apps")
from SpecViewer import App


class TabWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label1 = QLabel("Widget in Tab 1.")
        label2 = QLabel("Widget in Tab 2.")
        protein_viewer = GUI_FastaViewer()
        spec_viewer = App()
        mzml_viewer = mzMLTableView()
        config_viewer = ConfigView()
        
        tabwidget = QTabWidget()
        tabwidget.addTab(protein_viewer, "Protein viewer")
        tabwidget.addTab(spec_viewer, "Spectrum Viewer")
        tabwidget.addTab(mzml_viewer, "PSM/Protein Viewer")
        tabwidget.addTab(config_viewer, "Config Viewer")
        layout.addWidget(tabwidget, 0, 0)

def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
