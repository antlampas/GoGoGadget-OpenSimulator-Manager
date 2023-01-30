#!/bin/bash

#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.


#recoverConfig.sh [BaseBackupPath] [simulatorPath]
#[BaseBackupPath]: is the base directory of all the backups. e.g. if simulators backups are in /backups/simulator1, /backup/simulator2, etc, [BaseBackupPath] is /backup
#[simulatorPath]: this is exactly what's meant to be: if your simulator is in /simulators/simulator1, [simulatorPath] is exactly /simulators/simulator1
#So, if you wanna restore the backup for the simulator1, you'll givethe command: recoverConfig backups /simulators/simulator1

if [ $# = 2 ]
then
    if [ ! $( command -v mv ) ]
    then
        echo "The \"mv\" command is not installed..."
        echo "Please install \"mv\""
    else
        echo "OK! \"mv\" is installed!"
    fi

    if [ ! $( command -v cp ) ]
    then
        echo "The \"cp\" command is not installed..."
        echo "Please install \"cp\""
    else
        echo "OK! \"cp\" is installed!"
    fi

    if [ ! -d "$1" ]
    then
        echo "Backup directory doesn't exist..."
        exit 2
    fi

    if [ ! -d "$2" ]
    then
        echo "Simulator directory doesn't exist..."
        exit 3
    fi

    backupPath="$( echo ${1} | tr -s '/' )"
    simulatorPath="$( echo ${2} | tr -s '/' )"
    simulatorName="$(echo $simulatorPath | rev | cut -d/ -f2 | rev)"

    if [ -d $backupPath/$simulatorName ]
    then
        cp -rvf $backupPath/$simulatorName/* $simulatorPath/
    else
        echo "No backup found..."
    fi
else
    echo "Wrong number of arguments..."
    exit 1
fi
