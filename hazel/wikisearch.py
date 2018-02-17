from wikiapi import WikiApi
import wikipedia as w
from bs4 import *
#from wikiapi import WikiApi

def wiki(tokens, message):
	print "wiki websearch"
        try:

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
            main()
        except Exception, e:
            print "websearch failed", e
