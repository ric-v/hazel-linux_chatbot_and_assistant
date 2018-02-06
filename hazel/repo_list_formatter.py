#!/usr/bin/python

##########################################################################################################################

### Importing important python packages required by Hazel ###

import os
import sys
import random
import difflib
import operator
from nltk import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

############################################################################################################################


### LIST AND SORT PACKAGES IN OFFICIAL AND OTHER REPOSITORIES OF THE DISTRIBUTION TO repo_app_list.txt ###

def formatter():
	
	s = ""
	os.system('touch all_apps_unformated.txt') # Create temp files to store unsorted list 
	os.system('touch repo_app_list.txt')
	os.system('wget -P "." "https://aur.archlinux.org/packages.gz" &>/dev/null && gunzip -f "packages.gz" | sort packages > all_apps_unformated.txt') # List AUR packages
	os.system('sudo pacaur -Qq >> all_apps_unformated.txt') # List official repo packages

	with open('all_apps_unformated.txt', 'r') as f, open('repo_app_list.txt', 'w') as fo: # Format the input list
		for line in f:#
			tokens = word_tokenize(line)
			fo.write("\n")
			fo.write(str(tokens[0]))

	os.system("rm -rf packages") # Clean the temp files created during the process
	os.system("rm -rf all_apps_unformated.txt")


##########################################################################################################################