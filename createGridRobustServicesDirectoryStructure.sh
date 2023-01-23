#!/bin/bash

#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

gridBasePath="${1}"

robustServiceNames=()
invalidNames=()

if [[ $# -gt 1 ]]
then
    if [ -e ${gridBasePath} ]
    then
        if [ -d ${gridBasePath} ]
        then
            for i in ${@:2}
            do
                if [[ ! ${i} =~ ^[[:alnum]]$ ]]
                then
                    robustServiceNames+=(${i})
                else
                    echo "${i} is not a valid name"
                    invalidNames+=(${i})
                fi
            done
            if [[ ${#robustServiceNames[@]} -gt 0 ]]
            then
                for robustServiceName in ${robustServiceNames[@]}
                do
                    if mkdir -p ${gridBasePath}/robust/${robustServiceName}
                    then
                        echo "${gridBasePath}/${robustServiceName} created"
                    else
                        echo "${gridBasePath}/${robustServiceName} not created" >&2
                    fi
                done
            else
                echo "No valid robust service name given..."
                for i in ${invalidNames[@]}
                do
                    echo "${i}"
                done
                exit 3
            fi
            if [[ ${#invalidNames[@]} -gt 0 ]]
            then
                echo "The following services directories have not been created due invalid name:"
                for i in ${invalidNames[@]}
                do
                    echo "${i}"
                done
            fi
            exit 0
        else
            echo "${gridBasePath} is not a directory"
            exit 2
        fi
    else
        echo "${gridBasePath} doesn't exists"
        exit 1
    fi
elif [[ $# -eq 1 ]]
then
    if [ -e ${gridBasePath} ]
    then
        if [ -d ${gridBasePath} ]
        then
            if mkdir -p ${gridBasePath}/robust/robust
                    then
                        echo "${gridBasePath}/${robustServiceName} created"
                    else

                        echo "${gridBasePath}/${robustServiceName} not created" >&2
                    fi
        else
            echo "${gridBasePath} is not a directory"
            exit 2
        fi
    else
        echo "${gridBasePath} doesn't exists"
        exit 1
    fi
else
    echo "Wrong Number of arguments"
    echo "Expecting:"
    echo "\"GridBasePath\" \"ServiceName\" ... \"ServiceNameN\""
    echo "or"
    echo "\"GridBasePath\""
    echo
    exit 1
fi
