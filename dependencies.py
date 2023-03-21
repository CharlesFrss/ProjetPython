import os
import sys
import subprocess
# Installation des dépendances nécessaires
os.system("sudo apt-get update")
os.system("sudo apt-get install nmap")
os.system("sudo apt-get install python3-pip")
subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
