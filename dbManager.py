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

class dbManager:
    dbName = ""
    dbPath = ""
    def __init__(self,dbType="sqlite",dbName="",dbPath="",host="127.0.0.1",port="3306",username="",password=""):
        self.dbName = dbName
        if dbType == "sqlite":
            import sqlite3 as dbInterface
            self.dbInterface  = dbInterface
            self.dbConnection = self.dbInterface.connect(self.dbName)
        elif dbType == "mysql":
            import mysql.connector as dbInterface
            self.dbInterface  = dbInterface
            self.dbConnection = self.dbInterface.connect(user=username,password=password,host=host,port=port,database=self.dbName)
        else:
            print("Database type not supported or typo in database type name")
        self.dbCursor = self.dbConnection.cursor()
    def createDB(self,dbName=""):
        self.dbCursor.execute("CREATE DATABASE " + dbName)
    def backupDB(self,dbName="",savePath=""): pass
    def dropDB(self,dbName=""): pass

db = dbManager(dbType="mysql")