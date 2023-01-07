#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
from datetime import datetime,timedelta
from pathlib  import Path

if len(sys.argv) == 4:
    p = Path(sys.argv[1])
    timespan = int(sys.argv[2])
    regionName = str(sys.argv[3])
else:
    print("Wrong number of inputs")
    sys.exit(1)

f = list(sorted(p.glob('*')))

for i in f:
    s = i.stem
    d = datetime.strptime(s[-10:],'%Y-%m-%d')
    n = s[:-11]
    delta = datetime.today() - d
    if delta > timedelta(days=timespan) and n == regionName:
        i.unlink()
        print("File deleted")
sys.exit(0)
