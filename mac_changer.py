#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change it MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

# subprocess.call("ifconfig" + interface + "down", shell=True)
# subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
# subprocess.call("ifconfig" + interface + "up", shell=True)

print("Changing MAC Address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])