#!/usr/bin/python
import os

def basic():

	os.system('dialog --menu "select your choice" 20 50 6 1 "date" 2 "calendar" 3 "current location" 4 	"view any file text" 5 "time" 6 "view and edit any file" 2>/tmp/ch.txt')
	execfile('basic.py')

basic()
