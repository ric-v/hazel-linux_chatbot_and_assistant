#! /bin/bash

mkdir nltk_data/tokenizers
mkdir nltk_data/corpora

unzip -d nltk_data/tokenizers/ -o nltk_data/punkt.zip
unzip -d nltk_data/corpora/ -o nltk_data/stopwords.zip

rm -rf nltk_data/

mv nltk_data/nltk_data/ ~/

sudo pacman -Syy expac git

sudo pacman -U p*.tar.xz
sudo pacman -U co*.tar.xz

rm p*.tar.xz
rm c*.tar.xz