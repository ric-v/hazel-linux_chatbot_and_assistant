import random
from nltk import *
import os
import sys
import difflib
import operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher

def install(tokens):
	
        os.system("sudo rm /var/lib/pacman/db.lck")
        st = " "
	global a
	global d
	a = " "
	d = {}
	#message = filtered_sentenc
	#print message
	tokened = word_tokenize(tokens)
	tokened.remove("install")
	print "Hazel : searching and indexing best matches for ", tokened[0],"\n"
	
        for i in range(0, len(tokened)):
	    st = st + " " + tokened[i]
        a = os.popen("pacaur -Sqs " + st).read().split("\n")[:20]
        
        if len(a) <= 1:
            print "        No install candidates were found for ", tokened[0],". Are you sure you typed it right? Try again..."
            return
        
        else:
            installer(a)

def installer(a):
    
    for i, j in enumerate(a):
        d[i] = j.split("\n")[0]
        print i+1, d[i]
    x = input("\nChoose the id of the package you want to install to read more\npress 0 to exit \n: ")
    
    if x is not 0:
    
        for i, j in enumerate(a):
            d[i] = j.split(" - ")[0]
        cmd1 = "pacaur -Si "
        cmd2 = " > appname.txt"
        os.system(cmd1 + d[int(x-1)] + cmd2)
        os.system("most appname.txt")
        os.system("rm appname.txt")
        print "\nDo you wish to install",d[int(x-1)]," on this machine?"
        confirm = raw_input("type 'y' for yes, 'n' to search again, 'q' to quit : ")
        
        if confirm is "y":
            os.system("pacaur -S --force " + d[int(x-1)])
        
        elif confirm is "n":
            print "\n\n"
            installer(a)
            return
        
        elif confirm is "":
            return
        
        else:
            return
    
    elif x is "":
        return
    
    else:
        return


def remove(tokens):
        
        os.system("sudo rm /var/lib/pacman/db.lck")
        st = " "
	#global a
	#global d
	a = " "
	d = {}
        i = 0
        pcount = 0
	#message = filtered_sentenc
	#print message
	tokened = word_tokenize(tokens)
        
        if "remove" in tokened:
            tokened.remove("remove")
        
        elif "uninstall" in tokened:
            tokened.remove("uninstall")

	print "Hazel : searching for ", tokened[0]," in /usr/bin\n"
        os.system("pacaur -Qqm > installed_apps.txt")
        os.system("pacaur -Qqn >> installed_apps.txt")
        
        for i in range(0, len(tokened)):
            st = st + " " + tokened[i]
        
        with open('installed_apps.txt', 'r') as f:
            
            for line in f:
                liner = line.strip()
                matcher = SequenceMatcher(None, liner, st).ratio()
                
                if matcher >= 0.5:
                    #print line, matcher
                    d[i] = liner
                    i = i + 1
                    #print d[0]
                    pcount = pcount + 1
                
                else:
                    pcountr = 0
            
            if pcount >= 1:
                remover(pcount, d)

def remover(pc, d):
    pcount = pc
    
    for i in range(0, pcount):
        print i+1, d[i]
    select = input("\nTo quit the package description type 'q' anytime.\nEnter the package id to be uninstalled \ntype '0' to quit: ")
    
    if select is not 0:
        pkg = d[int(select-1)]
        os.system("pacaur -Qi " + pkg + " > appname.txt")
        os.system("most appname.txt")
        os.system("rm appname.txt")
        print "\n\nDo you wish to uninstall", pkg, "?"
        confirm = raw_input("Type 'y' to continue; 'n' to reselect; 'q' to quit : ")
        
        if confirm == 'y':
            os.system("pacaur -Rsc " + pkg)
        
        elif confirm == 'n':
            remover(pcount, d)
        
        elif confirm is "":
            return
    
    elif select is null:
        print "null"
    
    else:
        return


def update(tokens):
    tokened = word_tokenize(tokens)
    if "repo" in tokened or "repos" in tokened or "repository" in tokened or "mirrors" in tokened or "mirror" in tokened:
        print "Hazel : Updating reposirtories\n"
        os.system("sudo rm /var/lib/pacman/db.lck")
        os.system("pacaur -Syy")
    else:
        print "Hazel : Performing full system update\n"
        os.system("sudo rm /var/lib/pacman/db.lck")
        os.system("pacaur -Syyu")
