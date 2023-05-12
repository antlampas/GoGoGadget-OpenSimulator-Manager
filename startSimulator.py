#Author: antlampas
#Date: 2023-03-15
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Start Simulator

This creates a Tmux session and starts the simulator in it.
"""

from pathlib import Path
from sys import exit,argv
import libtmux 
import psutil

#Check arguments:
#- Grid Base Path
#- Grid Name
#- Simulator Name
if len(argv)==4:
    gridBasePath  = argv[1]
    gridName      = argv[2]
    simulatorName = argv[3]
    gridBasePath = gridBasePath.rstrip("/")
else:
    exit("Wrong number of arguments")

#Validate arguments
if not Path(gridBasePath).is_dir():
    exit("Grid base path provided doesn't exist")

if not gridName.isalnum():
    exit("Grid name is not alphanumeric only")

if not simulatorName.isalnum():
    exit("Simulator name is not alphanumeric only")

if not Path(gridBasePath+'/simulators/'+simulatorName).is_dir():
    exit("Simulator path doesn't exist")

#Check if the simulator is not running yet
pid = -1
for process in psutil.process_iter():
    try:
        if process.username() == simulatorName:
            if "tmux" in process.name().lower():
                pid = process.pid
                print(pid)
    except:
        pass

#If the simulator is not running, start it
if pid == -1:
    try:
        tmuxServer = libtmux.Server()
        tmuxServer.new_session(session_name=simulatorName,attach=False,start_directory=gridBasePath+'/simulators/'+simulatorName+'/bin',window_name=simulatorName.capitalize(),window_command='./opensim.sh')
    except Exception as e:
        exit("Exception!!! " + str(e))