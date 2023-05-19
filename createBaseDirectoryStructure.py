#Author: antlampas
#Date: 2023-05-13
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import pathlib

#TODO: test and debug
#TODO: add the tode to save the paths in the local database and in the configuration file

class createBaseDirecotryStructure:
    """Create Base Directory Structure

    This will create the initial OpenSimulator directory structure, with an
    optional initial grid.
    E.g.: if you want opensimulator under /srv/opensimulator and the log files
    under /var/log/opensimulator and the configuration files under
    /etc/opensimulator, you'll need to specify /srv as base path, /var/log
    as base log path and /etc as base conf path. This will create the
    /srv/opensimulator directory for grids, the /etc/opensimulator directory
    for configurattion files and the /var/log/opensimulator directory for logs.
    If you won't specify any base path and base log path, it will use /srv,
    /etc and /var/log as default, following the Filesystem Hierarchy Standard,
    so you'll have /srv/opensimulator, /etc/opensimulator and
    /var/log/opensimulator by default.
    """
    errors = []
    
    #Base path
    bPath  = ""
    #Base log path
    blPath = ""
    #Base configuration path
    bcPath = ""

    def __init__(self,basePath="/srv",baseLogPath="/var/log",baseConfPath="/etc"):
        """Constructor

        The constructor does all the work: checks the paths and tries to create
        the base directory structure. If it's unable to, it will put all the
        errors in a errors list and it will raise it as exception.
        """
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
        #Checks on paths
        for path in [bPath,blPath,bcPath]:
            if not path.exists():
                self.errors.append(str(path) + " doesn't exist")
                continue
            if not path.is_absolute():
                self.errors.append(path + " is not absolute")
                continue

            path.joinpath('opensimulator')
            
            if path.exists():
                self.errors.append(str(path) + " already exists")
            else:
                try:
                    path.mkdir(chmod=0o755):
                except OSError as e:
                    self.errors.append("Can't create " + path + " because " +str(e))
        if len(errors):
            raise Exception(self.errors)