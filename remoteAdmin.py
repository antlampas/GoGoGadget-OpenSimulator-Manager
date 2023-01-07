#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import xmlrpc.client
from datetime import date

class remoteAdmin:
    def __init__(self,address="127.0.0.1",port="8002",https=False):
        self.address      = address
        self.port         = port
        if not https:
            self.protocol = "http://"
        else:
            self.protocol = "https://"
        self.https        = https
        self.url          = self.protocol+self.address+":"+self.port+"/"
        self.simulator    = xmlrpc.client.ServerProxy(self.url)
    def command(self,command,parameters):
        comm = getattr(self.simulator,str(command))(parameters)
        return comm
