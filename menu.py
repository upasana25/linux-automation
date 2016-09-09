#!/usr/bin/python

import os,time,sys,commands

def menu():
	os.system('dialog --menu "Select your choice" 20 50 3 1 "Basic Linux" 2 "Hard Disk Management & RAM" 3 "Network Management" 2>/tmp/ch.txt')
	#reading choice
	f=open('/tmp/ch.txt')
	ch=f.read()
	f.close()

	if ch=='1':
		execfile('basic_menu.py')
	elif ch=='2':
		execfile('hdisk_menu.py')
	elif ch=='3':
		execfile('server_menu.py')
	else:
		os.system('dialog --infobox " Wrong Choice !!" 10 30')
		time.sleep(1)
		os.system('dialog --menu "chose any one :-" 20 50 2 1 "exit" 2 "back to the menu" 2>/tmp/ch.txt')
		f=open('/tmp/ch.txt')
		ch=f.read()
		f.close()

		if ch == '2':
			menu()
		else :
			os.system('exit')


menu()	
