import os
import sys
from bs4 import *
from socli import *
import wikipedia as wi
from wikiapi import WikiApi
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def wiki(tokens, message):

        print("\033[1;34;1m")        
        print("\nHazel : Please wait while I surf the web for a result")
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
            if "tell" in tokens:
                tokens.remove("tell")
            if "more" in tokens:
                tokens.remove("more")
            if "about" in tokens:
                tokens.remove("about")
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
            #print("websearch\n"
            if results == "":
                results = "null"
            print("\nFound result for : ", results[0]) # print the first search result
            print("\033[1;37;1m") # set console color
            print(wi.summary(s))
            #main()
        except Exception as e:
            print("I didnt get that. You may want to try that again")

def socli(chat, tokens):
    try:
        print("\033[1;34;1m") 
        if "how" in tokens and  "to" in tokens:
            tokens.remove("how")
            tokens.remove("to")
        query = ""
        for i in range(0, len(tokens)):
            query = query + str(tokens[i]) + " " 
        print("\nHazel : Do you want to search on \" How to ", query.strip(), "\"")
        que = input("        Continue? ")
        if que == 'y' or que == 'yes' or que == 'yeah' or que == 'ya':
            os.system("socli -t linux -iq " + query)
        elif que == 'n' or que == 'no' or que == 'nop' or que == 'na' or que == 'nah':
            query = input("\nHazel : Enter the search query : ")
            os.system("socli -t linux -iq " + query)
        else:
            print("\nHazel : It's more convinient if you could just type a 'y' or 'n'! Let's do that again.")
    except Exception as e:
        print("\nHazel : I hoped this to be a lot easier!!!")
        return