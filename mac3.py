#!/usr/bin/env python3
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
parser.parse_args()
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] changing the mac for "+interface+" to  "+new_mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
