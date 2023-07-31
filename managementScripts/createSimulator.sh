#!/bin/bash

#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

#NOTE: I wrote this script in Bash more as an exercise than as an actual need
#TODO: Rewrite this script in Python

#1) [OPENSIMULATORRELEASEPATH]
#2) [OPENSIMULATORINSTALLPATH
#2) [GRIDNAME]
#3) [SIMULATORNAME]

if [ $# -eq 4 ]
then
    OSReleasePath="${1}"
    OSInstallBasePath="${2}"
    gridName="${3}"
    simulatorName="${4}"

    if id -u ${simulatorName} &> /dev/null
    then
        userExists=true
    else
        echo "Simulator Operator doesn't exists. Please create a Simulator Operator account first" >&2
        exit 1
    fi

    if [ -e ${OSReleasePath} ] && [ -d ${OSReleasePath} ]
    then
        OSReleasePathExists=true
    else
        echo "OpenSimulator base path doesn't exist. Please, create the OpenSimulator base path first" >&2
        exit 2
    fi

    if [ -e ${OSInstallBasePath} ] && [ -d ${OSInstallBasePath} ]
    then
        OSInstallBasePathExists=true
    else
        echo "OpenSimulator base path doesn't exist. Please, create the OpenSimulator base path first" >&2
        exit 2
    fi

    if [ ${OSInstallBasePathExists} ] && [ -e ${OSInstallBasePath}/${gridName} ] && [ -d ${OSInstallBasePath}/${gridName} ]
    then
        gridPathExists=true
    else
        echo "Grid path doesn't exist or is not a directory. Please, create Grid path first" >&2
        exit 2
    fi

    if [ ${OSInstallBasePathExists} ] &&  [ -e ${OSInstallBasePath}/${gridName}/${simulatorName} ] && [ -d ${OSInstallBasePath}/${gridName}/${simulatorName} ]
    then
        simulatorPathExists=true
    else
        echo "Simulator path doesn't exist or is not a directory. Please, create Simulator path first" >&2
        exit 2
    fi

    if [[ $userExists && $OSReleasePathExists && $OSInstallBasePathExists && $gridPathExists && $simulatorPathExists ]]
    then
        cp ${OSReleasePath}/* ${OSInstallBasePath}/${gridName}/${simulatorName}/
        echo "Simulator created"
    else
        echo "Something went wrong. Check if Simulator Account and needed paths exist" >&2
    fi
else
     echo "Wrong number of arguments" >&2
     exit 1
fi
