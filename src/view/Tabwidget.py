from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from GUI_FastaViewer import GUI_FastaViewer

class TabWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label1 = QLabel("Widget in Tab 1.")
        label2 = QLabel("Widget in Tab 2.")
        protein_viewer = Window()
        tabwidget = QTabWidget()
        tabwidget.addTab(protein_viewer, "Protein viewer")
        tabwidget.addTab(label2, "Tab 2")
        layout.addWidget(tabwidget, 0, 0)

def main():
    app = QApplication(sys.argv)
    screen = TabWindow()
    screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
