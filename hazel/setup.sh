#! /bin/bash

mkdir nltk_data

unzip -d nltk_data/nltk_data/ -o nltk_data/punkt.zip
unzip -d nltk_data/nltk_data/ -o nltk_data/stopwords.zip

rm punkt.zip
rm stopwords.zip

mv nltk_data/ ~/