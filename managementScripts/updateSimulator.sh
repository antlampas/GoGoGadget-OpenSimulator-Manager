#!/bin/bash

#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

#NOTE: I wrote this script in Bash more as an exercise than as an actual need
#TODO: Rewrite this script in Python

#Arguments:
#1) New version path
#2) Base Grid Path
#3) Grid Name
#4) Simulator Name

if [ $# -lt 4 ]
then
    echo "Grid name or simulator name or path to new version is missing..."
    exit 1
elif [ $# -eq 4 ]
then
    newVersionPath="$( echo ${1} | tr -s '/' )"
    baseGridPath="$( echo ${2} | tr -s '/' )"
    gridName="${3}"
    simulatorName="${4}"

    gridPath="$( echo "${baseGridPath}/${gridName}" | tr -s '/')"
    simulatorPath="$( echo "${gridPath}/${simulatorName}" | tr -s '/')"

    if [ -e $newVersionPath ]
    then
        if [ -d $newVersionPath ]
        then
            if [ -e $gridPath ]
            then
                if [ -d $gridPath ]
                then
                    rm -rvf ${simulatorPath}/*
                    cp -rvf ${newVersionPath}/* ${simulatorPath}/
                else
                    echo "New version path isn't a directory"
                    exit 4
                fi
            else
                echo "Grid path doesn't exist"
                exit 3
            fi
        else
            echo "New version path isn't a directory"
            exit 4
        fi
    else
        echo "New version path doesn't exist"
        exit 3
    fi
else
    echo "Too many arguments"
    exit 2
fi
