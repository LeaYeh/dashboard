#!/bin/bash

if [ "$1" == "dev" ]; then
    docker-compose -f dev-docker-compose.yaml up --build -d
elif [ "$1" == "dashboard" ]; then
    docker-compose -f dashboard-docker-compose.yaml up --build -d 
else
    echo "Invalid command. Use 'run dev' or 'run dashboard'"
fi
