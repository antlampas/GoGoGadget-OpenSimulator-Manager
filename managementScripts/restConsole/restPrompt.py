#Author: antlampas
#Date: 2023-08-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
import asyncio
import re
import time
import urllib
import urwid

from threading import Thread,Event
from queue     import Queue

from restConsole   import restConsole
from xmlPrettifier import xmlPrettifier

class inputText(urwid.Edit):
    def __init__(self,queue):
        super().__init__('Prompt: ')
        self.queue = queue
    def keypress(self,size,key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 'enter':
            if not self.queue.full():
                self.queue.put(self.get_edit_text())
            self.set_edit_text('')
        super(inputText, self).keypress(size, key)

class outputText(urwid.ListBox):
    def __init__(self):
        super(outputText,self).__init__(urwid.SimpleListWalker([]))

class restPrompt(urwid.WidgetWrap):
    def __init__(self,event,queue,user="",password="",url="http://127.0.0.1",port=11000):
        self.event        = event
        self.queue        = queue
        self.console      = restConsole(user,password,url,port)
        self.inputWidget  = inputText(self.queue)
        self.outputWidget = outputText()
        self._w           = urwid.Frame(body=self.outputWidget,footer=self.inputWidget,focus_part='footer')
        self.console.connect()
    def getOutput(self,delay):
        while True:
            if self.event.is_set():
                break
            response = ''
            try:
                response = self.console.getExecResponse()
            except urllib.error.HTTPError as e:
                sys.stderr.write(str(e)+"\n")
                console.connect()
            except Exception as e:
                sys.stderr.write(str(e)+"\n")
                sys.exit(str(e))
            if response != '':
                prettifier = xmlPrettifier(response)
                responseList = prettifier.prettify()
                if responseList != '':
                    printList = []
                    for line in responseList:
                        printList.append(urwid.Text(line))
                    for line in printList:
                        self.outputWidget.body.append(line)
                        self.outputWidget.set_focus(len(self.outputWidget.body)-1)
            time.sleep(delay)
    def sendInput(self,delay):
        while True:
            if self.event.is_set():
                break
            while not self.queue.empty():
                command = self.queue.get()
                self.console.exec(command)
            time.sleep(delay)

########################### REST prompt main process ###########################
class mainApp(object):
    def __init__(self):
        self.e = Event()
        self.q = Queue()
        try:
            if   len(sys.argv) == 3:
                self.tui = restPrompt(self.e,self.q,sys.argv[1],sys.argv[2])
            elif len(sys.argv) == 4:
                self.tui = restPrompt(self.e,self.q,sys.argv[1],sys.argv[2],sys.argv[3])
            elif len(sys.argv) == 5:
                self.tui = restPrompt(self.e,self.q,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
            else:
                sys.exit("Wrong number of arguments")
        except:
            sys.exit(sys.exc_info()[1])
    def main(self):
        try:
            outputThread = Thread(target=self.tui.getOutput,args=(0.001,))
            inputThread  = Thread(target=self.tui.sendInput,args=(0.001,))

            outputThread.start()
            inputThread.start()

            eventLoop = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
            mainLoop  = urwid.MainLoop(self.tui,event_loop=eventLoop).run()

            self.e.set()
            print("Waiting for all threads shutdown...")
            outputThread.join()
            inputThread.join()
            print("All threads terminated")

            print("Bye...")
        except:
            sys.exit(sys.exc_info()[1])
######################### REST prompt main process end #########################
main = mainApp()

main.main()