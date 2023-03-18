import sys
import libtmux

from pathlib import Path

if len(sys.argv)==4:
    gridBasePath  = sys.argv[1]
    gridName      = sys.argv[2]
    simulatorName = sys.argv[3]
else:
    sys.exit("Wrong number of arguments")

if not Path(gridBasePath).is_dir():
    sys.exit("Grid base path provided doesn't exist")

print(gridBasePath)
gridBasePath = gridBasePath.rstrip("/")
print(gridBasePath)

if not gridName.isalnum():
    sys.exit("Grid name is not alphanumeric only")

print(gridName)

if not simulatorName.isalnum():
    sys.exit("Simulator name is not alphanumeric only")

print(simulatorName)

if not Path(gridBasePath+'/simulators/'+simulatorName).is_dir():
    sys.exit("Simulator path doesn't exist")

tmuxServer = libtmux.Server()
tmuxServer.new_session(session_name=simulatorName,start_directory=gridBasePath+'/simulators/'+simulatorName+'/bin',window_name=simulatorName.capitalize(),window_command='opensim.sh',attach=False)
print(tmuxServer.sessions)