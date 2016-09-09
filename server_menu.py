#!/usr/bin/python

import os

def server():

	os.system('dialog --menu "select your choice" 20 60 6 1 "whether host is rechable or not" 2 "display current network interfaces" 3 "assign a new IP" 4 "restore IP" 5 "configure particular interface" 6 "list hostname of the system" 2>/tmp/ch.txt')
	execfile('server.py')


server()
