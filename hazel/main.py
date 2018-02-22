#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

from __future__ import print_function
import os
import sys
import time
import socket
import signal
import psutil
import random
import getpass
import difflib
import getpass
import readline
import operator
import platform
import datetime
from bs4 import *
from nltk import *
import wikipedia as w
from gmail import *
from wikisearch import *
from systeminfo import *
from wikiapi import WikiApi
from hazel_chatter import *
from package_surfer import *
#from fileoperations import *
from textblob import TextBlob
from nltk.corpus import stopwords
from prompt_toolkit import prompt
from collections import *
#from collections import OrderedDict
from difflib import SequenceMatcher
from nltk.tokenize import word_tokenize
from prompt_toolkit.history import FileHistory
from vocabulary.vocabulary import Vocabulary as vb
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

##########################################################################################################################

### FUNCTION TO HANDLE EVENTS SUCH AS ctrl+C OR ctrl+Z TO PREVENT THE PROGRAM FROM TERMINATION ###

def sigint_handler(signum, frame):
    print ('') # Display message on occurance of below events

signal.signal(signal.SIGINT, sigint_handler) # handle Ctrl+C on event
signal.signal(signal.SIGTSTP, sigint_handler) # handle Ctrl+Z on event

def data(i):
    return i

global callme
callme = "there"


##########################################################################################################################


### FUNCTION TO IMPLEMENT FUNCTIONS  OTHER THAN PACKAGE MANAGEMENT, REDIRECTED FROM MAIN() FUNCTION BELOW ###
### UNFORMATTED AND NEEDS A MAJOR CHANGE TO WORK AS EXPECTED, CURRENTLY IN STAGE 1 ####

