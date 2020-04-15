#!/usr/bin/env python

import subprocess
import optparse
import re


def get_argument():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="Give the interface to change is mac address")
    parse.add_option("-m", "--new_mac", dest="new_address", help="Give the mac address")
    (options2, arguments) = parse.parse_args()
    if not options2.interface:
        parse.error("[-] please enter a interface -h for more infos")
    elif not options2.new_address:
        parse.error("[-] please enter a interface -h for more infos")
    else:
        return options2


def change_mac(interface, new_address):
    print("[+]changing the mac address of this " + interface + " to this new mac address " + new_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-]the interface don't have a mac address");


options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current MAc = " + str(current_mac))
if current_mac:
    change_mac(options.interface, options.new_address)
    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_address:
        print("[+]Mac change correctly")
    else:
        print("[-]Mac not change")

else:
    print("[-]can not change mac of the interface")

