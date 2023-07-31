#Author: antlampas
#Date: 2023-02-08
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

#dbManager(dbType,dbName,dbPath,host,port,username,password)
#
# dbType   = sqlite or mysql
# dbName   = database name saved in sqlite or mysql
# dbPath   = (SQLITE ONLY) the database path
# host     = (MYSQL ONLY) MySQL host
# port     = (MYSQL ONLY) MySQL port
# username = (MYSQL ONLY) MySQL database username
# password = (MYSQL ONLY) MySQL database password

#TODO: test
#TODO: debug

from pathlib import Path

class dbManager:
    """Database Manager

    This class acts as an uniform interface to the underlying DBMS, hiding the
    underlying complexity, so the user don't have to worry if the underlying
    DBMS is MySQL, MariaDB or Sqlite.
    """
    dbType = ""
    dbName = ""
    dbPath = ""
    host   = ""
    port   = 0

    def __init__(self,dbType="sqlite",dbName="",dbPath="",host="127.0.0.1",port="3306",username="",password=""):
        """Constructor

        Initializes the underlying DBMS with the correct connection data.
        """
        self.dbName = dbName
        self.dbType = dbType
        self.dbPath = dbPath
        if self.dbType == "sqlite":
            import sqlite3 as dbInterface
            self.sqlitePath = Path(self.dbPath + self.dbName)
            self.dbInterface  = dbInterface
            self.dbConnection = self.dbInterface.connect(str(self.sqlitePath))
        elif self.dbType == "mysql":
            import mysql.connector as dbInterface
            self.dbInterface  = dbInterface
            self.dbConnection = self.dbInterface.connect(user=username,password=password,host=host,port=port,database=self.dbName)
        else:
            print("Database type not supported or typo in database type")
        self.dbCursor = self.dbConnection.cursor()
    def query(self,query=""):
        response = self.dbCursor.execute(query).fetchall()
        return response
    def backupDB(self,dbName="",savePath=""):
        """Backup database

        This makes the physical backup of the database.
        """
        backupPath = Path(savePath)
        if backupPath.exists():
            if backupPath.is_dir():
                if self.dbType == "sqlite":
                    dbConnection.backup(backupPath)
                elif self.dbType == "mysql":
                    pass
            else:
                raise Exception("Provided backup path is not a directory")
        else:
            raise Exception("Provided backup path doesn't exist")