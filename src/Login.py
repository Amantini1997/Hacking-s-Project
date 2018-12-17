#!/usr/bin/python3
#import sys
#print("{}.{}.{} on".format(*sys.version_info,*sys.platform),sys.platform)
from tkinter import *
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as box


class Login:
    def __init__(self):
        self. window = Tk()
        self.window.geometry("330x500")
        self.window.resizable(0,0)
        self.window.title('Login Page')
        center(self.window)

        frame = Frame(self.window)

        Label1 = Label(self.window,text = 'Username:')
        Label1.pack(padx=15,pady= 5)

        self.entry1 = Entry(self.window,bd =5)
        self.entry1.pack(padx=15, pady=5)
        self.entry1.focus_force()



        Label2 = Label(self.window,text = 'Password: ')
        Label2.pack(padx = 15,pady=6)

        self.entry2 = Entry(self.window, bd=5, show="•")
        self.entry2.pack(padx = 15,pady=7)

        btn = Button(frame, text = 'Check Login',command = self.dialog1)
        btn.pack(side = RIGHT , padx =5)
        frame.pack(padx=100,pady = 19)
        self.window.mainloop()

    def dialog1(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if (username == 'admin' and  password == 'secret'):
            self.window.destroy()
        else:
            box.showinfo('info','Invalid Login')

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

login = Login()
    # def __init__(self,parent):
    #     self.win = gui("LOOP Login")#,"330x500")
    #     self.win.addLabelEntry("Username")
    #     self.win.addLabelSecretEntry("Password ")
    #     self.win.setPadding([20,20])
    #     self.win.addButtons(["Log in", "Register"], self.press, colspan = 2)
    #     self.win.setBg("green")
    #     self.win.setFont(18)
    #     self.win.setResizable(False)
    #     self.win.setFocus("Username")
    #     self.win.go()
        
    # def press(self,button):
    #     if button == "Cancel":
    #         self.win.stop()
    #     else:
    #         self.shake(loginCorrect)
    #         usr = self.win.getEntry("Username")
    #         pwd = self.win.getEntry("Password")
    #         print("User:", usr, "Pass:", pwd)

    # def shake(self,loginCorrect):
    #     if loginCorrect:
    #         self.win.errorBox("User and Password don't macth")
    #     else :
    #         Print("Logged in")