#!/bin/bash

#Author: antlampas
#Date: 2022-12-07
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

#backupConfig.sh [simulatorPath] [BaseBackupPath]
#[simulatorPath]:  this is exactly what's meant to be: if your simulator is in /simulators/simulator1, [simulatorPath] is exactly /simulators/simulator1
#[BaseBackupPath]: is the base directory of all the backups. e.g. if simulators backups are in /backups/simulator1, /backup/simulator2, etc, [BaseBackupPath] is /backup

if [ $# -eq 2 ]
then
    simulatorPath="$( echo ${1} | tr -s '/' )"
    backupPath="$( echo ${2} | tr -s '/' )"

    if [ -e $simulatorPath ] && [ -e $backupPath ] &&  [ -d $simulatorPath ] && [ -d $backupPath ]
    then
        if [ ! -d ${simulatorPath} ]
        then
            echo "Directory "${simulatorPath}" doesn't exist"
            exit 2
        fi

        if [ ! -d ${simulatorPath}/bin ] || [ ! -d ${simulatorPath}/bin/Regions ]
        then
            echo "The \"/bin\" directory or the \"Regions\" directory not found."
            echo "Maybe wrong simulator directory?"
            exit 3
        fi

        simulatorName=$(echo $simulatorPath | rev | cut -d"/" -f2 | rev)

        configInclude="${simulatorPath}/bin/OpenSim.ini ${simulatorPath}/bin/config-include/FlotsamCache.ini ${simulatorPath}/bin/config-include/GridCommon.ini"
        regionsini=$(ls ${simulatorPath}/bin/Regions/ | grep "ini$")

        regionsiniPathsArray=()
        backupRegionsiniPathsArray=()

        for i in $regionsini
        do
            regionsiniPathsArray+=(${simulatorPath}/bin/Regions/${i})
            backupRegionsiniPathsArray+=(${backupPath}/${simulatorName}/bin/Regions/${i})
        done
        regionsiniPaths=""
        backupRegionsiniPaths=""
        for i in ${regionsiniPathsArray[@]};
        do
            regionsiniPaths+=${i}" ";
        done;

        for i in ${backupRegionsiniPathsArray[@]};
        do
            backupRegionsiniPaths+=${i}" ";
        done;

        if [ ! -d $backupPath/$simulatorName ]
        then
            [ ! -d $backupPath ] && mkdir $backupPath
            mkdir -p $backupPath/$simulatorName/bin/config-include $backupPath/$simulatorName/bin/Regions
            cp -rvf --parents $configInclude $regionsiniPaths $backupPath
        else
            mv -vf $backupPath/$simulatorName $backupPath/${simulatorName}-old
            cp -rvf --parents $configInclude $regionsiniPaths $backupPath
        fi
    else
        echo "Simulator path and/or backup path don't exist or is not a directory"
        exit 2
    fi
else
    echo "Wrong number of arguments"
    exit 1
fi
