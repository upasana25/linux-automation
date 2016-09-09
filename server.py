#!/usr/bin/python

import os,time

def server():

	#os.system('dialog --menu "select your choice" 20 60 6 1 "whether host is rechable or not" 2 "display current network interfaces" 3 "assign a new IP" 4 "restore IP" 5 "configure particular interface" 6 "list hostname of the system" 2>/tmp/ch.txt')

	f=open('/tmp/ch.txt')
	ch=f.read()
	f.close()
	
	if ch == '1':
		os.system('dialog --inputbox "enter name or IP of the host" 10 40 2> /tmp/input.txt')
		f=open('/tmp/input.txt')
		input=f.read()
		f.close()

		e=os.system('ping -c 2 '+input)
		if e == 0:
			os.system('dialog --msgbox "host is reachable !!" 10 20')
		else :
			os.system('dialog --msgbox "host is unreachable --" 10 30')
		execfile('server_menu.py')
	
	elif ch == '2':
		os.system('ifconfig > /tmp/output.txt')#command for check system ip address
		os.system('dialog --textbox /tmp/output.txt 50 90')
		execfile('server_menu.py')
	
	elif ch == '3':
		os.system('dialog --inputbox "enter new ip which you want to assign :-" 10 40 2>/tmp/output.txt')		
		f=open('/tmp/output.txt')
		ip=f.read()
		f.close()		
		t=os.system('ifconfig  enp0s3 '+ip) #command to assign new ip
		if t != 0:
			os.system('ifconfig br0 '+ip)
		os.system('dialog --msgbox "assigned -- " 10 20')
		execfile('server_menu.py')
	
	elif ch == '4':
		t=os.system('dhclient -v enp0s3 > /tmp/output.txt')
		if t != 0 :
			os.system('dialog --msgbox "already running .. !!" 10 30')
		
		else :
			os.system('dialog --msgbox "done !!!!" 10 20')
		execfile('server_menu.py')
	
	elif ch == '5':
		t=os.system('ifconfig enp0s3 > /tmp/output.txt')
		if t != 0 :
			os.system('ifconfig enp0s3 > /tmp/output.txt')
		os.system('dialog --textbox /tmp/output.txt 20 70')
		execfile('server_menu.py')

	elif ch == '6':
		os.system('hostname -s > /tmp/output.txt')
		os.system('dialog --textbox /tmp/output.txt 10 20')
		execfile('server_menu.py')
	
	else :
		os.system('dialog --infobox "wrong choice !!" 10 20')
		time.sleep(1)
	
		os.system('dialog --menu "chose any one :-" 20 50 3 1 "exit" 2 "back to the menu" 3 "back to network management" 2>/tmp/ch.txt')
		f=open('/tmp/ch.txt')
		ch=f.read()
		f.close()

		if ch == '2':
			execfile('menu.py')

		elif ch == '3':
			execfile('server_menu.py')
		else :
			os.system('exit')

server()		
