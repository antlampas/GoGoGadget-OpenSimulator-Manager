#Author: antlampas
#Date: 2023-05-17
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from pathlib import Path
import shutil
import re

#TODO: test
#TODO: debug

class backupConfiguration:
    """Backup Configuration

    This will look for all the .ini and .config files in the opensimulatoir
    instance and it will copy it to the given backup path
    """
    configurationFiles = []
    errors = []
    def __init__(self,backupBasePath="",basePath="",gridName="",simulatorName="",robustServiceName=""):
        """Constructor

        """
        validPath = re.compile("^\/(?:[^/\0]+\/)*[^/\0]$")
        validName = re.compile("^[[:alnum:]]+$")
        
        # Validate paths
        if len(backupBasePath):
            if validPath.match(backupBasePath):
                self.backupBasePath  = Path(backupBasePath)
            else:
                self.errors.append("Invalid backup path")
        else:
            self.errors.append("No backup path provided")
        if len(basePath):
            if validPath.match(basePath):
                self.basePath  = Path(basePath)
            else:
                self.errors.append("Invalid base path")
        else:
            self.errors.append("No base path provided")
        # Validate names
        if len(gridName):
            if validName.match(gridName):
                self.gridName  = gridName
            else:
                self.errors.append("Invalid grid name")
        else:
            self.errors.append("No grid name provided")
        if len(simulatorName):
            if validName.match(simulatorName):
                self.simulatorName = simulatorName
            else:
                self.errors.append("Invalid simulator name")
        else:
            self.simulatorName = ""
        if len(robustServiceName):
            if validName.match(robustServiceName):
                self.robustServiceName = robustServiceName
            else:
                self.errors.append("Invalid robust service name")
        else:
            self.robustServiceName = ""

        # Check if at least simulator name ro robust service name is not empty
        if not (len(self.simulatorName) and len(self.robustServiceName)):
            self.errors.append("No simulator and no robust service name provided")

        # Actually does the dirty work
        if not len(self.errors):
            # If a simulator name is provided, use it to build the simulator
            # path. Otherwise, put a "null path" in it. I used the "base grid
            # path" as "null path" by convention.
            if len(self.simulatorName):
                self.simulatorPath = Path(str(self.basePath) + "/" + self.gridName + "/" + self.simulatorName)
            else:
                self.simulatorPath = Path(str(self.basePath) + "/" + self.gridName)
            # If a robust service name is provided, use it to build the
            # simulator path. Otherwise, put a "null path" in it. I used the
            # "base grid path" as "null path" by convention.
            if len(self.robustServiceName):
                self.robustServiceName = Path(str(self.basePath) + "/" + self.gridName + "/" + self.robustServiceName)
            else:
                self.robustServiceName = Path(str(self.basePath) + "/" + self.gridName)
            self.backupPath = Path(str(self.backupBasePath) + "/" + self.gridName)
            if not self.simulatorPath.samepath(Path(str(self.basePath) + "/" + self.gridName)):
                for f in self.simulatorPath.iterdir():
                    if (f.is_file() and (f.suffix == "ini" or f.suffix == "config")) or
                       (f.is_dir() and (f.name == "config-include" or f.name == "Regions")):
                        shutil.copy(str(f),str(backupPath)+f.name) #TODO: Temporary. Check if there's a way to do this with pathlib
        else:
            raise Exception(self.errors)