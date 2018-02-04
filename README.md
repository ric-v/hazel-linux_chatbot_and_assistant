# Hazel - Linux Chatbot and System Assistant
<hr>

### What is it about?
Hazel aims to be a beginner-friendly, assistive chatbot. Many of us know the benefits of using a free OS (like Linux, BSD, etc), yet we never use it as our primary OS. It's a general knowledge now that proprietary software and vensors force us to use their technology without giving us a choice. In my personal experience, more than cost-effectiveness or free content I felt choices very necessary and appealing. <br/>Hazel enable you enjoy this freedom without having to bother about the painful learning curve associated with a linux system. Hazel simply lets you enjoy the "view" while it runs "linux commands in the background". Users need not bother about having to learn how it works or how to do things. Hazel automates more than what an average user would want out of their linux machine.

### Getting started!!!
There are no complexity associated with using this software. The only skill you'll ever need to use your linux system is the ability to read and type basic english. You can ask hazel to do some actions for you and be done with it. You can perform almost all the basic tasks you want by chating with this bot.<br>If you are *an absolute beginner *or* is interested in learning Linux* then join now. Grab **any Arch-based Linux** to get started.

### Really getting started...
You might need to grab the following to start using Hazel<br>
* **Manjaro Linux** *(Any arch -based Linux)* - I started this project exclusively for Arch-based linux since I found it more beginner friendly and appealing than other linux distributions out there (Sorry Ubuntu and other pop distros! That's a naked truth)

* **Python2 and pip** - Ummh!!! Not for coding or any other geek suff. Install these to make sure the testing release of Hazel works properly as long as a stable version is not released. 
 
 > sudo pacman -S python2-pip  
* **Ability to read and type in English** and the ability to open  **terminal** all by yourself.... LOL! JK...


Download [Manjaro Linux](http://manjaro.org/get-manjaro/)<br>or<br>
Get an [Arch-based Linux](https://en.wikipedia.org/wiki/Arch_Linux#Derivatives)

### Install and Run Hazel on your system...

If you are a new user, download git first<br>
> sudo pacman -S git <br>

Clone the repository to your deivce home :
> git clone https://github.com/illuminati-RV/hazel-linux_chatbot_and_assistant.git <br>

Change present location to the project folder<br>
> cd hazel-linux_chatbot_and_assistant/hazel/ <br>

Setup nltk_data (skip this step if you already have nltk_data folder in your home folder or anywhere else)
>./setup.sh<br>

This script only installs essential nltk data, to get the whole nltk data, open a python shell<br>
> python2<br>
> > import nltk<br>
> > nltk.download()

Download python modules
> pip install -r requirements.txt

Run the main.py file to get started with Hazel
> python2 main.py


<br><br>
### About this project
This is a small project initiated to bring more people to the FOSS world. You can modify the code to your liking and preferences for private usage. If you wish to publish your work to the public, make sure to include the license and source code along with the publication.<br>If you are interested in learning python or coding in python, get started with this project. You can contact me for more details.<br><center> **CODE . SHARE . PROSPER** </center>
