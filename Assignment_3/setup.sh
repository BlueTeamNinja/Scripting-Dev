#!/bin/bash
wget https://github.com/PowerShell/PowerShell/releases/download/v7.3.7/powershell_7.3.7-1.deb_amd64.deb -O ./ps7.deb
dpkg -i ./ps7.deb
apt-get install -f
