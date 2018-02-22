#! /bin/bash

mkdir nltk_data/tokenizers
mkdir nltk_data/corpora

unzip -d nltk_data/tokenizers/ -o nltk_data/punkt.zip
unzip -d nltk_data/corpora/ -o nltk_data/stopwords.zip

rm -rf nltk_data/

mv nltk_data/nltk_data/ /usr/share/

sudo cp -rf hazel /usr/bin/
sudo cp -rf Hazel.desktop /usr/share/applications/

sudo pacman -Syy --force --noconfirm yaourt expac git most python2-pyqt4 make fakeroot gnome-terminal pacaur dialog

pip install -r requirements.txt

echo "

"
echo "Hazel is ready to work"