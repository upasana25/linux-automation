#!/usr/bin/python
import os
def hdisk():
	os.system('dialog --menu "select your choice" 20 60 6 1 "view partions of hardisk" 2 "view partions like file system" 3 "view used and free amount of RAM" 4 "list mounted file system" 5 "list all storage blocks" 6 "shoe low and high memory statistics of RAM" 2>/tmp/ch.txt')
	execfile('hdisk.py')

hdisk()
