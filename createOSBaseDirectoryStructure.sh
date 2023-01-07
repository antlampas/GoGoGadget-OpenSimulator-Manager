#/bin/bash

#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

#Arguments:
#1) Grid Operator username
#2) GridName
#3) Path for bins
#4) Path for backups

if [[ $# -eq 4 ]]
then
    gridOperator="${1}"
    OSBasePaths=( "${2}" "${3}" "${4}" )
else
    echo "Wrong Number of arguments"
    echo "Expecting:"
    echo "\"GridOperatorUsername\" \"GridName\" \"BinPath\" \"BackupsPath\""
    echo
    exit 1
fi

for i in ${OSBasePaths[@]}
do
    if [[ $i =~ ^[[:alnum:]/]+$ ]]
    then
        if [[  ! -e "${i}"  ]]
        then
            if id "${gridOperator}" &> /dev/null
            then
                if [[ $( sudo -u "${gridOperator}" mkdir "${i}" ) ]]
                then
                    echo "${i} created"
                else
                    echo "${i} not created"
                fi
            else
                echo "Grid Operator doesn't exist. Please, create a Grid Operator account first"
                exit 4
            fi
        else
            echo "Directory already exists" >&2
            exit 3
        fi
    else
        echo "The path ${i} is malformed! Check it, please" >&2
        exit 2
    fi
done

exit 0
