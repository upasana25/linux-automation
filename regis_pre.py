#!/usr/bin/python
import os,time

# regis_pre is for matching passwd and user name of previously registered users

def reg_1():
	#this is for user name
	os.system('dialog --inputbox "ENTER USER NAME" 10 30 2>/tmp/user.txt')
	#this is for password 
	os.system('dialog --insecure --passwordbox "ENTER PASSWORD" 10 30 2>/tmp/pass.txt') 
	#reading user name and password
	f=open('/tmp/user.txt')
	u=f.read()
	f.close()
	f=open('/tmp/pass.txt')
	p=f.read()
	f.close()
	if u== 'linux'and p== 'redhat':
		execfile('menu.py')
	else:
		os.system('grep -i '+u+' user.txt > /tmp/output.txt')
		f1=open('/tmp/output.txt')
		a1=(f1.read()).split(':')
		tmp=a1[1].split('\n')
		#print a1[0]
		#print tmp
		
		os.system('grep '+tmp[0]+' passwd.txt > /tmp/input.txt')
		f2=open('/tmp/input.txt')
		a2=(f2.read()).split(':')
		#print a2
		#time.sleep(10)
		
		if a2[0] == p:
			execfile('menu.py')
		else:
			os.system('dialog --infobox "you have entered wrong username or password" 10 30')
			time.sleep(1)
			#os.system('dialog --msgbox "CLICK OK" 10 30')
			os.system('dialog --menu "now what !!" 20 50 2 1 "exit" 2 "back to the menu" 2>/tmp/ch.txt')
			f=open('/tmp/ch.txt')
			ch=f.read()
			f.close()
		
			if ch == '2':
				execfile('start.py')
			else :
				os.system('exit')


reg_1()
