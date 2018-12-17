#!/usr/bin/python3
#import sys
#print("{}.{}.{} on".format(*sys.version_info,*sys.platform),sys.platform)

import tkinter as tk
from tkinter import *
from tkinter import *
from Login import Login
from Login import center

class Events(tk.Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent) 
        label = tk.Label(text="Events")         
        label.pack()
        self.data = 42  

class Location(tk.Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent) 
        label = tk.Label(text="Location")         
        label.pack()
        self.data = 42 

class Chat(tk.Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent) 
        label = tk.Label(text="Chat")         
        label.pack()
        self.data = 42 

class Profile(tk.Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent) 
        label = tk.Label(text="Profile")         
        label.pack()
        self.data = 42 

class Settings(tk.Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent) 
        label = tk.Label(text="Settings")         
        label.pack()
        self.data = 42 


class App:
    def __init__(self):
        self.win = Tk()
        self.setFrames()
        self.addButtons(self.lframe)
        self.setWindow()
        self.win.mainloop()

    def setFrames(self):
        self.mainframe = tk.Frame(self.win)

        self.uframe = tk.Frame(self.mainframe)
        self.uframe.pack(side="top")

        self.label = tk.Label(self.uframe)
        self.label.pack()

        self.lframe = tk.Frame(self.mainframe)
        self.lframe.pack(side="bottom", fill="x")

        self.mainframe.pack(side = "bottom")
        

    def setWindow(self):
        self.win.title("Event App")
        self.win.resizable(0,0)
        self.win.geometry("330x500")
        center(self.win)

    def addButtons(self,frame):
        events = tk.Button(frame, text="Events")
        events.bind('<Button-1>',self.openEvents)
        self.setButton(events,"events.png")
        location = tk.Button(frame,text="Location")
        location.bind('<Button-1>',self.openLocation)
        self.setButton(location,"location.png")
        chat = tk.Button(frame, text="Chat",)
        chat.bind('<Button-1>',self.openChat)
        self.setButton(chat,"chat.png")
        profile = tk.Button(frame,text="Profile")
        profile.bind('<Button-1>',self.openProfile)
        self.setButton(profile,"profile.png")
        settings = tk.Button(frame,text="Settings")
        settings.bind('<Button-1>',self.openSettings)
        self.setButton(settings,"settings.png")

    def setButton(self,button,path): 
        #buttonPhoto = PhotoImage(file="src/Photos/"+path)
        #button.config(width="60",height="40",image=buttonPhoto)
        button.pack(side=LEFT)

    def openEvents(self):
        self.frame = Events(self.win)

    def openLocation(self):
        self.frame = Location(self.win)

    def openChat(self):
        self.frame = Chat(self.win)
    
    def openProfile(self):
        self.frame = Profile(self.win)
    
    def openSettings(self):
        self.frame = Settings(self.win)

if __name__ == "__main__":
    app = App()