import os,sys,subprocess,shutil
import tkFileDialog
from Tkinter import *
root=Tk()
root.withdraw()
from tkMessageBox import *
def create(filename):
    showinfo("Warning","Path to create the file")
    path=tkFileDialog.askdirectory()
    print path+"/"+filename+".txt"
    f=open(path+"/"+filename+".txt",'w+')
    f.close()
def openfiles():
    showinfo("Hazel","Select a file to run")
    path=tkFileDialog.askopenfilename()
    if sys.platform=="win32":
      os.startfile(path)
    else:
      opener="open" if sys.platform =="darwin" else "xdg-open"
      subprocess.call([opener,path])
def delete():
    showinfo("Warning","Path to the file")
    path=tkFileDialog.askopenfilename()
    os.remove(path)
def writing(data):
    showinfo("Warning","Path to the file")
    path=tkFileDialog.askopenfilename()
    f=open(path,'w+')
    f.write(data)
    f.close()
def append(data):
    showinfo("Warning","Path to the file")
    path=tkFileDialog.askopenfilename()
    f=open(path,'a+')
    f.write(data)
    f.close()
def rename(data):
    showinfo("Warning","Path to the file")
    path=tkFileDialog.askopenfilename()
    os.rename(path,path+data+".txt")
def move():
    showinfo("Warning","Path to the source file")
    path1=tkFileDialog.askopenfilename()
    showinfo("Warning","Path to the destination location")
    path2=tkFileDialog.askdirectory()
    shutil.move(path1,path2)
def remove():
    showinfo("Warning","Path to remove the folder")
    path=tkFileDialog.askdirectory()
    os.rmdir(path)
def createf(data):
    showinfo("Warning","Path to create the folder")
    path=tkFileDialog.askdirectory()
    print path+"/"+data
    os.mkdir(path+"/"+data)
def lstdir():
    showinfo("Warning","Path to display the folder contents")
    path=tkFileDialog.askdirectory()
    s=os.listdir(path)
    print "Folder Contents"
    print20*"*"
    for i in s:
        print i
