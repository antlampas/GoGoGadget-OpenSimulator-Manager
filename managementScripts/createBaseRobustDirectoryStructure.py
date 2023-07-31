#Author: antlampas
#Date: 2023-05-15
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from pathlib import Path

#TODO: test
#TODO: debug
#TODO: add the tode to save the paths in the local database and in the configuration file

class createBaseRobustDirectorystructure:
    errors = []
    def __init__(self,basePath="",baseLogPath="",baseConfPath="",gridName="",services=[]):
        if basepath:     self.bPath = Path(basePath)      else: self.errors.append("No base path provided")
        if baseLogPath:  self.blPath = Path(baseLogPath)  else: self.errors.append("No base log path provided")
        if baseConfPath: self.bcpath = Path(baseConfPath) else: self.errors.append("No base configuration path provided")
        
        if not self.bPath.exists():  self.errors.append("Base path doesn't exist")
        if not self.blPath.exists(): self.errors.append("Base log path doesn't exist")
        if not self.bcPath.exists(): self.errors.append("Base configuration path doesn't exist")

        if gridName:
            self.gridPath     = Path(basePath     + "/opensimulator/" + gridName)
            self.gridLogPath  = Path(baseLogPath  + "/opensimulator/" + gridName)
            self.gridConfPath = Path(baseConfPath + "/opensimulator/" + gridName)
        else:
            self.errors.append("No grid name provided")
        
        if not self.gridPath.exists():     self.errors.append(gridName + " base path doesn't exists")
        if not self.gridLogPath.exists():  self.errors.append(gridName + " base log path doesn't exists")
        if not self.gridConfPath.exists(): self.errors.append(gridName + " base configuration path doesn't exists")

        if not len(self.errors):
            try:
                self.robustPath = str(self.gridPath) + "/robust"
                if not self.robustPath.exists():
                    self.robustPath.mkdir()
                if len(services):
                    for service in services:
                        path = Path(str(self.robustPath) + service)
                        if not path.exists():
                            path.mkdir()
                        else:
                            self.errors.append(service + " path already exists")
            except:
                raise
        else:
            raise Exception(self.errors)
        
        if len(self.errors): raise Exception(self.errors)