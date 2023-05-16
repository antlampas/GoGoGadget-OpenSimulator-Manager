/*
Author: antlampas
Date: 2022-12-07
This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
*/

/* TODO: test and debug */

CREATE TABLE Grids (
    GridName varchar(128) NOT NULL,
    GridPath varchar(256) NOT NULL,
    PRIMARY KEY(GridName)
);
CREATE TABLE 'ROBUST Services' (
    Grid varchar(128) REFERENCES Grids(Name),
    ServiceName varchar(128) NOT NULL,
    ServicePath varchar(256) NOT NULL,
    PRIMARY KEY(Grid,ServiceName),
    FOREIGN KEY(Grid) REFERENCES Grids(ServiceName)
);
CREATE TABLE Simulators (
    Grid varchar(128) NOT NULL,
    SimulatorName varchar(128) NOT NULL,
    SimulatorPath varchar(256) NOT NULL,
    PRIMARY KEY(Grid,SimulatorName),
    FOREIGN KEY(Grid) REFERENCES Grids(GridName)
);
CREATE TABLE Estates (
    Grid varchar(128) NOT NULL,
    Simulator varchar(128) NOT NULL,
    EstateName varchar(128) NOT NULL,
    EstateOwner varchar(128) NOT NULL,
    PRIMARY KEY(Grid,Simulator,EstateName),
    FOREIGN KEY(Grid) REFERENCES Grids(EstateName),
    FOREIGN KEY(Simulator) REFERENCES Simulators(EstateName)
);
CREATE TABLE Regions (
    Grid varchar(128) NOT NULL,
    Simulator varchar(128) NOT NULL,
    Estate varchar(128) NOT NULL,
    RegionName varchar(128) NOT NULL,
    PRIMARY KEY(Grid,Simulator,Estate,RegionName),
    FOREIGN KEY(Grid) REFERENCES Grids(GridName),
    FOREIGN KEY(Simulator) REFERENCES Simulators(Name),
    FOREIGN KEY(Estate) REFERENCES Estates(Name)
);
CREAtE TABLE Backups (
    BackupType varchar(24),
    BackupPath varchar(256),
    PRIMARY KEY(BackupType),
    UNIQUE(BackupPath)
);