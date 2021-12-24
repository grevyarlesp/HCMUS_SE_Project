from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QHBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import pyqtSlot

from Controller import Controller

class CommandButtons(QWidget):
    def __init__(self, controller : Controller):
        self.controller = controller
        QWidget.__init__(self)
        self.layout = QHBoxLayout(self)
        self.buttons = [QPushButton(c) for c in 
                ['Add Item', 'Del Item', 'Add collection', 'Delete collection', 'Save', 'Search', 'Favorite', 'View']
                ]

        for button in self.buttons:
            self.layout.addWidget(button)
        self.buttons[0].clicked.connect(self.addAnItem)
        self.buttons[1].clicked.connect(self.deleteAnItem)
        self.buttons[2].clicked.connect(self.addCollection)
        self.buttons[3].clicked.connect(self.deleteCollection)

        self.buttons[6].clicked.connect(self.addToFavorite)
        self.buttons[7].clicked.connect(self.viewAnItem)
    
    @pyqtSlot()
    def addAnItem(self):
        self.controller.addAnItem()

    @pyqtSlot()
    def deleteAnItem(self):
        self.controller.deleteAnItem()

    @pyqtSlot()
    def viewAnItem(self):
        self.controller.viewAnItem()

    @pyqtSlot()
    def addCollection(self):
        self.controller.addCollection()

    @pyqtSlot()
    def deleteCollection(self):
        self.controller.deleteCollection()

    @pyqtSlot()
    def addToFavorite(self):
        self.controller.addToFavorite()


