from pathlib import Path

class createBaseRobustDirectorystructure:
    errors = []
    def __init__(self,basePath="/srv",baseLogPath="/var/log",baseConfPath="/etc",gridName="",services=[]):
        if basepath:
            self.bPath = Path(basePath)
        else:
            self.errors.append("No base path provided")
        if baseLogPath:
            self.blPath = Path(baseLogPath)
        else:
            self.errors.append("No base log path provided")
        if baseConfPath:
            self.bcpath = Path(baseConfPath)
        else:
            self.errors.append("No base configuration path provided")
        if gridName:
            self.gridPath     = Path(basePath     + "/opensimulator/" + gridName)
            self.gridConfPath = Path(baseConfPath + "/opensimulator/" + gridName)
            self.gridLogPath  = Path(baseLogPath  + "/opensimulator/" + gridName)
        else:
            self.errors.append("No grid name provided")
        if not len(self.errors):
            try:
                if not len(services):
                    pass
            except:
                pass
        else:
            raise self.errors