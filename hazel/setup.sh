#! /bin/bash

mkdir nltk_data

unzip -d nltk_data/nltk_data/ -o nltk_data/punkt.zip
unzip -d nltk_data/nltk_data/ -o nltk_data/stopwords.zip

rm nltk_data/punkt.zip
rm nltk_data/stopwords.zip

mv nltk_data/nltk_data/ ~/