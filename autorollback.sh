#!/bin/bash

while true; do
    current_commit=$(git rev-parse HEAD)
    echo $current_commit
    sleep 120
    new_commit=$(git rev-parse HEAD)
    echo $new_commit
    if [[($current_commit == $new_commit)]]; then
        echo "now reverted to previous commit"
    else
        echo "new commit detected, no action taken"
    fi
done