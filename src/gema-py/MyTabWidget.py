from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QHBoxLayout, QLabel,QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import pyqtSlot
class MyTabWidget(QWidget):
    def __init__(self, parent, widgetsDict):
        super(QWidget, self).__init__(parent)
        self.widgetsDict = widgetsDict

        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        self.tabs.addTab(self.tab1,"Dashboard")
        self.tabs.addTab(self.tab2,"All")
        self.tabs.addTab(self.tab3,"Collection")
        self.tabs.addTab(self.tab4,"Server")
        self.tabs.addTab(self.tab5,"Client")

        self.allViewInit()
        self.collectionViewInit()
       
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def allViewInit(self):
        w = self.widgetsDict['AllTree']
        w.setHeaderLabels(['ID', 'Title', 'Favorite?', 'path'])
        self.tab2layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2layout)
        self.tab2layout.addWidget(w)

    def collectionViewInit(self):
        w = self.widgetsDict['CollectionTree']
        w.setHeaderLabels(['ID', 'Name'])
        self.tab3layout = QVBoxLayout()
        self.tab3.setLayout(self.tab3layout)
        self.tab3layout.addWidget(self.widgetsDict['CollectionTree'])

    @pyqtSlot()
    def on_click(self):
        print("Switch to tab\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


