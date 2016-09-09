#!/usr/bin/python
import os

def register():
	#this is for user name
	os.system('dialog --inputbox "ENTER YOUR USER NAME" 10 30 2>/tmp/user.txt')
	#this is for password 
	os.system('dialog --insecure --passwordbox "ENTER YOUR PASSWORD" 10 30 2>/tmp/pass.txt') 
	#reading user name and password

	f=open('/tmp/user.txt')
	u=f.read()
	f.close()
	f=open('/tmp/pass.txt')
	p=f.read()
	f.close()

	#saving user name and password

	f=open('user.txt','a')
	
	if u== 'linux'and p== 'redhat':
		execfile('menu.py')
	else :
		f1=open('user.txt','a+')
		f2=open('passwd.txt','a+')
		f2.read()
# read is list containing list of users with ID 
		read=(f1.read()).split('\n')
# i contain each element from read variable
		for i in read :
# var contain user and ID in list type ex; var = [user,ID]
			var = i.split(':')
			if var[0]==u and var[0]!='':
				os.system('dialog --msgbox "already exist" 10 20')
				time.sleep(1)
				exit()
		pre=read[-2]
		pre=pre.split(':')
		f1.write(u+':'+str(int(pre[1])+1))
		f2.write(p+':'+str(int(pre[1])+1))
		os.system('dialog --msgbox "registered sucessfully !!!!" 10 20')
		time.sleep(1)
		register()


register()
			