def others(tokens, message, unstopped_tokens, chat): # Funtion defention of Others, passed arguements are the tokenized message and original message or user input

    global callme

    ### WIKIPEDIA SEARCH ####
    
    if "tell" in unstopped_tokens and "about" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "tell" in unstopped_tokens and "more" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "change" in tokens and "date" in tokens:
        set_date()

    elif "date" in tokens:
        datenow(tokens)

    elif "time" in tokens:
        timenow(tokens)

    elif "my" in unstopped_tokens and "username" in unstopped_tokens or "my" in unstopped_tokens and "user" in unstopped_tokens and "name" in unstopped_tokens:
        if "change" in tokens:
            socli(chat, unstopped_tokens)
        username = getpass.getuser()
        print("\nHazel : Your username on this system is ",username)

    elif "look" in unstopped_tokens and "for" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "battery" in tokens and "status" in tokens or "battery" in tokens and "charge" in tokens or "battery" in tokens and "status" in tokens:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        if plugged==False: plugged="Not Plugged In"
        else: plugged="Plugged In"
        print("\nHazel : Your battery percentage is ", percent + "% | " + plugged)

    elif "ram" in unstopped_tokens and "usage" in unstopped_tokens or "ram" in tokens and "available" in tokens or "ram" in unstopped_tokens and "used" in unstopped_tokens:
        print("\033[1;34;1m")
        mem=str(os.popen('free -t -m').readlines())
        T_ind=mem.index('T')
        mem_G=mem[T_ind+14:-4]
        S1_ind=mem_G.index(' ')
        mem_T=mem_G[0:S1_ind]
        mem_G1=mem_G[S1_ind+8:]
        S2_ind=mem_G1.index(' ')
        mem_U=mem_G1[0:S2_ind]
        mem_F=mem_G1[S2_ind+8:]
        print('Total Memory = ' + mem_T + ' MB')    
        print('Free Memory = ' + mem_F + ' MB')

    elif "list" in unstopped_tokens and "browsers" in unstopped_tokens or "list" in unstopped_tokens and "browser" in unstopped_tokens or "show" in unstopped_tokens and "browser" in unstopped_tokens:
        a = os.popen("pacaur -Qqs web browser").read().split("\n")[:20] # Search and index first 20 results
        for i, j in enumerate(a): # display the indexed file
            d[i] = j.split("\n")[0]
            print(d[i])

    elif "list" in unstopped_tokens and "image" in unstopped_tokens or "list" in unstopped_tokens and "image" in unstopped_tokens or "show" in unstopped_tokens and "image" in unstopped_tokens:
        a = os.popen("pacaur -Qqs image viewer").read().split("\n")[:20] # Search and index first 20 results
        for i, j in enumerate(a): # display the indexed file
            d[i] = j.split("\n")[0]
            print(d[i])


    elif "internet" in tokens and "speed" in tokens:
        speedtest()

    elif "new" in unstopped_tokens and "mail" in tokens or "new" in unstopped_tokens and "email" in tokens or "new" in unstopped_tokens and "e-mail" in tokens:
        confirm = input("Do you wish to send a new email? ")
        if confirm == 'y' or confirm == 'yes' or confirm == 'ya' or confirm == 'yeah' or confirm == 'yep':
            mail()

    elif "send" in unstopped_tokens and "mail" in tokens or "send" in unstopped_tokens and "email" in tokens or "send" in unstopped_tokens and "e-mail" in tokens:
        confirm = input("Do you wish to send a new email? ")
        if confirm == 'y' or confirm == 'yes' or confirm == 'ya' or confirm == 'yeah' or confirm == 'yep':
            mail()

    elif "how" in unstopped_tokens and "to" in unstopped_tokens:
        socli(chat, unstopped_tokens)

    elif "how" in unstopped_tokens and "can" in unstopped_tokens and "i" in unstopped_tokens:
        socli(chat, unstopped_tokens)

    elif "how" in unstopped_tokens and "will" in unstopped_tokens and "i" in unstopped_tokens:
        socli(chat, unstopped_tokens)

    elif "my" in unstopped_tokens and "ip" in tokens or "my" in unstopped_tokens and "network" in tokens and "address" in tokens or "system" in tokens and "ip" in tokens:
        try:
            print("\033[1;34;1m")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print("\nHazel : Your current IP address is", s.getsockname()[0])
            s.close()
        except Exception as e:
            print("no connection")
            s.close()

    elif "where" in unstopped_tokens and "is" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "get" in unstopped_tokens and "details" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "tell" in unstopped_tokens and "me" in unstopped_tokens and "about" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "get" in unstopped_tokens and "information" in unstopped_tokens:
        wiki(unstopped_tokens, message)
 
    elif "what" in unstopped_tokens and "is" in unstopped_tokens and "my" not in unstopped_tokens:
        socli(chat, unstopped_tokens)

    elif "call" in unstopped_tokens and "me" in unstopped_tokens:
        if callme == 'there' or not callme:
            callme = boss()
        else:
            print(callme)

    elif "kernel" in unstopped_tokens and "version" in unstopped_tokens or "which" in unstopped_tokens and "kernel" in unstopped_tokens:
        os.system("uname -r")  

    elif "my" in unstopped_tokens and "name" in unstopped_tokens:
        if callme == "there" or not callme:
            callme = boss()
        else:
            print("\033[1;34;1m")
            print("\nHazel : Come on, ",callme, "stop testing our relationship! I know who you are.")

    elif "memory" in unstopped_tokens and "usage" in tokens or"memory" in tokens and "available" in tokens or "storage" in tokens and "space" in tokens or "harddisk" in tokens and "space" in tokens and "left" in tokens:
        meminfo()

    elif "Which" in tokens and "os" in tokens and "i" in tokens or "Which" in tokens and "operating system" in tokens and "i" in tokens:
        platform.linux_distribution()

    elif "my" in unstopped_tokens and "os" in tokens or "os" in tokens and "using" in tokens or "operating system" in tokens and "using" in tokens:
        platform.linux_distribution()

    elif "existing" in tokens and "users" in tokens or "list" in tokens and "users" in tokens:
        list_users(tokens)

    elif "new" in tokens and "user" in tokens or "new" in tokens and "account" in tokens:
        adduser(tokens)

    elif "change" in tokens and "password" in tokens:
        chpasswd(tokens)

    elif "remove" in tokens and "user" in tokens or "remove" in tokens and "account" in tokens or "delete" in tokens and "user" in tokens or "delete" in tokens and "account" in tokens:
        deltuser(tokens)

    elif "internet" in tokens and "active" in tokens or "internet" in tokens and "connected" in tokens or "available" in tokens:
        is_connected()

    elif "who" in unstopped_tokens and "is" in unstopped_tokens or "who" in unstopped_tokens and "was" in unstopped_tokens:
        wiki(unstopped_tokens, message)


    ### GOOGLE SEARCH ###

    elif "google" in tokens: # googler api search to display top 10 results from google with link, links open in default browser 
        cmd = "googler"
        print("To quit the search results, type q")
        os.system(cmd + " " + message) # perform command in shell


    ### Close the application, ctrl+c or ctrl+z wont work ###

    elif "close" in tokens or "q" in tokens or 'quit' in tokens or 'exit' in tokens:
        exit(0)

    ### OPEN FILE MANAGER ###
    ### CURRENTLY SUPPORTS OPENING TEXT FILES OR PROGRAMMING FILES ###

    elif "create" in tokens:
        openfiles()



    #### IF USER INTENDS TO DO NONE OF THE ABOVE ACTIONS, RUN THE hazel_chatter.py FILE TO GET NORMAL CHAT OUTPUTS ###
    ### DEEP LEARNING MODEL NOT IMPLEMENTED YET. CURRENTLY WORKS WITH A TEXT DATABASE TO RETRIEVE AN NLP OUTPUT, THIS IS RECURSIVE CHAT AND NOT GENERATIVE AS IN DEEP LEARNING ###

    else:
        chatter(chat) # Function call to hazel_chatter.py, passed the original user input as asrguement



