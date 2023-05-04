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
        comment = re.compile('^;{2,2}|;#')
        optionValidBeginning = re.compile('^[a-zA-Z]')
        with open(self.filename) as configFile:
            unitName = ""
            for line in configFile:
                option = line.strip()
                if configUnitStart.match(option):
                    unitName = option[1:-1]
                    self.configuration[unitName] = {}
                elif comment.match(option) or option == "":
                    continue
                elif deactivatedOption.match(option):
                    if unitName == "":
                        continue
                    else:
                        activatedOption = option[1:].strip()
                        if optionValidBeginning.match(activatedOption):
                            assignmentPosition = activatedOption.find("=")
                            if assignmentPosition > 0:
                                optionName = activatedOption[:assignmentPosition].strip()
                                if assignmentPosition < len(activatedOption):
                                    value = activatedOption[assignmentPosition+1:].strip()
                                else:
                                    value = ""
                                if optionName in self.configuration[unitName].keys():
                                    if type(self.configuration[unitName][optionName]) is list:
                                        self.configuration[unitName][optionName].append(value)
                                    else:
                                        optionsList = [self.configuration[unitName][optionName]]
                                        optionsList.append(value)
                                        self.configuration[unitName][optionName] = optionsList
                                else:
                                    self.configuration[unitName][optionName] = str(value)
                else:
                    if unitName == "":
                        continue
                    else:
                        assignmentPosition = option.find("=")
                        if assignmentPosition > 0:
                            optionName = option[:assignmentPosition].strip()
                            value = option[assignmentPosition+1:].strip()
                            if optionName in self.configuration[unitName].keys():
                                if type(self.configuration[unitName][optionName]) is list:
                                    self.configuration[unitName][optionName].append(value)
                                else:
                                    optionsList = [self.configuration[unitName][optionName]]
                                    optionsList.append(value)
                                    self.configuration[unitName][optionName] = optionsList
                            else:
                                self.configuration[unitName][optionName] = str(value)