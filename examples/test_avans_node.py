#!/usr/bin/env python

#######################################################################################################################
# AVANS - BLOCKCHAIN - MINOR MAD                                                                                      #
#                                                                                                                     #
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# Example python script to show the working principle of the TcpServerNode Node class.                                #
#######################################################################################################################

import time
import sys

from AvansNode import AvansNode
from argparse import ArgumentParser
node = None # global variable
parser = ArgumentParser()
parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
args = parser.parse_args()
port = args.port
# Default configuration
host = '127.0.0.1'

if ( len(sys.argv) > 2 ):
    host = sys.argv[1]
    port = int(sys.argv[2])

print("Starting node on host " + host + " listening on port " + str(port))

node = AvansNode(host, port)
node.enable_visuals()

node.start()

time.sleep(1)

print("Node started.")

running = True
while running:
    print("Commands: connect, ping, discovery, stop")
    s = input("Please type a command:") # python 2.x
    if ( s == "stop" ):
        running = False

    if ( s == "connect"):
        # host = input("host: ")
        host = "127.0.0.1"

        port = int(input("port: "))
        node.connect_with_node(host, port)

    elif ( s == "ping" ):
        node.send_ping()

    elif ( s == "discovery" ):
        node.send_discovery()

    else:
        print("Command not understood '" + s + "'")
            

print("main stopped")

node.stop()

