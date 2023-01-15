#Author: Red Erik @ OSGrid
#Date: 2023-01-04
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
import re
import signal

from time import sleep
from multiprocessing import Process

from restConsole import restConsole
from xmlPrettifier import xmlPrettifier

def mainLoop():
    while True:
        try:
            command = input("Prompt: ")
            if command == "disconnect":
                console.__del__()
                sleep(0.1)
                break
            elif command == "quit":
                status = console.exec("quit")
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

############################## Initialization #################################
try:
    if len(sys.argv) == 3:
        console = restConsole(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 4:
        console = restConsole(sys.argv[1],sys.argv[2],sys.argv[3])
    elif len(sys.argv) == 5:
        console = restConsole(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        sys.exit("Wrong number of arguments")
except Exception as e:
    print(str(e))
    sys.exit(1)

ml = Process(target=mainLoop)
ka = Process(target=console.keepAlive,args=(60,))
############################ End Initialization ###############################

################################# Main Loop ###################################
ml.start()
kl.start()
ml.join()
kl.join()
sys.exit(0)
############################### End Main Loop #################################