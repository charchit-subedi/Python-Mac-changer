#!/usr/bin/env python
import subprocess

interface = "wlan0"
new_mac = "00:55:89:46:97:56"

print("[+] changing MAC Address for "+interface+" to "+new_mac)
subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
