#!/bin/bash

#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, C>

gridBasePath="$( echo "${1}/" | tr -s '/' )"
gridName="${2}"
simulatorName="${3}"

if [[ ! -e $gridBasePath ]]
then
    echo "The grid base path provided doesn't exist or is incorrect"
    exit 1
fi
if [[ ! -d $gridBasePath ]]
then
    echo "The grid base path provided isn't a directory"
    exit 2
fi
if [[ ! $simulatorName =~ ^[[:alnum:]]+$ ]]
then
    echo "Invalid simulator name"
    exit 1
fi

tmux_pid=$( pgrep tmux -G $simulatorName )

if [[ -z $tmux_pid ]]
then
    tmux start-server
    tmux new-session -d -s ${gridName} -n ${simulatorName} "cd ${gridBasePath}/simulators/${simulatorName}/bin && ./opensim.sh"
    PID=$( pgrep tmux -U $simulatorName )
    touch /tmp/${simulatorName}.pid
    echo ${PID} > /tmp/${simulatorName}.pid
    exit 0
else
    echo "Simulator start failed..."
    exit 1
fi
