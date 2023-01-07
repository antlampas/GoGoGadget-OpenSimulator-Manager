#!/bin/bash

#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

if [ $# -eq 4 ]
then
    backupPath="${1}"
    user="${2}"
    password="${3}"
    dbName="${4}"
elif [ $# -eq 3 ]
then
    backupPath="${1}"
    user="${2}"
    password="${3}"
else
    echo "Wrong number of arguments"
    echo "Expecting:"
    echo "\"username\" \"password\" \"databaseName\" \"backupPath\""
    echo
    exit 1
fi

if [ $( command -v mysqldump ) ]
then
    if [ "${dbName}" ]
    then
        mysqldump --no-tablespaces -u "${user}" -p"${password}" -r "${backupPath}"/"${dbName}"-$(date +%Y-%m-%d).sql --databases "${dbName}"
    else
        mysqldump --no-tablespaces -u "${user}" -p"${password}" -r "${backupPath}"/"${user}"-$(date +%Y-%m-%d).sql --databases "${user}"
    fi
else
    echo "Please install mysqldump"
    exit 2
fi
