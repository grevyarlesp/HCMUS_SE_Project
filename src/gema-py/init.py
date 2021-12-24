from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from config import Config
import sys

def main():
    config = Config()
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(config.getDBPath())
    print(con)
    print(con.databaseName())
    print(con.connectionName())

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    createTableQuery = QSqlQuery()

    createTableQuery.exec(
            """
            CREATE TABLE collections (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR(10) UNIQUE NOT NULL
            )
            """
    )
    createTableQuery.exec(
            """
            CREATE TABLE items (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR(10) NOT NULL, 
                fav BOOLEAN,
                path VARCHAR(10) NOT NULL
            )
            """
        )
    createTableQuery.exec(
            """
            CREATE TABLE CollectionItems (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                item_id INTEGER NOT NULL,
                collection_id INTEGER NOT NULL,
                FOREIGN KEY (item_id) REFERENCES items(id),
                FOREIGN KEY (collection_id) REFERENCES collections(id)
            )
            """
        )
    print(con.tables())

if __name__ == '__main__':
    main()
