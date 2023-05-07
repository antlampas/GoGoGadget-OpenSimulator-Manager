#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import xmlrpc.client
import signal

from datetime import date

class remoteAdmin:
    """Remote Admin interface

    Exposes OpenSimulator Remote Admin interface and simplifies the interaction

    Remote Admin reference: http://opensimulator.org/wiki/RemoteAdmin
    """
    def __init__(self,address="127.0.0.1",port="8002",https=False):
        """Constructor

        address = the IP address or domain name of the simulator
        port = the port the Remote Admin module is listening on
        https = tells if the simulator is running over https or not
        protocol = http or https
        url = Remote Admin full url
        simulator = actual Remote Admin client
        """
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
        """Command executor

        This is the method to be called to execute the intended Remote Admin command

        command = the command spelled according to the wiki page of the remote admin
        parameters = the parameters required by the command
        """
        try:
            comm = getattr(self.simulator,str(command))(parameters)
            return comm
        except:
            raise
