#!/bin/bash

if [ "$#" -ne 2 ]; then
    exit 1
fi

python3 AEE.py "$1" "$2"