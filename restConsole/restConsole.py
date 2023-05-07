#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import urllib.request
import urllib.parse
import defusedxml.minidom
import sys
import signal

from threading import Event

class restConsole:
    """REST Console interface
    
    Exposes the REST Console interface and simplifies the the interaction

    REST Console Reference: http://opensimulator.org/wiki/RestConsole
    """
    def __init__(self,user="",password="",url="http://127.0.0.1/",port="11000"):
        """Constructor

        user = is the REST Console username set in OpenSim.ini
        password = is the REST Console password set in OpenSim.ini
        url = is REST Console URL, including the protocol and the tailing slash
        port = is the REST Console port set in OpenSim.ini

        Gets the REST Console connection info and starts the session
        """
        self.url      = url
        self.port     = port
        self.user     = user
        self.password = password

        self.connect()
    def connect(self):
        """REST Console Connect

        Starts the REST Console Session
        """
        data = urllib.parse.urlencode({'USER': self.user,'PASS': self.password}).encode('ascii')
        request = urllib.request.Request(f"{self.url}:{self.port}/StartSession/",data,method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                if len(doc.getElementsByTagName("SessionID")) > 0:
                    self.SessionID = doc.firstChild.firstChild.firstChild.nodeValue
                    self.getExecResponse()
                else:
                    raise Exception("Unable to create session: Session ID not found")
        except:
            raise
    def exec(self,command=""):
        """REST Console Exec

        Sends the required command to the started REST Console
        """
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
        """REST Console Request Response

        Queries the REST Console for every response
        """
        request = urllib.request.Request(f"{self.url}:{self.port}/ReadResponses/{self.SessionID}",method='POST')
        try:
            with urllib.request.urlopen(request) as response:
                string = response.read()
                doc = defusedxml.minidom.parseString(string)
                return doc.toprettyxml('    ')
        except:
            raise
    def __del__(self):
        """REST Console Distructor

        Quits the REST Console
        """
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