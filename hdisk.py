#!/usr/bin/python
import os,time,sys,commands
def hdisk():
	#.system('dialog --menu "select your choice" 20 60 6 1 "view partions of hardisk" 2 "view partions like file system" 3 "view used and free amount of RAM" 4 "list mounted file system" 5 "list all storage blocks" 6 "shoe low and high memory statistics of RAM" 2>/tmp/ch.txt')

	f=open('/tmp/ch.txt')
	ch=f.read()
	f.close()

#op,txt is output file
	if ch == '1':
		os.system('fdisk -l /dev/sda > /tmp/output.txt') #view partition of hard disk
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	elif ch == '2':
		os.system('fdisk -l > /tmp/output.txt') #view partition like file system
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	elif ch == '3':
		os.system('free -h > /tmp/output.txt') #view used and free amount of RAM
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	elif ch == '4':
		os.system('df > /tmp/output.txt') #listed mouned file system
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	elif ch == '5':
		os.system('lsblk > /tmp/output.txt') #list all storage blocks
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	elif ch == '6':
		os.system('free -l > /tmp/output.txt') #shoe low and high memory statistics of RAM
		os.system('dialog --textbox /tmp/output.txt 20 50')
		execfile('hdisk_menu.py')

	else :
		os.system('dialog --infobox "wrong choice !!" 10 20')
		time.sleep(1)
	
		os.system('dialog --menu "chose any one :-" 20 50 3 1 "exit" 2 "back to the menu" 3 "back to the hardisk & RAM" 2>/tmp/ch.txt')
		f=open('/tmp/ch.txt')
		ch=f.read()
		f.close()

		if ch == '2':
			execfile('menu.py')

		elif ch == '3':
			execfile('hdisk_menu.py')
		else :
			exit()


hdisk()
