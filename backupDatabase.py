#Author: antlampas
#Date: 2023-05-17
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import pathlib,mysql.connector,sqlite3

class backupDatabase:
    """Backup Database

    This will backup the whole specified database
    """
    configurationFiles = []
    def __init__(self,dbType="mysql",dbName="",host="",username="",password=""):
        pass