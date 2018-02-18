import os
import sys
import random
import socket
import string
import difflib
import datetime
from nltk import *
from random import randint

dt=str(datetime.datetime.now().date())

def datenow(tokens):
	if "today" in tokens or "now" in tokens or "what" in tokens:
	    now = datetime.datetime.now()
	    
	    if str(datetime.datetime.now().day) is 1 or str(datetime.datetime.now().day) is 21 or str(datetime.datetime.now().day) is 31:
	        subscrit = "st"
	    
	    elif str(datetime.datetime.now().day) is 2 or str(datetime.datetime.now().day) is 22:
	        subscrit = "nd"
	    
	    else:
	        subscrit = "th"
	    
	    if now.month is 1:
	        month = "January"
	    
	    elif now.month is 2:
	        month = "February"
	    
	    else:
	        return
	    
	    print "Hazel : Today is ",str(datetime.datetime.now().day), subscrit," of", month,str(datetime.datetime.now().year) 
	
	else:
		ask = raw_input("Do you mean to get today's date?")
		
		if ask == 'y' or ask == 'yes' or ask == 'ya' or ask == 'yeah':
		    now = datetime.datetime.now()
		
		    if str(datetime.datetime.now().day) is 1 or str(datetime.datetime.now().day) is 21 or str(datetime.datetime.now().day) is 31:
		        subscrit = "st"
		
		    elif str(datetime.datetime.now().day) is 2 or str(datetime.datetime.now().day) is 22:
		        subscrit = "nd"
		
		    else:
		        subscrit = "th"
		
		    if now.month is 1:
		        month = "January"
		
		    elif now.month is 2:
		        month = "February"
		
		    else:
		        return
		
		    print "Hazel : Today is ",str(datetime.datetime.now().day), subscrit," of", month,str(datetime.datetime.now().year)
		
		else:
			return

def timenow(tokens):
	
	hr = datetime.datetime.now().strftime('%H')
	mn = datetime.datetime.now().strftime('%M')
	sec = datetime.datetime.now().strftime('%S')

	print "Hazel : The time is ", str(hr), ":", str(mn)


def adduser(tokens):
	choices = {1: "Create a user account with home directory", 2: "Create an administrator account with home directory", 0: "quit this menu"}
	for key, value in choices.items():
            print key, "- ", value
	ch = raw_input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
	#print ch

	if ch == '1':
		useracnt()
		return
	
	elif ch == '2':
		adminacnt()
		return
	
	elif ch == '0':
		return
	
	else:
		print "\n\n\nchoose an option from the below list : "
		adduser(tokens)


def useracnt():
	uname = raw_input("Set a new username for this user : ")
	if not os.system("sudo useradd -m "+ uname):
		print "Account for ", uname, "was succesfully created."
		password = raw_input("Type 'y' to set a new password or press enter to let me set a random password for you : ")
		
		if not password:
			passwd = password_generator()
		
		elif password.lower() == 'y':
			os.system("sudo passwd " + uname)
		
		else:
			return
		
		udetails = raw_input("Do you wish to edit personal details of this account? type 'y' or 'n' : ")
		
		if udetails.lower() == 'y':
			full_name = raw_input("Enter your full name : ")
			os.system("sudo chfn -f " + full_name + uname + " > temp")
			print uname, "was succesfully modified and ready to use"
			os.system("rm -rf temp")
		
		else:
			return

def adminacnt():
	uname = raw_input("Set a new username for the admin account : ")
	if not os.system("sudo useradd -m -G wheel "+ uname):
		print "Account for ", uname, "was succesfully created."
		password = raw_input("Type 'y' to set a new password or press enter to let me set a random password for you : ")
		
		if not password:
			passwd = password_generator()
		
		elif password.lower() == 'y':
			os.system("sudo passwd " + uname)
		
		else:
			return
		
		udetails = raw_input("Do you wish to edit personal details of this account? type 'y' or 'n' : ")
		if udetails.lower() == 'y':
			full_name = raw_input("Enter your full name : ")
			os.system("sudo chfn -f " + full_name + uname + " > temp")
			print uname, "was succesfully modified and ready to use"
			os.system("rm -rf temp")
		
		else:
			return

def password_generator():
	pas = randint(10, 99)
	pas1 = random.choice(string.ascii_lowercase)
	pas2 = random.choice(string.ascii_lowercase)
	pas3 = randint(10, 99)
	passwd = str(pas)+pas1+pas2+str(pas3)
	print "Your system password is ",passwd
	check = raw_input("Do you wish to try another?  ")
	
	if check.lower() == 'y':
		password_generator()
	
	else:
		return passwd



def deltuser(tokens):
	choices = {1: "remove user only", 2: "remove user with all its data", 0: "quit this menu"}
	for key, value in choices.items():
            print key, "- ", value
	ch = raw_input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
	#print ch

	if ch == '1':
		useacnt()
		return

	elif ch == '2':
		admnacnt()
		return
	
	elif ch == '0':
		return
	
	else:
		print "\n\n\nchoose an option from the below list : "
		adduser(tokens)

	if "create" in tokens:
		tokens.remove("create")
	
	if "new" in tokens:
		tokens.remove("new")
	
	if "user" in tokens:
		tokens.remove("user")
		useacnt()
	
	if "account" in tokens:
		tokens.remove("account")
	
	if "admin" in tokens:
		tokens.remove("admin")
		admnacnt()
	
	if "administrator" in tokens:
		tokens.remove("administrator")
		admnacnt()


def useacnt():
	uname = raw_input("Type the user name you want to delete : ")
	if not os.system("sudo userdel  "+ uname):
		print "Account for ", uname, "was succesfully deleted ."
		

def admnacnt():
	uname = raw_input("type user account you want to delete : ")
	if not os.system("sudo userdel -rf " + uname):
		print "Account for ", uname, "was succesfully deleted."


def chpasswd(tokens):
	choices = {1: "Change the user password", 2: "Change root password (not recommended for new users)", 0: "quit this menu"}
	for key, value in choices.items():
            print key, "- ", value
	ch = raw_input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
	
	if ch == '1':
		uname = raw_input("Enter the username you want to remove : ")
		os.system("sudo passwd " + uname)
	
	elif ch == '2':
		uname = raw_input("Enter the username you want to remove : ")
		os.system("sudo passwd " + uname)
	
	elif ch == '0':
		return
	
	else:
		return

def is_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        print 'Hazel : Your internet is connected.'
        return True

    except Exception,e:
        #print e
        print "Hazel : Your internet connection is off."
    return False


def speedtest():
    try:
        ch = raw_input("Shall I show the result in Bytes rather than in Bits (1 Bytes = 8 Bits; 128kBps ~ 1Mbps) : ")
        if ch.lower() == 'y' or ch.lower() == 'yes' or ch.lower() =='bytes' or ch.lower() == 'byte':
            os.system("speedtest --bytes --simple")
            return
        elif ch.lower() == 'n' or ch.lower() == 'no' or ch.lower() == 'bits' or ch.lower() == 'bit':
            os.system("speedtest --simple")
            return
        else:
            print "Hazel : Whoa! what was that. Choose any of the given value."
            speedtest()
    
    except Exception,e:
        print "Hazel : I have strong feeling that you are not connected to the internet"

