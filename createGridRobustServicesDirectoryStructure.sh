#!/bin/bash

#Author: Red Erik @ OSGrid
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

gridBasePath="${1}"

if [ -e ${gridBasePath} ]
then
    if [ -d ${gridBasePath} ]
    then
        robustServiceNames=()
        for i in ${@:2}
        do
            if [ ${i} =~ ^[[:alnum]]$ ]
            then
                robustServiceNames+=(${i})
            else
                echo "${i} is not a valid name"
            fi
        done
        if [ "${#robustServiceNames[@]}" ]
        then
            for robustServiceName in ${robustServiceNames[@]}
            do
                if [ $( mkdir ${gridBasePath}/robust/${robustServiceName} ) ]
                then
                    echo "${gridBasePath}/${robustServiceName} created"
                else

                    echo "${gridBasePath}/${robustServiceName} not created" >&2
                fi
            done
        else
            echo "No valid robust service name given"
            exit 3
        fi
    else
        echo "${gridBasePath} is not a directory"
        exit 2
    fi
else
    echo "${gridBasePath} doesn't exists"
    exit 1
fi
