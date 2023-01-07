#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import urllib.request
import urllib.parse
import defusedxml.minidom
import sys

from time import sleep

class restConsole:
    SessionID = 0
    def __init__(self,user="",password="",url="http://127.0.0.1/",port="11000"):
        self.url    = url
        self.port   = port

        userAndPass = {'USER': user,'PASS': password}
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
        except Exception as e:
            raise
    def exec(self,command):
        comm = {'ID':str(self.SessionID),'COMMAND':command}
        UserCommand = urllib.parse.urlencode(comm).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/SessionCommand/",UserCommand,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml(indent='    ')
        except Exception as e:
            raise
    def getExecResponse(self):
        request = urllib.request.Request(f"{self.url}:{self.port}/ReadResponses/{self.SessionID}",method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml('    ')
        except Exception as e:
            raise
    def keepAlive(self):
        pass
    def __del__(self):
        comm = {'ID':str(self.SessionID)}
        data = urllib.parse.urlencode(comm).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/CloseSession/",data,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml('    ')
        except Exception as e:
            raise