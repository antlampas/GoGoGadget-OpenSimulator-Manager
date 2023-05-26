#Author: antlampas
#Date: 2023-02-08
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import dbManager

class localDB:
    def __init__(self):
        """Database Manager

        This class manages the GoGo Gadget OpenSimulator Manager internal database,
        needed to track all registered Grids and Simulator.
        
        The internal database is meant to simplify the tracking of all the data
        about the Grids and Simulators, such as Grids names, Grids paths, Grids
        administrators usernames, Simulators names, Simulators paths, Simulators
        owners usernames, Simulator-Grid binds.
        """
        pass