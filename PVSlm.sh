#!/bin/bash

# Make sure to copy this script in the PVS path

# Give write permission over bashrc
sudo chmod ugo+r ~/.bashrc

# Create an alias for the PVS path
sudo echo alias 'PVSPATH="'$PWD'"' >> ~/.bashrc

# Add an alias for the PVS Library Manager
sudo echo alias 'pvslm="python '$PWD'/LMPVS.py"' >> ~/.bashrc

# Install the bash
. ~/.bashrc


