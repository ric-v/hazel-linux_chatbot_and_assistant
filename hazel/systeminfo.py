import os
import sys
import random
import socket
import string
import difflib
import datetime
from nltk import *
from random import randint

dt = str(datetime.datetime.now().date())


def datenow(tokens):
    print("\033[1;34;1m")
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
        
        print("\nHazel : Today is ",str(datetime.datetime.now().day), subscrit," of", month,str(datetime.datetime.now().year))
    
    else:
        
        print("\033[1;34;1m")
        print("Hazel : Do you mean to get today's date?\n\n")
        print("\033[1;32;1m")
        ask = input("\n\nYou   : ")
        
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
            
            print("\033[1;34;1m")
            print("\nHazel : Today is ",str(datetime.datetime.now().day), subscrit," of", month,str(datetime.datetime.now().year))
        
        else:
            return

def timenow(tokens):
    
    hr = datetime.datetime.now().strftime('%H')
    mn = datetime.datetime.now().strftime('%M')
    sec = datetime.datetime.now().strftime('%S')
    print("\033[1;34;1m")
    print("\nHazel : The time is ", str(hr), ":", str(mn))


def adduser(tokens):
    print("\033[1;34;1m")
    print("\n\n")
    choices = {1: "Create a user account with home directory", 2: "Create an administrator account with home directory", 0: "quit this menu"}
    for key, value in choices.items():
        print(key, "- ", value)
        ch = input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
        # print ch
        
        if ch == '1':
            useracnt()
            return
        
        elif ch == '2':
            adminacnt()
            return
        
        elif ch == '0':
            return
        
        else:
            print("\n\n\nchoose an option from the below list : ")
            adduser(tokens)


def useracnt():
    print("\033[1;34;1m")
    uname = input("Hazel : Set a new username for this user : ")
    
    if not os.system("sudo useradd -m "+ uname):
        print("        Account for ", uname, "was succesfully created.")
        password = input("        Type 'y' to set a new password or press enter to let me set a random password for you : ")
        
        if not password:
            passwd = password_generator()
        
        elif password.lower() == 'y':
            os.system("sudo passwd " + uname)
        
        else:
            return
        
        udetails = input("        Do you wish to edit personal details of this account? type 'y' or 'n' : ")
        
        if udetails.lower() == 'y':
            full_name = input("Enter your full name : ")
            os.system("sudo chfn -f " + full_name + uname + " > temp")
            print("        ", uname, "was succesfully modified and ready to use")
            os.system("rm -rf temp")
        
        else:
            return

def adminacnt():
    print("\033[1;34;1m")
    uname = input("Hazel : Set a new username for the admin account : ")
    if not os.system("sudo useradd -m -G wheel "+ uname):
        print("        Account for ", uname, "was succesfully created.")
        password = input("        Type 'y' to set a new password or press enter to let me set a random password for you : ")
        
        if not password:
            passwd = password_generator()
        
        elif password.lower() == 'y':
            os.system("sudo passwd " + uname)
        
        else:
            return
        
        udetails = input("        Do you wish to edit personal details of this account? type 'y' or 'n' : ")
        if udetails.lower() == 'y':
            full_name = input("Enter your full name : ")
            os.system("sudo chfn -f " + full_name + uname + " > temp")
            print("        ", uname, "was succesfully modified and ready to use")
            os.system("rm -rf temp")
        
        else:
            return

def password_generator():
    print("\033[1;34;1m")
    pas = randint(10, 99)
    pas1 = random.choice(string.ascii_lowercase)
    pas2 = random.choice(string.ascii_lowercase)
    pas3 = randint(10, 99)
    passwd = str(pas)+pas1+pas2+str(pas3)
    print("        Your system password is ",passwd)
    check = input("        Do you wish to try another?  ")
    
    if check.lower() == 'y':
        password_generator()
    
    else:
        return passwd

