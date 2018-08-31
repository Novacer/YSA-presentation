#!/bin/bash

# This shell script is for running the frontend angular app

cd example-ui

cd angular-frontend

echo "Install node modules? (This will install everything in package.json)"
echo "This requires npm to be installed!"
echo "Type yes / no"

read install

if [ $install == "yes" ] || [ $install == "Yes" ] || [ $install == "y" ] || [ $install == "Y" ]
then
	echo "Installing dependencies"
	npm install
else
	echo "Skipping install of dependencies, but note that code won't work unless you set it up yourself."
fi

echo "Starting angular app"

npm start

cd ../../