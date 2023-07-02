#!/usr/bin/env python3
import subprocess

interface = input("Please input interface name > ")
new_mac = input("Please input NEW MAC Address >")

print("[+] changing MAC Address for "+interface+" to "+new_mac)

subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
