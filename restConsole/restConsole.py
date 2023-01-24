#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import urllib.request
import urllib.parse
import defusedxml.minidom
import sys
import signal

from threading import Event

class restConsole:
    SessionID = 0
    def __init__(self,user="",password="",url="http://127.0.0.1/",port="11000"):
        self.url      = url
        self.port     = port
        self.user     = user
        self.password = password
        self.connect()
    def connect(self):
        userAndPass = {'USER': self.user,'PASS': self.password}
        data = urllib.parse.urlencode(userAndPass).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/StartSession/",data,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                if len(doc.getElementsByTagName("SessionID")) > 0:
                    self.SessionID = doc.firstChild.firstChild.firstChild.nodeValue
                    self.getExecResponse()
                else:
                    raise Exception("Unable to create session")
        except:
            raise
    def exec(self,command=""):
        comm = {'ID':str(self.SessionID),'COMMAND':command}
        UserCommand = urllib.parse.urlencode(comm).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/SessionCommand/",UserCommand,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml(indent='    ')
        except:
            raise
    def getExecResponse(self):
        request = urllib.request.Request(f"{self.url}:{self.port}/ReadResponses/{self.SessionID}",method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml('    ')
        except:
            raise
    def keepAlive(self,timeSpan):
        keepalive = True
        exit = Event()
        def sleep(timeSpan):
            nonlocal exit
            exit.wait(timeSpan)
        def stopLoop(signum,frame):
            nonlocal keepalive
            keepalive = False
            exit.set()
        signal.signal(signal.SIGTERM,stopLoop)
        while keepalive:
            try:
                self.exec("")
            except HTTPError:
                self.connect()
            except:
                raise
            sleep(timeSpan)
    def __del__(self):
        comm = {'ID':str(self.SessionID)}
        data = urllib.parse.urlencode(comm).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/CloseSession/",data,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml('    ')
        except:
            raise