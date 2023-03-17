"""from tkinter import *
from tkinter import messagebox
#creating the application main window.
top = Tk()
top.geometry("600x400")
u_name = StringVar()
u_pass = StringVar()
large_font = ('Verdana', 15)
top.title("Login")


def checkuser():
    get_name = u_name.get().strip()
    get_pass = u_pass.get().strip()
    print("Name:", get_name, ",", "Password:", get_pass)
    #-----validation here


def login():



    #creating label
    uname = Label(top, text = "Username",font=large_font).place(x = 30,y = 50)
    e1 = Entry(top,width = 20,textvariable=u_name,font=large_font).place(x = 100, y = 50)

    #creating label
    password = Label(top, text = "Password",font=large_font).place(x = 30, y = 90)
    e2 = Entry(top, width = 20,textvariable=u_pass,font=large_font).place(x = 100, y = 90)

    sbmitbtn = Button(top, text = "Submit",activebackground = "pink",font=large_font, activeforeground = "blue",command=checkuser).place(x = 30, y = 120)

    top.mainloop()

login()"""

from tkinter import *
from tkinter import messagebox
#creating the application main window.
top = Tk()
top.geometry("600x400")
u_name = StringVar()
u_pass = StringVar()
large_font = ('Verdana', 15)
top.title("Login")


def checkuser():
    get_name = u_name.get().strip()
    get_pass = u_pass.get().strip()
    print("Name:", get_name, ",", "Password:", get_pass)



    top.withdraw()
    print("done....")

    #-----validation here
    adminhome()

def adminhome():
    master1 = Toplevel()
    master1.title("Admin Home")
    master1.state("zoomed")
    master1.mainloop()


def login():
    #creating label
    uname = Label(top, text = "Username",font=large_font).place(x = 30,y = 50)
    e1 = Entry(top,width = 20,textvariable=u_name,font=large_font).place(x = 140, y = 50)

    #creating label
    password = Label(top, text = "Password",font=large_font).place(x = 30, y = 90)
    e2 = Entry(top, width = 20,textvariable=u_pass,font=large_font,show="*").place(x = 140, y = 90)
    sbmitbtn = Button(top, text="Cancel", activebackground="pink", font=large_font, activeforeground="blue", command=top.destroy).place(x=300, y=130)

    sbmitbtn = Button(top, text = "Submit",activebackground = "pink",font=large_font, activeforeground = "blue",command=checkuser).place(x = 200, y = 130)

    top.mainloop()

login()


