#! /bin/bash

sudo pacman -Syy --force --noconfirm python-pip yaourt expac git gcc  most make fakeroot gnome-terminal pacaur dialog

mkdir nltk_data/tokenizers
mkdir nltk_data/corpora

unzip -d nltk_data/tokenizers/ -o nltk_data/punkt.zip
unzip -d nltk_data/corpora/ -o nltk_data/stopwords.zip

mv nltk_data/nltk_data/ /usr/share/

rm -rf nltk_data/

sudo cp -rf hazel /usr/bin/
sudo cp -rf Hazel.desktop /usr/share/applications/

pip install -r requirements.txt

echo "

"
echo "Hazel is ready to work"