#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

import os
import sys
import random
import difflib
import os.path
import operator
from nltk import *
from nltk.corpus import stopwords
from repo_list_formatter import *
from difflib import SequenceMatcher
from nltk.tokenize import word_tokenize

global d
global a

###########################################################################################################################

### PACKAGE INSTALLER - Search and indexing from repo list ###

def install(tokens):
    pacmandb = os.path.isfile("/var/lib/pacman/db.lck")
    if pacmandb is False:
        print("")

    elif pacmandb is True:
        os.system("sudo rm /var/lib/pacman/db.lck") # Unlock package manager

    st = " "
    a = " "
    d = {}
    tokened = word_tokenize(tokens) # tokenizer

    if "install" in tokened:
        tokened.remove("install")

    if "get" in tokened:
        tokened.remove("get")

    if "setup" in tokened:
        tokened.remove("setup")

    if "download" in tokened:
        tokened.remove("download")

    if "want" in tokened:
        tokened.remove("want")

    for i in range(0, len(tokened)):
        st = st + " " + tokened[i] # Make out package name from tokens    #print st[2:]
    print("Hazel : searching and indexing best matches for", st[2:],"\n")
    a = os.popen("pacaur -Sqs " + st).read().split("\n")[:20] # Search and index first 20 results

    if len(a) <= 1: # if a has no entry
        print("        No install candidates were found for ", st[2:],". Are you sure you typed it right? Try again...")
        os.system("notify-send -u critical Hazel 'package not found'")
        return

    else:
        installer(a) # Continue with installing proces
        return




##########################################################################################################################


### PACKAGE INSTALLER - Install selected package ###

def installer(a):

    d = {}
    for i, j in enumerate(a): # display the indexed file
        d[i] = j.split("\n")[0]
        print(i+1, d[i])
    x = input("\nChoose the id of the package from the above list, which you want to install\npress '0' to exit \n: ")
    x = int(x)

    if x is 0:
        return

    elif x is not 0:
        for i, j in enumerate(a): # Prepare package for installation from the  id chosen
            d[i] = j.split(" - ")[0]

        cmd1 = "pacaur -Si " # Get package info
        cmd2 = " > appname.txt"
        os.system(cmd1 + d[int(x-1)] + cmd2)
        print("\nDo you wish to install",d[int(x-1)]," on this machine?")
        confirm = input("type 'y' for yes, 'r' to read more information about the package, 'n' to quit : ")
        print(confirm)

        if confirm.lower() == "y":
            os.system("notify-send -u critical Hazel 'Installing package'")
            print(d[int(x-1)])
            os.system("pacaur -S --force --noconfirm --noedit " + d[int(x-1)]) # Automated installation of package
            os.system("notify-send -u critical Hazel 'Succesfully installed'")

        elif confirm.lower() == "r": # Display
            print("\n\n")
            os.system("most appname.txt") # display package info
            os.system("rm appname.txt") # remove the display file
            installer(a) # redisplay package list
            return

        elif confirm.lower() == "": # exit installation process
            os.system("notify-send -u critical Hazel 'You didnt input a value'")
            #return

        else:
            #print("quit")
            return

    elif x == "": # NO Result
        os.system("notify-send -u critical Hazel 'you did'nt choose a package ID'")
        return

    else:
        return




##########################################################################################################################


### PACKAGE REMOVER - Search and index installed package ###


def remove(tokens):
    pacmandb = os.path.isfile("/var/lib/pacman/db.lck")
    if pacmandb is False:
        print("")

    elif pacmandb is True:
        os.system("sudo rm /var/lib/pacman/db.lck") # Unlock package manager

    st = " "
    a = " "
    d = {}
    i = 0
    pcount = 0
    tokened = word_tokenize(tokens)

    if "remove" in tokens:
        tokened.remove("remove")

    elif "dont" in tokened:
        if "want" in tokened:
            i = i + 1
            tok = "remove"
            tokened.remove("want")    #break
        tok = "remove"
        tokened.remove("dont")

    elif "want" in tokened:
        tok = "install"
        tokened.remove("want")

    elif "remove" in tokened:
        tok = "remove"
        tokened.remove("remove")

    elif "get" in tokened:
        if "rid" in tokened:
            i = i + 1
            tok = "remove"
            tokened.remove("rid") #break
        tok = "install"
        tokened.remove("get")

    elif "uninstall" in tokened:
        tok = "remove"
        tokened.remove("uninstall")

    elif "longer" in tokened:
        #print("longer")
        if "need" in tokened:
            i = i + 1
            tokened.remove("need")

        if "want" in tokened:
            i = i + 1
            tokened.remove("want")
        tok = "remove"
        tokened.remove("longer")

    print("Hazel : searching for ", tokened[0]," in the system\n")
    os.system("pacaur -Qqm > installed_apps.txt")
    os.system("pacaur -Qqn >> installed_apps.txt")

    for i in range(0, len(tokened)):
        st = st + " " + tokened[i]

    with open('installed_apps.txt', 'r') as f:
        for line in f:
            liner = line.strip()
            matcher = SequenceMatcher(None, liner, st).ratio()

            if matcher >= 0.5:    #print line, matcher
                d[i] = liner
                i = i + 1 #print d[0]
                pcount = pcount + 1

            else:
                pcountr = 0

        if pcount >= 1:
            remover(pcount, d)

        else:
            os.system("notify-send -u critical Hazel 'No package were installed with that name.'")


def remover(pc, d):
    print("\033[1;34;1m")
    pcount = pc

    for i in range(0, pcount):
        print(i+1, d[i])

    select = input("\nTo quit the package description type 'q' anytime.\nEnter the package id to be uninstalled \ntype '0' to quit: ")
    select = int(select)

    if select == 0:
        print("")

    elif select is not 0:
        pkg = d[int(select-1)]
        os.system("pacaur -Qi " + pkg + " > appname.txt")
        os.system("most appname.txt")
        print("\n\nDo you wish to uninstall", pkg, "?")
        confirm = input("Type 'y' to continue; 'n' to reselect; 'q' to quit : ")

        if confirm == 'y':
            os.system("notify-send -u critical Hazel 'Removing the package'")
            os.system("pacaur -Rsc " + pkg)
            os.system("notify-send -u critical Hazel 'package removed succesfully'")

        elif confirm == 'n':
            remover(pcount, d)

        elif confirm == "":
            os.system("notify-send -u critical Hazel 'Your did'nt input any value")
            return

    elif not select:
        os.system("notify-send -u critical Hazel 'You did'nt choose a package to remove")
        print("null")

    else:
        return

##########################################################################################################################


### PACKAGE UPDATER - update package or system ####

def update(tokens):
    print("\033[1;34;1m")
    pacmandb = os.path.isfile("/var/lib/pacman/db.lck")
    if pacmandb is False:
        print("")

    elif pacmandb is True:
        os.system("sudo rm /var/lib/pacman/db.lck") # Unlock package manager
    tokened = word_tokenize(tokens)
    if "repo" in tokened or "repos" in tokened or "repository" in tokened or "mirrors" in tokened or "mirror" in tokened:
        print("Hazel : Updating reposirtories\n")
        os.system("pacaur -Syy  --noconfirm --noedit --silent")
        os.system("notify-send -u critical Hazel 'Updated distribution reposirtories'")

    else:
        print("Hazel : Performing full system update\n")
        os.system("pacaur -Syyu --noconfirm --noedit --silent")
        os.system("notify-send -u critical Hazel 'Updated your system'")



##########################################################################################################################