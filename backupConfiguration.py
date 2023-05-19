#Author: antlampas
#Date: 2023-05-17
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from pathlib import Path
import re

class backupConfiguration:
    """Backup Configuration

    This will look for all the .ini and .config files in the opensimulatoir
    instance and it will copy it to the given backup path
    """
    configurationFiles = []
    errors = []
    def __init__(self,basePath="",gridName="",simulatorName="",robustServiceName=""):
        """Constructor

        """
        validPath = re.compile("^\/(?:[^/\0]+\/)*[^/\0]$")
        validName = re.compile("^[[:alnum:]]+$")
        
        # Validate base path
        if len(basePath):
            if validPath.match(basePath):
                self.bPath  = Path(basePath)
            else:
                self.errors.append("Invalid path")
        else:
            self.errors.append("No base path provided")
        # Validate grid name
        if len(gridName):
            if validName.match(gridName):
                self.gName  = gridName
            else:
                self.errors.append("Invalid grid name")
        else:
            self.errors.append("No grid name provided")
        # Validate simulator name
        if len(simulatorName):
            if validName.match(simulatorName):
                self.sName = simulatorName
            else:
                self.errors.append("Invalid simulator name")
        else:
            self.sName = ""
        # Validate robust service name
        if len(robustServiceName):
            if validName.match(robustServiceName):
                self.rsName = robustServiceName
            else:
                self.errors.append("Invalid robust service name")
        else:
            self.rsName = ""

        # Check if at least simulator name ro robust service name is not empty
        if not (len(self.sName) and len(self.rsName)):
            self.errors.append("No simulator and no robust service name provided")

        # Actually start the dirty work
        if not len(self.errors):
            if len(self.sName):
                self.simulatorPath = Path(str(self.bPath) + "/" + self.gridName + "/" + self.sName)
            else:
                self.simulatorPath = Path(str(self.bPath) + "/" + self.gridName)
            if len(self.rsName):
                self.robustServiceName = Path(str(self.bPath) + "/" + self.gridName + "/" + self.rsName)
            else:
                self.robustServiceName = Path(str(self.bPath) + "/" + self.gridName)
        else:
            raise Exception(self.errors)