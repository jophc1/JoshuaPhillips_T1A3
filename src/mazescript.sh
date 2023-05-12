#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Python3 not installed and is needed for this program. For a guide to install Python3 
    please go to https://wiki.python.org/moin/BeginnersGuide/Download' >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py $1
deactivate

