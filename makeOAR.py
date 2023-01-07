#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
from datetime import date

from remoteAdmin import remoteAdmin

if len(sys.argv) == 6:
    simAddr       = sys.argv[1]
    simPort       = sys.argv[2]
    simPasswd     = sys.argv[3]
    regionName    = sys.argv[4]
    backupPath    = sys.argv[5]
else:
    print("Wrong number of imputs")
    sys.exit(1)

ra = remoteAdmin(f"{simAddr}",f"{simPort}")

oar = ra.command("admin_save_oar",{'password':f'{simPasswd}','region_name':f'{regionName}','filename':f'{backupPath}/{regionName}-'+date.today().strftime('%Y-%m-%d')+'.oar'})

if oar is not AttributeError:
    print(oar)
    sys.exit(0)
else:
    print("Command not found")
    sys.exit(1)
