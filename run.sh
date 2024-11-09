#!/bin/bash

# This is the order:
# 1) Network interface, 2) RAM Allocation, 3) testing file location

if [ $# -ge 3 ]; then
    # See whether we need network access or not.
    if [ "$1" != "no" ]; then
        firejail --noprofile --net=$1 --rlimit-as=$2 python main.py --file $3 --network_status yes
    else
        firejail --noprofile --net=none --rlimit-as=$2 python main.py --file $3
    fi
else
    echo "Not enough arguments"
fi
