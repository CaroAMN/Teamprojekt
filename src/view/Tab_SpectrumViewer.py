import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from FilesNumberHandler import Files_Number_Handler

sys.path.insert(0, "../apps")
from SpecViewer import App


class Tab_SpectrumViewer(QWidget):
    """Creates a Spectrum Viewer for the main application. The loaded mzML files
    are loaded in a combobox. For the selected file the spectrum will be displayed in the
    Spectrum Viewer

    Attributes
    ----------
    SpecViewer = Class App from SpecViewer
        Displays provided spectra from an mzML file

    boxTitel = QLabel
        a label which displays the titel for the combobox

    combobox = QComboBox
        a QComboBox which will contain all loaded mzML file names

    layout = QVBoxLayout
        a vertical layout to locate the Spectrum Viewer and the
        combobox with its titel label

    Horizontal_layout = QHBoxLayout
        a horizontal layout to locate the combobox with its titel label

    Methods
    -------

    Load_mzML
        gets the loaded mzML files from a dictionary and for each file
        a item for the combobox is created

    Load_Spectrum
        gets the selcted item  of the combobox and displays the
        spectrum of the selected file

     """

    def __init__(self):
        super().__init__()

        self.SpecViewer = App()
        self.boxTitel = QLabel()
        self.combobox = QComboBox()

        self.combobox.activated.connect(self.Load_Spectrum)
        self.boxTitel.setText('Identified Spectra')

        self.layout = QVBoxLayout()
        self.Horizontal_layout = QHBoxLayout()
        self.Horizontal_layout.addWidget(self.combobox)
        self.Horizontal_layout.addWidget(self.boxTitel)
        self.Horizontal_layout.addStretch(1)
        self.layout.addWidget(self.SpecViewer)
        self.layout.addLayout(self.Horizontal_layout)


        self.setLayout(self.layout)
        self.show()

    def Load_mzML(self):
        """
        Gets all mzML files from the Dictionary and adds a new item to the
        combobox for each files
        """
        files = Files_Number_Handler.Dictionary_Return_Value('mzML')
        for file in files:
            self.combobox.addItem(file)
        self.combobox.setSizeAdjustPolicy(self.combobox.AdjustToContents)

    def Load_Spectrum(self, file):
        """
        Gets the text of the selected combobox item
        and loads the file to the SPectrum Viewer
        """
        file_name = self.combobox.currentText()
        working_directory = Files_Number_Handler.Dictionary_Return_Value('data')
        self.SpecViewer.setScanBrowserWidget()
        self.SpecViewer.scanbrowser.loadFile(working_directory + '/' + file_name)
