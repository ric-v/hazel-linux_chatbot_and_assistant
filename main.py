import random
from nltk import *
import os
import sys
import difflib
import operator
from bs4 import *
import wikipedia as w
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyQt4.QtGui import *
from package_surfer import *
from difflib import SequenceMatcher

#from fileoperations import *
#import list_of_commands as command
#from webscraping import *
#import Tkinter, tkFileDialog

def data(i):
    return i

print("\033[1;34;1m")
print "\n\nHazel : Hey there, type 'h' to see all options or simply start chatting with me"

while True:
    print("\033[1;32;1m")
    message = raw_input("\n\nYou   : ")
    msg = message
    tokens = word_tokenize(message)
    d = {}
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in tokens if not w in stop_words]
    filtered_sentence = []
    for w in tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    filtered_list = filtered_sentence
    filtered_sentence = ' '.join(filtered_list)

    message = filtered_sentence
    #print message
    tokens = word_tokenize(message)
    #tokens = word_tokenize(msg)

#    if not message:
#        print("\033[1;34;1m")
#       print "Hazel :  Is ur tooth aching? talk to me..."
#        continue

    if "h" in tokens:
        print("\033[1;37;1m")
        os.system("cat help.txt")
            #print "\n1. howoto - google how to do something. open details in your browser " \
            #"\n2. install - search and install a linux package from the official repository" \
            #"\n3. whois - search the biography of personnals"

    elif "search" in tokens:
        try:
            from wikiapi import WikiApi
            wiki = WikiApi()
            WikiApi({'locale': 'en'})
            tokens.remove("search")
            st = ""
            for i in tokens:
                s = st + i + " "
            results = wiki.find(s)
            print("\033[1;37;1m")
            print "websearch\n"
            print results[0]
            print w.summary(s)
        except Exception, e:
            continue

    elif "howto" in tokens:
        cmd = "googler"
        os.system(cmd + " " + message)

    elif "install" in tokens or 'uninstall' in tokens or "remove" in tokens or "upgrade" in tokens or "update" in tokens:
        #print "Package Management"
        try:
            st = ""
            a = " "
            print("\033[1;34;1m")
            
            if "install" in tokens:
                install(message)
            
            elif "remove" in tokens or "uninstall" in tokens:
                remove(message)

            elif "upgrade" in tokens or "update" in tokens:
                update(message)

            else:
                print "command not found"
        except Exception, e:
            print e
            continue

    elif "close" in tokens or "exitt" in tokens:
        exit(0)

    elif "help" in tokens:
		cmd = "googler"
		print "To quit the search results, type q"
		os.popen(cmd + " " + message)

    elif "file" in tokens:
        print("\033[1;34;1m")
        loc = raw_input("Enter the location you want to open or just press enter to open default direcotry : ")
        if not loc:
            # Create an PyQT4 application object.
            a = QApplication(sys.argv) # The QWidget widget is the base class of all user interface objects in PyQt4.
            w = QWidget() # Set window size.
            #w.resize(320, 240) # Set window title
            #w.setWindowTitle("Hello World!") # Get filename using QFileDialog
            filename = QFileDialog.getOpenFileName(w, 'Open File', '~/')
            #print (filename) # print file contents
            with open(filename, 'r') as f:
                print "\n\n"
                print("\033[1;37;1m")
                print(f.read()) # Show window
                #w.show()
                #sys.exit(a.exec_())
        else:
            a = QApplication(sys.argv) # The QWidget widget is the base class of all user interface objects in PyQt4.
            w = QWidget() # Set window size.
            #w.resize(320, 240) # Set window title
            #w.setWindowTitle("Hello World!") # Get filename using QFileDialog
            filename = QFileDialog.getOpenFileName(w, 'Open File', loc)
            #print (filename) # print file contents
            with open(filename, 'r') as f:
                print "\n\n"
                print(f.read()) # Show window
                #w.show()
                #sys.exit(a.exec_())



    # elif [data(i) in tokens for i in command.file_management] in tokens:
    #     print "file operations"
    #     try:
    #         if "create" in tokens:
    #             filename = raw_input("enter file name\n")
    #             print "create"
    #             create(filename)
    #         elif "oopen" in tokens:
    #             openfiles()
    #         elif "delete" in tokens:
    #             delete()
    #         elif "write" in tokens:
    #             print "writing new data"
    #             data = raw_input("enter the data")
    #             writing(data)
# elif "append" in tokens:
# elif "rename" in tokens:
# elif "oopen" in tokens:
# elif "move" in tokens:
# elif "change permission" in tokens:
# elif "create folder" in tokens:
# elif "remove folder" in tokens:
# elif "delete folder" in tokens:
# elif "list" in tokens:
# elif "create shortcuts" in tokens:
# elof "shortcuts" in tokens:
##
        # except Exception, e:
        #     print e
        #     continue

    else:
        f = open("db.TXT", "r")
        data = f.readlines()
        for i in data:
            i = i[:-1]
            s = i.split(":")
            d[s[0]] = s[1]
        dic = {}
        for i in d.keys():
            seq = difflib.SequenceMatcher(None, msg, i)
            dic[i] = seq.ratio()
        if max(dic.values()) < 0.5:
            print("\033[1;34;1m")
            print "Hazel : I dont know about it.Dont have a meaning in the dataset.If You need any assistance please type help"
            continue
        else:
            print("\033[1;34;1m")
            print "Hazel :", d[max(dic.iteritems(), key=operator.itemgetter(1))[0]]
