import sys
import os
from os.path import expanduser
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QHBoxLayout, QLabel,QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlDatabase

from CommandButtons import CommandButtons
from Controller import Controller
from config import Config

from MyTabWidget import MyTabWidget

import init

class App(QMainWindow):
    def __init__(self, controller : Controller):
        super().__init__()
        self.title = 'GEMA - Generic eBook Management Application'
        self.left = 0
        self.top = 0
        self.width = 680
        self.height = 680
        self.setWindowTitle(self.title)
        self.controller = controller
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initWidgets()
        controller.setWidgetsDict(self.widgetsDict)
        self.InitUI()

    def InitUI(self):
        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.centralLayout)

        self.tab_widget = MyTabWidget(self, self.widgetsDict)
        self.setCentralWidget(self.centralWidget)
        self.centralLayout.addWidget(self.tab_widget)

        # ADd command buttons
        self.buttonsWidget = CommandButtons(self.controller)
        self.centralLayout.addWidget(self.buttonsWidget)
        self.show()

    def initWidgets(self):
        self.widgetsDict = {
                "AllTree": QTreeWidget(),
                "CollectionTree": QTreeWidget()
            }

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return: 
            self.widgetsDict['CollectionTree'].clearSelection()
            self.widgetsDict['AllTree'].clearSelection()
        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == '__main__':
    config = Config()
    controller = Controller(config)
    app = QApplication(sys.argv)
    ex = App(controller)
    sys.exit(app.exec_())
