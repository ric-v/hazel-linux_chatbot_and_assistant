from bs4 import *
import wikipedia as wi
from wikiapi import WikiApi
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def wiki(tokens, message):

        print("\033[1;34;1m")        
        print "\nHazel : Please wait while I surf the web for a result"
        try:

            wiki = WikiApi()
            WikiApi({'locale': 'en'})
            if "search" in tokens:
                tokens.remove("search") # remove search keyword to retrieve the main content to be searched
            if "what" in tokens:
                tokens.remove("what")
            if "who" in tokens:
                tokens.remove("who")
            if "look" in tokens:
                tokens.remove("look")
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
     
            s = "" # appends the remaining tokens to be searched for
            for i in tokens:
                s = s + i + " " # appending the tokens to form a search keyword
            results = wiki.find(s) # package function to do online searched
            #print "websearch\n"
            if results == "":
                results = "null"
            print "\nFound result for : ", results[0] # print the first search result
            print("\033[1;37;1m") # set console color
            print wi.summary(s)
            #main()
        except Exception, e:
            print "I didnt get that. You may want to try that again"
