#!/usr/bin/env python3
import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:36:96:56:78:45", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
