#! /bin/bash

mkdir nltk_data

unzip -d nltk_data/nltk_data/ nltk_data/punkit.zip
unzip -d nltk_data/nltk_data/ nltk_data/stopwords.zip

mv nltk_data/ ~/