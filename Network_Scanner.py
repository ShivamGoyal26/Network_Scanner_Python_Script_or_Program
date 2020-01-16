#!/usr/bin/env python

import scapy.all as scapy
# here for this we need to import the module with the name scapy.all here we gave the new new to the scapy.all using the as which is scapy

# def scan(ip):
#     scapy.arping(ip)    # here the arping is the function which is usually does all the work for us using the ARP Protocol for each ip range passed to the function
#
# scan("10.0.2.1/24")
# here we will not use this method, because it works automatically but here we will make a new one by our own

# def scan(ip):
#     arp_request = scapy.ARP(pdst = ip)  # we are making the object of the class ARP with the name arp_request # here technically we are making ARP request that can ask from the other devices that who has the (your given ip address)
#     print(arp_request.summary())  # It will give the details to us like how ARP Sends the packets to all other devices
#     # here we have the output something like that (ARP who has 10.0.2.23 says 10.0.2.20) it means we have successfully made the packets here it is saying to all the devices who has 10.0.2.20 ip address and return value to 10.0.2.20 which is ip of our system
#     # scapy.ls(scapy.ARP())  # Here this will show us the details of the ARP() class like what type of arguments ARP() accepts
#
# scan("10.0.2.23")

# here we have succesfully created the who has given ip but here the next problem is that now we have to send this request to each device which is connected
# to our network so lets see

# in order to do this we have to use the ether framwork because as we know data is sent with the help of the mac address in the network
# lets create an ethernet frame first it is similary to the ARP request that we have created

# def scan(ip):
#     arp_request = scapy.ARP(pdst = ip)
#     broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")   # here we are making the ether framwork here we need to set the destination mac address as we know data is sent in the form of the mac address thats why we have to give the destination mac so that the other devices can sent their own detials to our machine
    # here we will send the boradcast mac address which is the virtually mac address it does not exists in real and here the benefit is that when we sent this broadcast mac address then it will send to all the devices connected in the same network
    # which is ff:ff:ff:ff:ff:ff
    # print(broadcast.summary())  # lets see what it will show to us
    #
    # here it will us this output (08:00:27:33:75:72 > ff:ff:ff:ff:ff:ff (0x9000)) its gonna be send a ethernet packet from 08:00:27:33:75:72 which is the mac address of our to the broadcast mac address
# now we have to combine both packests which is ethernet and the ARP packet
#     arp_request_broadcast = broadcast / arp_request
#     arp_request_broadcast.show()  # this will show us the more detail then the summary() function
# scan("10.0.2.3")


# upto here our first step is complete which is created a packet that is directed to the broadcast Mac address so that i can be send to all clients in the same network
# and asks for the specific ip whatever we asked in the ip variable



# the next step is to send the packets in the network and wait for the responese


# def scan(ip):
#     arp_request = scapy.ARP(pdst = ip)
#     broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast / arp_request
#     # print(broadcast.summary())
#     # now scapy has the function called srp(name of the packet which we want to send) this function allows us to send the packets with the custom ether part in the network and recieve the response
# # here it will return us more than one information which is here we stored in the two variables answered and non-answered in the form of list
# # now here we didn't give the address to this here we just asked to send it but not mentioned where to send but here we have already passed the dstination address in the boradcast variable means now it will send the packed to the dest mac address which is ff:ff:ff:ff:ff:ff and now this will boradcast the packet to other clients
# # if you dont want to send the packet to the broadcast mac you can use the mac of that client where you wanna send this packet
#     answered, unanswered = scapy.srp(arp_request_broadcast, timeout =1)
#     print(answered.summary()) # see the output you will get everything
# scan("10.0.2.1/24")


def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    # it has the list answered and noo-answered
    # further answered_list has also the two list which is packets, answers
    print("IP\t\t\tMAC Address\n---------------------------------------------------------------------------------------")
    for element in answered_list:

        print(element[1].psrc + "\t\t" + element[1].hwsrc)  # ip address of the client


scan("10.0.2.1/24")