import sys

from PyQt5.QtWidgets import (QGridLayout, QWidget,
                             QLineEdit, QApplication, QLabel)

class Edit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)


    def dragEvent(self, e):
            if e.mimeData().hasFormat('text/uri-list'):
                e.accept()
            else:
                e.ignore()

    def dropEvent(self, e):
        data = e.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            print(filepath)
            self.setText(filepath)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.edit1 = Edit()
        self.edit2 = Edit()
        self.edit3 = Edit()
        self.edit4 = Edit()

        self.mz = QLabel("mz",self)
        self.fasta = QLabel("fasta",self)
        self.tsv = QLabel("tsv",self)
        self.id = QLabel("id",self)

        grid.addWidget(self.mz, 0, 0)
        grid.addWidget(self.edit1, 1, 0)

        grid.addWidget(self.tsv, 0, 1)
        grid.addWidget(self.edit2, 1, 1)

        grid.addWidget(self.id, 2, 0)
        grid.addWidget(self.edit3, 3, 0)

        grid.addWidget(self.fasta, 2, 1)
        grid.addWidget(self.edit4, 3, 1)

        self.setWindowTitle('drag and drop')
        self.setGeometry(300, 300, 300, 150)
        #self.resize()




def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