########################################################################################################################


### MAIN FUNCTION WHICH WORKS AT APPLICATION STARTUP AND RECEIVES USER INPUT ###

def main():

    print("\033[1;34;1m")
    print("\n\n\nHazel : Hey ",callme,", type 'h' to get help or simply start chatting with me") # Initial message shown at every startup
    
    SQLCompleter = WordCompleter(['install', 'uninstall', 'update', 'upgrade', 'who is', 'what is', 'quit', 'google', 'check internet connection', 'my ip address', 'my name', 'send email', 'internet speed', 'date today', 'time now', 'change date', 'change time', 'battery status'],
                             ignore_case=True)

    while True: # Enter the loop anyways
        print("\033[1;32;1m")
        message =   prompt('\nYou   : ',
                        history=FileHistory('/tmp/history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter,
                        )
        message = message.lower()
        msg = message.lower() # temporary storage of message value
        unstopped_tokens = ""
        tokens = word_tokenize(message) # NLTK function tokenize to tokenize user input
        unstopped_tokens = word_tokenize(message)
        d = {} # Store package names during package management
        tok = "" # Temporary variable to store tokens and to determine its value
        stop_words = set(stopwords.words('english')) # Remove stop words
        filtered_sentence = [w for w in tokens if not w in stop_words]
        filtered_sentence = []
        for w in tokens: # Filtering input by removing stopwords such as 'I', 'for', 'is', etc.
            if w not in stop_words:
                filtered_sentence.append(w) # Get and store message without stopeords

        filtered_list = filtered_sentence
        filtered_sentence = ' '.join(filtered_list) # Making a sentance out of the tokens
        chat = message
        message = filtered_sentence # storing input in message
        tokens = word_tokenize(message) # tokenize new message
        pcount = 0 # pcount to check if package manager search result is null or greater than 1

        message_length = len(message.split()) # Textblob function to check the sentiment asscoiated with a sentance.
        blob = TextBlob(message) # Apply sentiment analysis on message. If polarity is +ve or -ve, directly goto chat else if its neutral, perform system command or else do chat
        length = len(message.split()) # find length of the message

        for sentence in blob.sentences: # Get polarity or sentment value. 0 = neutral, -ve = negative, +ve = positive
            pol = sentence.sentiment.polarity # polarity ranges from -1 to +1

        if "h" in tokens: # Print the help.txt file to read the description and manual page of Hazel
            print("\033[1;37;1m")
            os.system("most /opt/hazel-linux_chatbot_and_assistant/hazel/help.txt") # Using 'most' command to print in pages 

        elif "h" not in tokens: # if not h, go through package list anyways to ckeck if user have mentioned the name of a package in the chat input

            tokened = tokens # Temporary variable for tokens


            ### STARTING FROM HERE IS PACKAGE MANAGEMENT, THIS IS UNDERGONE FOR ALL INPUTS TO MAKE SURE PACKAGE MANAGEMENT IS DONE IN THE MOST EFFICIENT WAY POSSIBLE, IF NO PACKAGE NAME OR ACTION IS MENTIONED, THE EXECUTION CONTINUES TO OTHER FUNCTIONS OR CHAT ###

            for i in range(0, len(tokened)): # search all tokened value
                if "install" in tokened:
                    tok = "install" # tok is set to install so that, all keywords that mey seem similar to install are passed to installer function
                    tokened.remove("install") # remove the checked keyword

                elif "dont" in tokened:
                    if "want" in tokened:
                        i = i + 1 # update i value as 1st value is checked and removed
                        tok = "remove" # tok is set to remove so that, all keywords that may seem similar to remove are passed to remover function
                        tokened.remove("dont") # remove the checked keyword
                        tokened.remove("want")
                        break
                    tok = "remove"
                    tokened.remove("want")

                elif "want" in tokened and "install" in tokened:
                    tok = "install"
                    tokened.remove("want")

                elif "want" in tokened and "remove" in tokened or "want" in tokened and "remove" in tokened:
                    tok = "remove"
                    tokened.remove("remove")

                elif "remove" in tokened:
                    tok = "remove"
                    tokened.remove("remove")


                elif "uninstall" in tokened:
                    tok = "remove"
                    tokened.remove("uninstall")

                elif "upgrade" in tokened:
                    print(tok)
                    if "system" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("system")
                    if "all" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("all")
                    if "apps" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("apps")
                    tokened.remove("upgrade")
                    update(message) # call update function in package_surfer.py

                elif "update" in tokened:
                    print(tok)
                    if "system" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("system")
                    if "all" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("all")
                    if "apps" in tokened:
                        i = i + 1
                        tok = "upgrade"
                        tokened.remove("apps")
                    tokened.remove("update")
                    update(message) # call update function in package_surfer.py


                elif "longer" in tokened:
                    if "need" in tokened:
                        i = i + 1
                        tok = "remove"
                        tokened.remove("need")
                    if "want" in tokened:
                        i = i + 1
                        tok = "remove"
                        tokened.remove("want")
                    tok = "remove"
                    tokened.remove("longer")
                    

            ###  END OF CONDITION CHECKING ###
            ### ENTERING PACKAGE NAME CROSS CHECKING WITH THE ONES IN THE DISTRIBUTION REPOSITORIES ###

            for j in range(0, len(tokened)):
                with open('/opt/hazel-linux_chatbot_and_assistant/hazel/repo_app_list.txt','r') as f: # Open repo_app_list.txt which contains the list of all possible packages that can be installed on this Linux
                    for line in f:
                        liner = line.strip() # remove white spaces
                        matcher = SequenceMatcher(None, liner, tokened[j]).ratio() # Match the list element with input term to see if a package has atleast 50% similar name as with the package in the repository

                        if matcher >= 0.75: # if a package with >= 50% match is found, it is listed later
                            pcount = pcount + 1 # updates pcount since a package with match is found

            if pcount > 0: # if atleast 1 package exists in repo_app_list.txt
                print("\033[1;34;1m")

                if "install" == tok: # tok is install
                    print("\nPackage Installer\n")
                    install(message) # call install function in package_surfer.py

                elif "remove" == tok: # tok is remove
                    print("\nPackage Remover\n")
                    remove(message) # call remove function in package_surfer.py

                else: # If none of the above operation is triggered, it is not package management, redirect to other funtions
                    others(tokens, message, unstopped_tokens, chat)
            else:
                others(tokens, message, unstopped_tokens, chat)

if __name__ == "__main__":
    main()
else:
    print("hell")

#main() # start executing the main.py file by calling main() funtion



##########################################################################################################################
