#Author: antlampas
#Date: 2023-01-04
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""REST Prompt

A command-line interactive prompt for the OpenSimulator REST Console
"""

#TODO: review the design to "decouple" the prompt from the output

import sys
import urllib.request
import urllib.parse

from threading     import Event

from restConsole   import restConsole
from xmlPrettifier import xmlPrettifier

exit = Event()

def sleep(timeSpan):
    """Sleep

    An utility function for multithreaded sleep
    """
    exit.wait(timeSpan)

def mainLoop():
    """Main Loop

    This is the main loop waiting for user input and prints the REST Console output
    """
    reconnected = False
    while True:
        try:
            if not reconnected:
                command = input("Prompt: ")
            else:
                reconnected = False
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
                sleep(0.5)
                response = console.getExecResponse()
                prettifier = xmlPrettifier(response)
                value = prettifier.prettify()
                print(value,end='')
                sleep(0.1)
        except urllib.error.HTTPError:
            console.connect()
            reconnected = True
        except TimeoutExpired:
            console.getExecResponse()
        except Exception as e:
            print(str(e))
            sys.exit(1)
    print("Disconnecting...")

############################## Initialization #################################
try:
    if   len(sys.argv) == 3:
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

############################ End Initialization ###############################

################################# Main Loop ###################################
mainLoop()
print("Quitting...")
sys.exit(0)
############################### End Main Loop #################################