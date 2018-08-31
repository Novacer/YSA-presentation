#!/bin/bash

# This shell script is for running the backend flask API

echo "Install dependencies globally? (This will install everything in requirements.txt)"
echo "This requires pip to be installed!"
echo "Type yes / no"

read install

if [ $install == "yes" ] || [ $install == "Yes" ] || [ $install == "y" ] || [ $install == "Y" ]
then
	echo "Installing dependencies"
	pip install -r requirements.txt
else
	echo "Skipping install of dependencies, but note that code won't work unless you set it up yourself."
fi

cd example-code

echo "setting environment variables..."

export FLASK_APP=first_api.py

echo "running server..."

flask run

cd ..