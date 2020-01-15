#!/usr/bin/env python

import scapy.all as scapy
# here for this we need to import the module with the name scapy.all here we gave the new new to the scapy.all using the as which is scapy

def scan(ip):
    scapy.arping(ip)    # here the arping is the function which is usually does all the work for us using the ARP Protocol 

scan("10.0.2.20")