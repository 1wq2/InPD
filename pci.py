import os
import subprocess

subprocess.call("lspci -mmnn > " + os.getcwd() + "/log.txt", shell=True)
log = open(os.getcwd() + "/log.txt")

