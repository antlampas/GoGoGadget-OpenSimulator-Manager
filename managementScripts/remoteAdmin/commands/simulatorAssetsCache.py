#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys

from time import sleep

from remoteAdmin import remoteAdmin

if len(sys.argv) == 4:
    simAddr       = sys.argv[1]
    simPort       = sys.argv[2]
    simPasswd     = sys.argv[3]
else:
    print("Wrong number of imputs")
    sys.exit(1)

ra = remoteAdmin(f"{simAddr}",f"{simPort}")

sleep(0.01)

retry = True
while retry:
    try:
        clearCache = ra.command("admin_console_command",{'password':f'{simPasswd}','command':'fcache assets'})
    except:
        retry = True
    else:
        retry = False
    sleep(0.01)

if clearCache is not AttributeError:
    print(clearCache)
    sys.exit(0)
else:
    print("Command not found")
    sys.exit(1)
