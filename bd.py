from tkinter import *
import sys
import cv2
import os
import argparse



def browseFiles():
    global window
    window = Tk()
    print("Kindly Run 1.py File")
    os.system('1.py')



users = { "username": "password"}

def beginning():
    global registerfirsterror
    global beginningwindow
    beginningwindow = Tk()
    beginningwindow.geometry("700x450+1000+530")

    chooseloginbutton = Button(beginningwindow, text="LOGIN", command=loginscript)
    chooseloginbutton.pack(fill=BOTH)
    chooseregisterbutton = Button(beginningwindow, text="REGISTER", command=registerscript)
    chooseregisterbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Training Image", command=browseFiles)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Image Filter", command=imagescript)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Image Blur", command=imagescript1)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Eriction", command=imagescript2)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Threshold", command=imagescript3)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Movedetection", command=imagescript4)
    choosetrainingbutton.pack(fill=BOTH)
    choosetrainingbutton = Button(beginningwindow, text="Imagecascading", command=imagescript5)
    choosetrainingbutton.pack(fill=BOTH)
    chooseexitbutton = Button(beginningwindow, text="EXIT", command=sys.exit)
    chooseexitbutton.pack(fill=BOTH)
    registerfirsterror = Label(beginningwindow)
    frame = Frame()
    frame.pack(pady=2)


# Register script


def registerscript():
    global regusername
    global regpassword
    global registerwindow
    global registerverifylabel
    registerwindow = Tk()
    registerwindow.geometry("455x190+1000+175")
    regusernamelabel = Label(registerwindow, text="Username : ")
    regusernamelabel.pack(fill=BOTH)
    regusername = Entry(registerwindow, width=32)
    regusername.pack()
    regpasswordlabel = Label(registerwindow, text="Password : ")
    regpasswordlabel.pack(fill=BOTH)
    regpassword = Entry(registerwindow, width=32)
    regpassword.pack()
    frame = Frame()
    frame.pack(pady=3)
    registerbutton = Button(registerwindow, text="REGISTER", command=registerverify)
    registerbutton.pack()
    frame = Frame()
    frame.pack(pady=2)
    backbutton = Button(registerwindow, text="BACK", command=beginning)
    backbutton.pack()
    registerverifylabel = Label(registerwindow)
    registerverifylabel.pack()


# Login script

def loginscript():
    global username
    global password
    global loginwindow
    global loginverifylabel
    try:
        registerverifylabel["text"] = ""
        loginwindow = Tk()
        loginwindow.geometry("215x160+1000+35")
        usernamelabel = Label(loginwindow, text="Username : ")
        usernamelabel.pack(fill=BOTH)
        username = Entry(loginwindow, width=32)
        username.pack()
        passwordlabel = Label(loginwindow, text="Password : ")
        passwordlabel.pack(fill=BOTH)
        password = Entry(loginwindow, width=32)
        password.pack()
        loginbutton = Button(loginwindow, text="LOGIN", command=loginverify)
        loginbutton.pack()
        frame = Frame()
        frame.pack(pady=2)
        backbutton = Button(loginwindow, text="BACK", command=beginning)
        backbutton.pack()
        loginverifylabel = Label(loginwindow)

    except NameError:
        registerfirsterror.pack()
        registerfirsterror["text"] = "Please Create Account ! "


def imagescript():
    os.system('imagesave.py')


def imagescript1():
    os.system('Imageblur.py')


def imagescript2():
    os.system('Eriction.py')


def imagescript3():
    os.system('Threshold.py')


def imagescript4():
    os.system('Movedetection.py')


def imagescript5():
    os.system('Imagecascading1.py')


def loginverify():
    frame = Frame()
    frame.pack(pady=3)
    loginverifylabel.pack(fill=BOTH)
    if username.get() in users.keys():
        if password.get() == users[username.get()]:
            loginverifylabel["text"] = "Login Successful ! "
        else:
            loginverifylabel["text"] = "Invalid username or password ! "
    else:
        loginverifylabel["text"] = "Invalid username or password ! "


def registerverify():
    if regusername.get() in users:
        frame = Frame()
        frame.pack(pady=2)
        registerverifylabel["text"] = "This Username Is Taken"
    else:
        users[
            regusername.get()] = regpassword.get()
        beginning()


beginning()  # Starting program
mainloop()
