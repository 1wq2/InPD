import os
import subprocess
import re

subprocess.call("sudo hdparm -I /dev/sda > " + os.getcwd() + "/log.txt", shell=True)
logfile = open(os.getcwd() + "/log.txt")

dictianory.update(tempDict)

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getcwd() + "/log.txt")
os.remove(path)
