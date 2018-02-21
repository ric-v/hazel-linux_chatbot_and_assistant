#! /bin/bash

mkdir nltk_data/tokenizers
mkdir nltk_data/corpora

unzip -d nltk_data/tokenizers/ -o nltk_data/punkt.zip
unzip -d nltk_data/corpora/ -o nltk_data/stopwords.zip

rm -rf nltk_data/

mv nltk_data/nltk_data/ /usr/share/

sudo cp hazel /usr/bin/
sudo cp Hazel.desktop /usr/share/applications/

sudo pacman -Syy --force --noconfirm yaourt expac git most python2-pyqt4 make fakeroot gnome-terminal pacaur dialog

pip2 install -r requirements.txt


mkdir .local/share/applications

mv -f hazel.desktop.desktop ~/.local/share/applications/

echo "

"
echo "Hazel is ready to work"