#Author: antlampas
#Date: 2023-03-15
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
import libtmux

from pathlib import Path

if len(sys.argv)==4:
    gridBasePath  = sys.argv[1]
    gridName      = sys.argv[2]
    simulatorName = sys.argv[3]
    gridBasePath = gridBasePath.rstrip("/")
else:
    sys.exit("Wrong number of arguments")

if not Path(gridBasePath).is_dir():
    sys.exit("Grid base path provided doesn't exist")

if not gridName.isalnum():
    sys.exit("Grid name is not alphanumeric only")

if not simulatorName.isalnum():
    sys.exit("Simulator name is not alphanumeric only")

if not Path(gridBasePath+'/simulators/'+simulatorName).is_dir():
    sys.exit("Simulator path doesn't exist")

tmuxServer = libtmux.Server()

try:
    tmuxServer.new_session(session_name=simulatorName,start_directory=gridBasePath+'/simulators/'+simulatorName+'/bin',window_name=simulatorName.capitalize(),window_command='opensim.sh',attach=False)
except Exception as e:
    print(str(e))
    sys.exit(1)