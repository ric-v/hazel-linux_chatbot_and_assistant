#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

import os
import sys
import time
import socket
import signal
import random
import difflib
import operator
import datetime
from bs4 import *
from nltk import *
import wikipedia as w
from gmail import *
from wikisearch import *
from systeminfo import *
from PyQt4.QtGui import *
from wikiapi import WikiApi
from hazel_chatter import *
from package_surfer import *
from fileoperations import *
from textblob import TextBlob
from nltk.corpus import stopwords
from difflib import SequenceMatcher
from nltk.tokenize import word_tokenize
from vocabulary.vocabulary import Vocabulary as vb


##########################################################################################################################



### FUNCTION TO HANDLE EVENTS SUCH AS ctrl+C OR ctrl+Z TO PREVENT THE PROGRAM FROM TERMINATION ###

def sigint_handler(signum, frame):
    print '' # Display message on occurance of below events

signal.signal(signal.SIGINT, sigint_handler) # handle Ctrl+C on event
signal.signal(signal.SIGTSTP, sigint_handler) # handle Ctrl+Z on event

def data(i):
    return i



##########################################################################################################################


### FUNCTION TO IMPLEMENT FUNCTIONS  OTHER THAN PACKAGE MANAGEMENT, REDIRECTED FROM MAIN() FUNCTION BELOW ###
### UNFORMATTED AND NEEDS A MAJOR CHANGE TO WORK AS EXPECTED, CURRENTLY IN STAGE 1 ####

def others(tokens, message, unstopped_tokens): # Funtion defention of Others, passed arguements are the tokenized message and original message or user input


    ### WIKIPEDIA SEARCH ####
    
    if "search" in tokens:
        wiki(tokens, message)

    elif "who" in unstopped_tokens and "is" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "what" in unstopped_tokens and "is" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "look" in unstopped_tokens and "for" in unstopped_tokens:
        wiki(unstopped_tokens, message)

    elif "internet" in tokens and "speed" in tokens:
        speedtest()

    elif "mail" in tokens or "email" in tokens or "e-mail" in tokens:
        mail()

    elif "ip" in tokens or "IP" in tokens:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print "Hazel : Your current IP address is", s.getsockname()[0]
            s.close()
        except Exception,e:
            print "no connection"
            s.close()


    elif "new" in tokens and "user" in tokens or "new" in tokens and "account" in tokens:
        adduser(tokens)

    elif "change" in tokens and "password" in tokens:
        chpasswd(tokens)

    elif "remove" in tokens and "user" in tokens or "remove" in tokens and "account" in tokens or "delete" in tokens and "user" in tokens or "delete" in tokens and "account" in tokens:
        deltuser(tokens)

    elif "internet" in tokens and "active" in tokens or "internet" in tokens and "connected" in tokens:
        is_connected()

    elif "date" in tokens:
        datenow(tokens)

    elif "time" in tokens:
        timenow(tokens)

            
    ### GOOGLE SEARCH ###

    elif "howto" in tokens: # googler api search to display top 10 results from google with link, links open in default browser 
        cmd = "googler"
        print "To quit the search results, type q"
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
        chatter(message) # Function call to hazel_chatter.py, passed the original user input as asrguement



########################################################################################################################


### MAIN FUNCTION WHICH WORKS AT APPLICATION STARTUP AND RECEIVES USER INPUT ###

def main():

    print("\033[1;34;1m")
    print "\n\nHazel : Hey there, type 'h' to get help or simply start chatting with me" # Initial message shown at every startup

    while True: # Enter the loop anyways
        print("\033[1;32;1m")
        message = raw_input("\n\nYou   : ") # recieve user input at message
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
            os.system("most help.txt") # Using 'most' command to print in pages

        elif "h" not in tokens: # if not h, go through package list anyways to ckeck if user have mentioned the name of a package in the chat input

            tokened = tokens # Temporary variable for tokens


            ### STARTING FROM HERE IS PACKAGE MANAGEMENT, THIS IS UNDERGONE FOR ALL INPUTS TO MAKE SURE PACKAGE MANAGEMENT IS DONE IN THE MOST EFFICIENT WAY POSSIBLE, IF NO PACKAGE NAME OR ACTION IS MENTIONED, THE EXECUTION CONTINUES TO OTHER FUNCTIONS OR CHAT ###

            for i in range(0, len(tokened)): # search all tokened value
                if "install" in tokened:
                    tok = "install" # tok is set to install so that, all keywords that mey seem similar to install are passed to installer function
                    tokened.remove("install") # remove the checked keyword

                elif "setup" in tokened:
                    tok = "install"
                    tokened.remove("setup")

                elif "download" in tokened:
                    tok = "install"
                    tokened.remove("download")

                elif "dont" in tokened:
                    if "want" in tokened:
                        i = i + 1 # update i value as 1st value is checked and removed
                        tok = "remove" # tok is set to remove so that, all keywords that may seem similar to remove are passed to remover function
                        tokened.remove("dont") # remove the checked keyword
                        tokened.remove("want")
                        break
                    tok = "remove"
                    tokened.remove("want")

                elif "want" in tokened:
                    tok = "install"
                    tokened.remove("want")

                elif "remove" in tokened:
                    tok = "remove"
                    tokened.remove("remove")

                elif "get" in tokened: # here, 'get rid' means to remove but 'get' alone means to install
                    if "rid" in tokened:
                        i = i + 1
                        tok = "remove"
                        tokened.remove("rid")
                        break
                    tok = "install"
                    tokened.remove("get")

                elif "uninstall" in tokened:
                    tok = "remove"
                    tokened.remove("uninstall")

                elif "upgrade" in tokened:
                    print tok
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
                    print "\nSystem updater\n"
                    update(message) # call update function in package_surfer.py

                elif "update" in tokened:
                    print tok
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
                    print "\nSystem updater\n"
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
                with open('repo_app_list.txt','r') as f: # Open repo_app_list.txt which contains the list of all possible packages that can be installed on this Linux
                    for line in f:
                        liner = line.strip() # remove white spaces
                        matcher = SequenceMatcher(None, liner, tokened[j]).ratio() # Match the list element with input term to see if a package has atleast 50% similar name as with the package in the repository

                        if matcher >= 0.9: # if a package with >= 50% match is found, it is listed later
                            pcount = pcount + 1 # updates pcount since a package with match is found

            if pcount > 0: # if atleast 1 package exists in repo_app_list.txt
                print("\033[1;34;1m")

                if "install" is tok: # tok is install
                    print "\nPackage Installer\n"
                    install(message) # call install function in package_surfer.py

                elif "remove" == tok: # tok is remove
                    print "\nPackage Remover\n"
                    remove(message) # call remove function in package_surfer.py

                else: # If none of the above operation is triggered, it is not package management, redirect to other funtions
                    others(tokens, message, unstopped_tokens)
            else:
                others(tokens, message, unstopped_tokens)

main() # start executing the main.py file by calling main() funtion



##########################################################################################################################
