import re

from sys import argv
from pathlib import Path

class configParser:
    filename = ""
    activeConfiguration = {}
    inactiveConfiguration = {}
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
                    self.activeConfiguration[unitName] = {}
                    self.inactiveConfiguration[unitName] = {}
                elif comment.match(option) or option == "":
                    continue
                elif deactivatedOption.match(option):
                    if unitName == "":
                        continue
                    else:
                        decommentedOption = option[1:].strip()
                        if optionValidBeginning.match(decommentedOption):
                            assignmentPosition = decommentedOption.find("=")
                            if assignmentPosition > 0:
                                optionName = decommentedOption[:assignmentPosition].strip()
                                if assignmentPosition < len(decommentedOption):
                                    value = decommentedOption[assignmentPosition+1:].strip()
                                else:
                                    value = ""
                                if optionName in self.inactiveConfiguration[unitName].keys():
                                    if type(self.inactiveConfiguration[unitName][optionName]) is list:
                                        self.inactiveConfiguration[unitName][optionName].append(value)
                                    else:
                                        optionsList = [self.inactiveConfiguration[unitName][optionName]]
                                        optionsList.append(value)
                                        self.inactiveConfiguration[unitName][optionName] = optionsList
                                else:
                                    self.inactiveConfiguration[unitName][optionName] = str(value)
                else:
                    if unitName == "":
                        continue
                    else:
                        assignmentPosition = option.find("=")
                        if assignmentPosition > 0:
                            optionName = option[:assignmentPosition].strip()
                            value = option[assignmentPosition+1:].strip()
                            if optionName in self.activeConfiguration[unitName].keys():
                                if type(self.activeConfiguration[unitName][optionName]) is list:
                                    self.activeConfiguration[unitName][optionName].append(value)
                                else:
                                    optionsList = [self.activeConfiguration[unitName][optionName]]
                                    optionsList.append(value)
                                    self.activeConfiguration[unitName][optionName] = optionsList
                            else:
                                self.activeConfiguration[unitName][optionName] = str(value)