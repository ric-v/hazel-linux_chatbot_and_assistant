#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

import os
import sys
import time
import random
import signal
import difflib
import operator
from bs4 import *
from nltk import *
import wikipedia as w
from PyQt4.QtGui import *
from hazel_chatter import *
from package_surfer import *
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

def others(tokens, message): # Funtion defention of Others, passed arguements are the tokenized message and original message or user input


    ### WIKIPEDIA SEARCH ####

    if "search" in tokens: # wikipedia search for famous personals or movies or popular titles ### NOT WORKING PROPERLY ###
        try:
            from wikiapi import WikiApi
            wiki = WikiApi()
            WikiApi({'locale': 'en'})
            tokens.remove("search") # remove search keyword to retrieve the main content to be searched
            st = "" # appends the remaining tokens to be searched for
            for i in tokens:
                s = st + i + " " # appending the tokens to form a search keyword
            results = wiki.find(s) # package function to do online search
            print("\033[1;37;1m") # set console color
            #print "websearch\n"
            print "\n", results[0] # print the first search result
            print w.summary(s)
        except Exception, e:
            print "websearch failed"


    ### GOOGLE SEARCH ###

    elif "howto" in tokens: # googler api search to display top 10 results from google with link, links open in default browser 
        cmd = "googler"
        os.system(cmd + " " + message) # perform command in shell


    ### Close the application, ctrl+c or ctrl+z wont work ###

    elif "close" in tokens or "q" in tokens: 
        exit(0)


    ### GOOGLE SEARCH NOT WORKING ####

    elif "help" in tokens:
        cmd = "googler"
        print "To quit the search results, type q"
        os.popen(cmd + " " + message)


    ### OPEN FILE MANAGER ###
    ### CURRENTLY SUPPORTS OPENING TEXT FILES OR PROGRAMMING FILES ###

    elif "file" in tokens: # open qt gui file manager to choose a file which will be displayed in the same screen
        print("\033[1;34;1m")
        loc = raw_input("Enter the location you want to open or just press enter to open default direcotry : ") # Enter an absolute path. Look for tutorials on linux file paths for more details or simply press enter

        if not loc: # Open in a default locations, User home directory
            a = QApplication(sys.argv)
            w = QWidget()
            filename = QFileDialog.getOpenFileName(w, 'Open File', '~/')
            with open(filename, 'r') as f: # open a file in read mode
                print "\n\n"
                print("\033[1;37;1m")
                print(f.read()) # diplay the file contents

        else: # open file manager in the specified location
            a = QApplication(sys.argv)
            w = QWidget()
            filename = QFileDialog.getOpenFileName(w, 'Open File', loc)
            with open(filename, 'r') as f:
                print "\n\n"
                print(f.read())


    #### IF USER INTENDS TO DO NONE OF THE ABOVE ACTIONS, RUN THE hazel_chatter.py FILE TO GET NORMAL CHAT OUTPUTS ###
    ### DEEP LEARNING MODEL NOT IMPLEMENTED YET. CURRENTLY WORKS WITH A TEXT DATABASE TO RETRIEVE AN NLP OUTPUT, THIS IS RECURSIVE CHAT AND NOT GENERATIVE AS IN DEEP LEARNING ###

    else:
        chatter(message) # Function call to hazel_chatter.py, passed the original user input as asrguement



########################################################################################################################


### MAIN FUNCTION WHICH WORKS AT APPLICATION STARTUP AND RECEIVES USER INPUT ###

def main():

    print("\033[1;34;1m")
    print "\n\nHazel : Hey there, type 'h' to see all options or simply start chatting with me" # Initial message shown at every startup

    while True: # Enter the loop anyways
        print("\033[1;32;1m")
        message = raw_input("\n\nYou   : ") # recieve user input at message
        msg = message # temporary storage of message value

        tokens = word_tokenize(message) # NLTK function tokenize to tokenize user input
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

                        if matcher >= 0.5: # if a package with >= 50% match is found, it is listed later
                            pcount = pcount + 1 # updates pcount since a package with match is found

                if pcount > 0: # if atleast 1 package exists in repo_app_list.txt
                    print("\033[1;34;1m")

                    if "install" is tok: # tok is install
                        print "\nPackage Installer\n"
                        install(message) # call install function in package_surfer.py

                    elif "remove" == tok: # tok is remove
                        print "\nPackage Remover\n"
                        remove(message) # call remove function in package_surfer.py

                    elif "upgrade" == tok: # tok is update
                        print "\nSystem updater\n"
                        update(message) # call update function in package_surfer.py

                    else: # If none of the above operation is triggered, it is not package management, redirect to other funtions
                        others(tokens, message)
                else:
                    others(tokens, message)

main() # start executing the main.py file by calling main() funtion



##########################################################################################################################
