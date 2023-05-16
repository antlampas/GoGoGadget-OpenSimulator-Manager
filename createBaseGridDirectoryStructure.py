#Author: antlampas
#Date: 2023-05-15
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from pathlib import Path

class createBaseGridDirectorystructure:
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
        
        if self.gridPath.exists():     self.errors.append(gridName + " base path already exists")
        if self.gridLogPath.exists():  self.errors.append(gridName + " base log path already exists")
        if self.gridConfPath.exists(): self.errors.append(gridName + " base configuration path already exists")

        if not len(self.errors):
            try:
                if not len(services):
                    self.gridPath.mkdir()
                    self.gridLogPath.mkdir()
                    self.gridConfPath.mkdir()
            except:
                raise
        else:
            raise Exception(self.errors)