#!/bin/bash

while true; do
    current_commit=$(git rev-parse HEAD)
    sleep 10
    new_commit=$(git rev-parse HEAD)

    if ["$current_commit" = "$new_commit"]; then
        echo "now reverted to previous commit"
    else
        echo "new commit detected, no action taken"
    fi
done