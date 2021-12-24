import os

from os.path import expanduser
class Config():
    def __init__(self):
        home = expanduser("~")
        path = os.path.join(home, 'Documents','GEMALibrary')
        try:
            os.mkdir(path)
        except:
            pass
        self.path = path

    def getStoragePath(self):
        return self.path

    def getDBPath(self):
        return os.path.join(self.path, "store.db")

