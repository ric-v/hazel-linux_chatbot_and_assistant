#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

import difflib
import operator

global d

##########################################################################################################################

d = {}


### CHAT DATA AND FUNCTION - performs normal chat to user input ###

def chatter(msg):
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

    if max(dic.values()) < 0.5: # Unknown input
        print("\033[1;34;1m")
        print "Hazel : Can you  be more specific, type 'h' to get help or 'q' to quit"

    else: # Reply to known input
        print("\033[1;34;1m")
        print "Hazel :", d[max(dic.iteritems(), key=operator.itemgetter(1))[0]]



##########################################################################################################################