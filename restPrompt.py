#Author: Red Erik @ OSGrid
#Date: 2023-01-04
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
import re
from time import sleep

from restConsole import restConsole
from xmlPrettifier import xmlPrettifier

############################## Initialization #################################
if len(sys.argv) == 3:
    try:
        console = restConsole(sys.argv[1],sys.argv[2])
    except Exception as e:
        print(str(e))
        sys.exit(1)
elif len(sys.argv) == 4:
    try:
        console = restConsole(sys.argv[1],sys.argv[2],sys.argv[3])
    except Exception as e:
        print(str(e))
        sys.exit(1)
elif len(sys.argv) == 5:
    try:
        console = restConsole(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    except Exception as e:
        print(str(e))
        sys.exit(1)
else:
    sys.exit("Wrong number of arguments")

status = console.exec("")
response = console.getExecResponse()
prettifier = xmlPrettifier(response)
value = prettifier.prettify()
print(value,end='')
############################ End Initialization ###############################

################################# Main Loop ###################################
while True:
    try:
        command = input("Prompt: ")
        if command == "disconnect":
            console.__del__()
            sleep(0.1)
            break
        elif command == "quit":
            console.exec("quit")
            console.__del__()
            sleep(0.1)
            break
        else:
            status = console.exec(command)
            response = console.getExecResponse()
            prettifier = xmlPrettifier(response)
            value = prettifier.prettify()
            print(value,end='')
    except Exception as e:
        print(str(e))
        sys.exit(1)
sys.exit(0)
############################### End Main Loop #################################