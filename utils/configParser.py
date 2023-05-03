import re

from sys import argv
from pathlib import Path

class configParser:
    filename = ""
    configuration = {}
    def __init__(self,filename):
        filePath = Path(str(filename))
        if filePath.exists():
            if filePath.is_file():
                self.filename = filename
            else:
                exit(str(filename) + " is not a file")
        else:
            exit("File doesn't exist or incorrect path")
    def getConfiguration(self):
        configUnitStart = re.compile('^\[.*\]$')
        deactivatedOption = re.compile('^;{1,1}')
        comment = re.compile('^;{2,2}')
        with open(self.filename) as configFile:
            unitName = ""
            for line in configFile:
                option = line.strip()
                if configUnitStart.match(option):
                    unitName = option[1:-1]
                    self.configuration[unitName] = {}
                elif deactivatedOption.match(option):
                    if unitName == "":
                        continue
                    else:
                        assignmentPosition = option.find("=")
                        if assignmentPosition > 0:
                            activatedOption = option[1:].strip()
                            optionName = activatedOption[:assignmentPosition-2].strip()
                            value = option[assignmentPosition+1:].strip()
                            self.configuration[unitName][optionName] = value
                elif comment.match(option) or option == "":
                    continue
                else:
                    if unitName == "":
                        continue
                    else:
                        assignmentPosition = option.find("=")
                        if assignmentPosition > 0:
                            optionName = option[:assignmentPosition-1].strip()
                            value = option[assignmentPosition+1:].strip()
                            self.configuration[unitName][optionName] = value