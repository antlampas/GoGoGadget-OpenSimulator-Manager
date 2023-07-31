#!/bin/bash

# A temporary test console 

echo -n "REST configurations path (absolute path): "
read configPath
echo -n "Simulators: "
read -a SIMULATORS
echo -n "Password for sudo: "
read -s PASSWORD

tmux start-server
tmux new-session -d -s OSGrid -n HTOP htop
for i in ${SIMULATORS[@]}
do
    tmux new-window -t OSGrid -n "${i}" "sudo -u ${i} tmux attach"
    sleep 0.3
    tmux send-keys -t OSGrid:"${i}" "$PASSWORD" 'Enter'
    tmux splitw -t OSGrid:"${i}"
    sleep 0.3
    params=( $(awk -F'=' -v ORS=' ' '{print $2}' "${configPath}"/"${i}".conf) )
    tmux send-keys -t OSGrid:"${i}".1 'read -s changeDirectory' 'Enter'
    tmux send-keys -t OSGrid:"${i}".1 'cd /srv/opensimulator/managementScripts/' 'Enter'
    tmux send-keys -t OSGrid:"${i}".1 'read -s startRestPrompt' 'Enter'
    tmux send-keys -t OSGrid:"${i}".1 "sudo -u opensimulator python restPrompt.py ${params[2]} ${params[3]} http://${params[0]} ${params[1]}" 'Enter'
    tmux send-keys -t OSGrid:"${i}".1 '$changeDirectory' 'Enter'
    tmux send-keys -t OSGrid:"${i}".1 '$startRestPrompt' 'Enter'
    sleep 0.3
    tmux send-keys -t OSGrid:"${i}" "$PASSWORD" 'Enter'
done
tmux attach
