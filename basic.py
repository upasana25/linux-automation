#!/usr/bin/python
import os,time,commands

def basic():

	#os.system('dialog --menu "select your choice" 20 50 6 1 "date" 2 "calendar" 3 "current location" 4 	"view any file text" 5 "time" 6 "view and edit any file" 2>/tmp/ch.txt')

	f=open('/tmp/ch.txt')
	ch=f.read()
	f.close()
	
	#output.txt is output file
	if ch == '1':
		os.system('date +%x > /tmp/output.txt')#for date command
		f=open('/tmp/output.txt')
		output=f.read()
		f.close()
		print output
		os.system('dialog  --msgbox  "'+output+'"  10 20')
		#os.system('dialog --textbox /tmp/output.txt 10 20')
		execfile('basic_menu.py')

	elif ch == '2':
		cal=commands.getoutput('cal') #for cal(calendar) command
		os.system('dialog --msgbox "calender of this month is :  \n'+cal+'"  20 40 ')
		execfile('basic_menu.py')

	elif ch == '3':
		path=commands.getoutput('pwd') #for pwd(current location) command
		os.system('dialog --msgbox '+path+' 10 20')
		execfile('basic_menu.py')
	
	elif ch == '4':
		os.system('dialog --inputbox "enter name/path of the file :" 10 20 2>/tmp/name')
		f=open('/tmp/name')
		name=f.read()
		f.close()
		os.system('dialog --textbox '+name+' 20 30')
		execfile('basic_menu.py')

	elif ch == '5':
		tym=commands.getoutput('date +%X') #displaying time 
		os.system('dialog --msgbox "'+tym+'" 10 20')
		execfile('basic_menu.py')

	elif ch == '6':
		os.system('dialog --inputbox "enter name/path of the file :" 10 20 2>/tmp/name.txt') #view and edit any file
		f=open('/tmp/name.txt')
		name=f.read()
		f.close()
		os.system('dialog --textbox '+name+' 20 40 2>/tmp/output.txt')

		f1=open(name,'a+')
		read1=f1.read()
	
		f2=open('/tmp/output.txt')
		read2=f2.read()
		f2.close()

		if read1 != read2 :
			f1.seek(0)
			f1.write(read2)
		execfile('basic_menu.py')

	else :
		os.system('dialog --infobox "wrong choice !!" 10 20')
		time.sleep(1)
	
		os.system('dialog --menu "chose any one :-" 20 50 3 1 "exit" 2 "back to the menu" 3 "back to the basic linux" 2>/tmp/ch.txt')
		f=open('/tmp/ch.txt')
		ch=f.read()
		f.close()

		if ch == '2':
			execfile('menu.py')

		elif ch == '3':
			execfile('basic_menu.py')
		else :
			os.system('exit')


basic()
