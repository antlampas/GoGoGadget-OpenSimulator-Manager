#Author: antlampas
#Date: 2023-05-01
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import re

from sys import argv
from pathlib import Path

class configParser:
    """Configuration Parser

    Reads a single OpenSimulator configuration file and makes it available as a
    dictionary of configuration statemens and their values.
    There's a second dictionary, in case there are "disabled" configurations in
    the configuration file; that's exposed too.

    filename = the configuration file path to be examined
               activeConfiguration = the actual configuration read from the
               configuration file. Its a "hierarchical" dictionary and the
               key-value pair meaning is SectionName-OptionDictionary. The
               key-value pair meaning is OptionName-value
    inactiveConfiguration = here are all those options marked as "deactivated"
               or "defaulted" i.e. lines beginning with a single colon (;). The
               dictionary structure is the same as the activeConfiguration
    activeConfiguration = here are all the actual configured lines, i.e. all
               the lines not beginning with a single colon (;).
    """
    filename = ""
    activeConfiguration = {}
    inactiveConfiguration = {}
    def __init__(self,filename):
        """Constructor

        At parser initialization it expects the configuration file path, and
        checks if it exists and if it's an actual file, i.e. not a directory
        """
        filePath = Path(str(filename))
        if filePath.exists():
            if filePath.is_file():
                self.filename = filename
            else:
                exit(str(filename) + " is not a file")   #TODO: convert this to Exceptions System
        else:
            exit("File doesn't exist or incorrect path") #TODO: convert this to Exceptions System
    def readConfiguration(self):
        """Read Configuration

        This is what does the actual nasty work: reads the configuration line
        by line, ignores the "pure comments", i.e. the lines starting with
        double colons (;;), puts the line starting and endind with square
        brakets in the active configuration dictionary, puts the configuration
        lines in a dictionary in the corresponding section key of the active
        configuration dictionary and the deactivated lines, i.e. the lines
        starting with a single colon (;), in the deactivated configuration
        dictionary
        """
        ##Regular Expressions for line recognition.
        #Identifies the configuration section name
        configSectionStart = re.compile('^\[.*\]$') 
        #Identifies the deactivated configuration line
        deactivatedOption = re.compile('^;{1,1}')
        #Identifies the comments
        comment = re.compile('^;{2,2}|;#')
        #Configuration line validation:
        #- must start with a character
        #- must contain a equal sign
        #- must not contain spaces between words before the equal sign
        optionValidBeginning = re.compile('^[a-zA-Z][a-zA-Z0-9]*\s?=.*')
        with open(self.filename) as configFile:
            sectionName = ""
            for line in configFile:
                option = line.strip()
                if configSectionStart.match(option):
                    sectionName = option[1:-1]
                    self.activeConfiguration[sectionName]   = {}
                    self.inactiveConfiguration[sectionName] = {}
                elif comment.match(option) or option == "":
                    #Ignore comments and empty lines
                    continue
                elif deactivatedOption.match(option):
                    #Checks if we're in a configuration section
                    if sectionName == "":
                        continue
                    else:
                        #Being a deactivated configuration line, it starts with
                        #a colon. We don't need to put the colon in the
                        #dictionary. We delete the colon and we will put the
                        #configuration line in the deactivatedOption dictionary
                        decommentedOption = option[1:].strip()
                        if optionValidBeginning.match(decommentedOption):
                            assignmentPosition = decommentedOption.find("=")
                            if assignmentPosition > -1:
                                optionName = decommentedOption[:assignmentPosition].strip()
                                if assignmentPosition < len(decommentedOption):
                                    value = decommentedOption[assignmentPosition+1:].strip()
                                else:
                                    value = ""
                                if optionName in self.inactiveConfiguration[sectionName].keys():
                                    if type(self.inactiveConfiguration[sectionName][optionName]) is list:
                                        self.inactiveConfiguration[sectionName][optionName].append(value)
                                    else:
                                        optionsList = [self.inactiveConfiguration[sectionName][optionName]]
                                        optionsList.append(value)
                                        self.inactiveConfiguration[sectionName][optionName] = optionsList
                                else:
                                    self.inactiveConfiguration[sectionName][optionName] = str(value)
                else:
                    #Checks if we're in a configuration section
                    if sectionName == "":
                        continue
                    else:
                        assignmentPosition = option.find("=")
                        if assignmentPosition > 0:
                            optionName = option[:assignmentPosition].strip()
                            value = option[assignmentPosition+1:].strip()
                            #Considering Python dictionaries can't hold
                            #duplicates keys, we need a workaround: put
                            #multiple values bound to "duplicated" keys in a
                            #list and assign it to the key
                            if optionName in self.activeConfiguration[sectionName].keys():
                                if type(self.activeConfiguration[sectionName][optionName]) is list:
                                    self.activeConfiguration[sectionName][optionName].append(value)
                                else:
                                    optionsList = [self.activeConfiguration[sectionName][optionName]]
                                    optionsList.append(value)
                                    self.activeConfiguration[sectionName][optionName] = optionsList
                            else:
                                self.activeConfiguration[sectionName][optionName] = str(value)