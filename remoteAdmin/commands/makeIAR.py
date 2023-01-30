#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
from remoteAdmin import remoteAdmin

if len(sys.argv) == 8:
    simAddr       = sys.argv[1]
    simPort       = sys.argv[2]
    simPasswd     = sys.argv[3]
    userName      = sys.argv[4]
    userPasswd    = sys.argv[5]
    inventoryPath = sys.argv[6]
    archivePath   = sys.argv[7]
else:
    print("Wrong number of imputs")
    sys.exit(1)

ra = remoteAdmin(f"{simAddr}",f"{simPort}")

iar = ra.command("admin_console_command",{'password':f'{simPasswd}','command':f'save iar {userName} "{inventoryPath}" {userPasswd} "{archivePath}" '})

if oar is not AttributeError:
    print(iar)
    sys.exit(0)
else:
    print("Command not found")
    sys.exit(1)