def deltuser(tokens):
    print("\033[1;34;1m")
    print("\n\n")
    choices = {1: "remove user only", 2: "remove user with all its data", 0: "quit this menu"}
    for key, value in choices.items():
        print(key, "- ", value)
        ch = input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
	# print ch
        
        if ch == '1':
            useacnt()
            return
        
        elif ch == '2':
            admnacnt()
            return
        
        elif ch == '0':
            return
        
        else:
            print("\n\n\nchoose an option from the below list : ")
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
    print("\033[1;34;1m")
    uname = input("Hazel : Type the user name you want to delete : ")
    if not os.system("sudo userdel  "+ uname):
        print("        Account for ", uname, "was succesfully deleted .")


def admnacnt():
    print("\033[1;34;1m")
    print("Hazel : Type user account you want to delete")
    uname = input("\n\nYou   : ")
    if not os.system("sudo userdel -rf " + uname):
        print("        Account for ", uname, "was succesfully deleted.")


def chpasswd(tokens):
    print("\033[1;34;1m")
    print("\n\n")
    choices = {1: "Change the user password", 2: "Change root password (not recommended for new users)", 0: "quit this menu"}
    for key, value in choices.items():
        print(key, "- ", value)
        ch = input("\nTo read more on how each option works type 'r'\nor\nEnter your choice : ")
        
        if ch == '1':
            uname = input("\nEnter the username you want to remove : ")
            os.system("sudo passwd " + uname)
        
        elif ch == '2':
            uname = input("\nEnter the username you want to remove : ")
            os.system("sudo passwd " + uname)
        
        elif ch == '0':
            return
        
        else:
            return

def list_users(tokens):
    print("\033[1;34;1m")
    print("\nHazel : Users in this systme are : ")
    os.system("ls /home")

def is_connected():
    print("\033[1;34;1m")
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        print('\nHazel : Your internet is connected.')
        return True

    except Exception as e:
        print("\nHazel : Your internet connection is off. Shall I get you connected?")
        ask = input("You   : ")
        ask = ask.lower()
        if ask == 'y' or y == 'yes' or ask == 'ya' or ask == 'yeah':
            os. system("sudo wifi-menu")
        else:
            return
    return False


def speedtest():
    print("\033[1;34;1m")
    try:
        ch = input("\nHazel : Shall I show the result in Bytes rather than in Bits (1 Bytes = 8 Bits; 128kBps ~ 1Mbps) : ")
        if ch.lower() == 'y' or ch.lower() == 'yes' or ch.lower() =='bytes' or ch.lower() == 'byte':
            os.system("speedtest --bytes --simple")
            return
        elif ch.lower() == 'n' or ch.lower() == 'no' or ch.lower() == 'bits' or ch.lower() == 'bit':
            os.system("speedtest --simple")
            return
        else:
            print("\nHazel : Whoa! what was that. Choose any of the given value.")
            speedtest()

    except Exception  as e:
        print("\nHazel : I have strong feeling that you are not connected to the internet")


def boss():
    print("\033[1;34;1m")
    callme = input("\nHazel : What should I call you?")
    if not callme:
        print("\n        Well that's a hard name to call...")
        callme = input("\n       Tell me your name : ")
    print("\nHazel : Hello ", callme," I hope you are enjoying my company so far!")
    return callme

def meminfo():
    print("\033[1;34;1m")
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    print('\nHazel : Total memory: {0}'.format(meminfo['MemTotal']))
    print('        Free memory: {0}'.format(meminfo['MemFree']))


def set_date():
    print("\033[1;34;1m")
    #hr = datetime.datetime.now().strftime('%H')
    #mn = datetime.datetime.now().strftime('%M')
    #sec = datetime.datetime.now().strftime('%S')
    #print("\nHazel : Current system time is : ", hr,":",mn,":",sec)
    print("\nHazel : Current date is : ", datetime.datetime.now())
    year = input("\nEnter the year as YYYY : ")
    month = input("Enter the month as MM : ")
    date = input("Enter the date as DD : ")
    date_change = year+"-"+month+"-"+date
    print(date_change)
    os.system("timedatectl set-time " + date_change)