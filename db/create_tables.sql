/*
Author: antlampas
Date: 2022-12-07
This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
*/

CREATE TABLE Backups (Type varchar(24), Path varchar(256), PRIMARY KEY(Type), UNIQUE(Path));
CREATE TABLE Estates (Grid varchar(128) NOT NULL, Simulator varchar(128) NOT NULL, Name varchar(128) NOT NULL, Owner varchar(128) NOT NULL, PRIMARY KEY(Grid,Simulator,Name), FOREIGN KEY(Grid) REFERENCES Grids(Name), FOREIGN KEY(Simulator) REFERENCES Simulators(Name));
CREATE TABLE Grids (Name varchar(128) NOT NULL, 'Base Path' varchar(256) NOT NULL,PRIMARY KEY(Name), UNIQUE('Base Path'));
CREATE TABLE 'ROBUST Services' (Grid varchar(128) REFERENCES Grids(Name), Name varchar(128) NOT NULL, Path varchar(256) NOT NULL, PRIMARY KEY(Grid,Name),FOREIGN KEY(Grid) REFERENCES Grids(Name));
CREATE TABLE Regions (Grid varchar(128) NOT NULL, Simulator varchar(128) NOT NULL, Estate varchar(128) NOT NULL, Name varchar(128) NOT NULL, PRIMARY KEY(Grid,Simulator,Estate,Name), FOREIGN KEY(Grid) REFERENCES Grids(Name), FOREIGN KEY(Simulator) REFERENCES Simulators(Name), FOREIGN KEY(Estate) REFERENCES Estates(Name));
CREATE TABLE Simulators (Grid varchar(128) NOT NULL, Name varchar(128) NOT NULL, Path varchar(256) NOT NULL, PRIMARY KEY(Grid,Name), FOREIGN KEY(Grid) REFERENCES Grids(Name));