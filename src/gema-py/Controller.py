import sys, os, subprocess
import string    
import random # define the random module  
from shutil import copyfile
import pikepdf
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QHBoxLayout, QLabel, QFileDialog, QListWidgetItem, QTreeWidgetItem, QInputDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def getRandomString():
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
    return ran

# Controller for processing various stuffs

class Controller():
    def __init__(self, config):
        self.path = config.getStoragePath()
        self.dbPath = config.getDBPath()
        self.connecToDB()

    def setWidgetsDict(self, widgetsDict):
        self.widgetsDict = widgetsDict
        self.updateAllListView()
        self.updateCollectionView()

    def connecToDB(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName(self.dbPath)
        if not con.open():
            print("Database Error: %s" % con.lastError().databaseText())
            sys.exit(1)
        return con

    def updateAllListView(self):
        w = self.widgetsDict['AllTree']

        w.clear()

        query = QSqlQuery()
        query.exec("SELECT * from items")

        # _ = range(4)
        while (query.next()):
            # s = '\t'.join(str(query.value(_)) for _ in range(4))
            s = [str(query.value(_)) for _ in range(4)]
            # w.addItem(QTreeWidgetItem(w, s))
            item = QTreeWidgetItem(w, s)

    def updateCollectionView(self):
        w = self.widgetsDict['CollectionTree']

        w.clear()

        query = QSqlQuery()
        query.exec("SELECT * from collections")

        while (query.next()):
            # s = '\t'.join(str(query.value(_)) for _ in range(4))
            s = [str(query.value(_)) for _ in range(2)]
            # w.addItem(QTreeWidgetItem(w, s))
            item = QTreeWidgetItem(w, s)

    def deleteAnItem(self):
        item = self.widgetsDict['AllTree'].selectedItems()
        w = self.widgetsDict['AllTree']
        for i in item:
            path = i.text(3)
            iid = int(i.text(0))
            try:
                os.remove(path)
            except:
                pass
            query = QSqlQuery()
            query.exec(
                f"""
                DELETE from items
                where id = {iid}
                """
            )
        self.updateAllListView()

    def viewAnItem(self):
        item = self.widgetsDict['AllTree'].selectedItems()
        for i in item:
            path = i.text(3)
            open_file(path)

    def addAnItem(self):
        # Get a file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(None,"Pick a file", "","(*.pdf)", options=options)
        if (not filePath):
            return
        name, file_extension = os.path.splitext(filePath)
        newName = getRandomString() + file_extension
        newPath = os.path.join(self.path, newName)
        # print(newPath)
        copyfile(filePath, newPath)
        pdf = pikepdf.Pdf.open(newPath)

        docinfo = pdf.docinfo
        try:
            title = docinfo["/Title"]
            if (not title):
                title = os.path.basename(filePath)
        except:
            title = os.path.basename(filePath)

        query = QSqlQuery()
        # print(title, newPath)
        query.exec(
                f"""
                INSERT INTO items (name, path)
                VALUES ('{title}', '{newPath}')
                """
                )
        self.updateAllListView()

    def addCollection(self):
        text, ok = QInputDialog.getText(None, 'Enter collection name', 'Enter collection name')
        if (not ok):
            return
        query = QSqlQuery()
        # print(title, newPath)
        query.exec(
                f"""
                INSERT INTO collections (name)
                VALUES ('{text}')
                """
                )
        self.updateCollectionView()

    
    def deleteCollection(self):
        items = self.widgetsDict['CollectionTree'].selectedItems()
        for item in items:
            cid = int(item.text(0))

            query = QSqlQuery()
            query.exec(
            f"""
            DELETE from collections
            where id = {cid}
            """
            )
        self.updateCollectionView()
            


    def addToFavorite(self):
        item = self.widgetsDict['AllTree'].selectedItems()
        for i in item:
            fav = 0
            iid = int(i.text(0))
            if (i.text(2) == '1'):
                fav = 1
            fav = 1 - fav
            query = QSqlQuery()
            query.exec(
                f"""
                UPDATE items
                SET fav={fav}
                WHERE id = {iid}
                """
            )
            

        self.updateAllListView()
