#Author: antlampas
#Date: 2023-05-17
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import pathlib

class backupConfiguration:
    """Backup Configuration

    This will look for all the .ini and .config files in the opensimulatoir
    instance and it will copy it to the given backup path
    """
    configurationFiles = []
    def __init__(self,basePath="",gridName="",simulatorName="",robustServiceName=""):
        pass