#!/usr/bin/env python3

import subprocess

interface = input("please enter the interface name > ")
new_mac = input("please enter the New MAC address > ")

print("[+] changing the mac address of "+ interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
