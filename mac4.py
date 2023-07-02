#!/usr/bin/env python3
import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing the Mac address of "+interface+", to "+new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Input the Name of interface")
parser.add_option("-m", "--mac", dest="new_mac", help="Input New MAC address")


(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)


