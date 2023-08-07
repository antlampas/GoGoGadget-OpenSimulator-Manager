import sys
import asyncio
import re
import time
import urllib
import urwid

from threading import Thread,Event,Lock
from queue     import Queue

from restConsole   import restConsole
from xmlPrettifier import xmlPrettifier

class inputText(urwid.Edit):
    def __init__(self,queue,lock):
        super().__init__('Prompt: ')
        self.queue   = queue
        self.lock    = lock
    def keypress(self,size,key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 'enter':
            if not self.queue.full():
                with self.lock:
                    self.queue.put(self.get_edit_text())
            self.set_edit_text('')
        super(inputText, self).keypress(size, key)

class restPrompt(urwid.WidgetWrap):
    def __init__(self,delay,queue,lock,user="",password="",url="http://127.0.0.1",port=11000):
        self.lock         = lock
        self.queue        = queue
        self.console      = restConsole(user,password,url,port)
        self.alphanum     = re.compile('[a-zA-Z0-9<>]+')
        self.inputWidget  = inputText(queue,lock)
        self.outputWidget = urwid.Text('')
        self._w           = urwid.Frame(body=urwid.Filler(self.outputWidget),footer=self.inputWidget,focus_part='footer')

        self.console.connect()
    def getOutput(self,delay,event):
        startTime = time.perf_counter_ns()
        while True:
            if event.is_set(): break
            response = ''
            endTime  = time.perf_counter_ns()
            if (endTime - startTime) >= delay*pow(10,9):
                try:
                    sys.stderr.write("Getting response\n")
                    response = self.console.getExecResponse()
                    sys.stderr.write(response)
                    startTime = time.perf_counter_ns() 
                except urllib.error.HTTPError as e:
                    sys.stderr.write(str(e)+"\n")
                    console.connect()
                except Exception as e:
                    sys.stderr.write(str(e)+"\n")
                    sys.exit(str(e))
            if response == '':
                sys.stderr.write("Empty response\n")
                if not self.queue.empty():
                    sys.stderr.write("Receiving command\n")
                    with self.lock:
                        command = self.queue.get()
                    sys.stderr.write("Executing command\n")
                    self.console.exec(command)
                    time.sleep(0.6)
                    sys.stderr.write("Command executed. Retreiving response\n")
                    response = self.console.getExecResponse()
                    sys.stderr.write("Response:\n" + response)
            if response != '':
                sys.stderr.write("Writing response onscreen\n")
                prettifier = xmlPrettifier(response)
                prettyResponse = prettifier.prettify()
                if prettyResponse != '':
                    self.outputWidget.set_text(self.outputWidget.get_text()[0] + prettyResponse + '\n')

e = Event()
q = Queue()
l = Lock()

try:
    if   len(sys.argv) == 3:
        tui = restPrompt(1,q,l,sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 4:
        tui = restPrompt(1,q,l,sys.argv[1],sys.argv[2],sys.argv[3])
    elif len(sys.argv) == 5:
        tui = restPrompt(1,q,l,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        sys.exit("Wrong number of arguments")
except Exception as e:
    sys.exit(str(e))

outputThread = Thread(target=tui.getOutput,args=(0.5,e))

outputThread.start()

eventLoop = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
mainLoop  = urwid.MainLoop(tui,event_loop=eventLoop).run()

e.set()
outputThread.join()