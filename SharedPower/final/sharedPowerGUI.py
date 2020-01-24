from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
import time
from tkinter import messagebox
import tkinter.messagebox as me
import sqlite3
from tkinter import Frame
from datetime import date
import datetime
import os
from tkinter import Tk, filedialog
from tkcalendar import *

conn = sqlite3.connect('form.db')
c = conn.cursor()
##class MainPage:
##    def __init__(self,master):
##        self.master=master
##        super(MainPage, self).__init__()
##
##    def progressBar(self):
##        self.logo_icon=ImageTk.PhotoImage(file="images/first.png")
##        title=Label(self.master, text='Lenden: the customers satisfaction', fg='black', bg='white',font=('times new roman',20,'bold'))
##        title.place(x=0,y=20,relwidth=1)
##
##        login_frame=Frame(self.master, bg="white")
##        login_frame.place(x=200,y=80)
##        logolbl1=Label(login_frame, image=self.logo_icon)
##        logolbl1.grid(row=0, column=1, pady=20)
##
##        self.button2 = ttk.Button(self.master, text = "Lets begin the journey with us!!", command = self.start_progressbar)
##        self.button2.place(x=200,y=400)
## 
##        self.progress_bar = ttk.Progressbar(self.master, orient = 'horizontal', length = 400, mode = 'indeterminate')
##        self.progress_bar.place(x=120,y=350)
## 
##    def start_progressbar(self):
##        self.progress_bar.start()



class Login(Frame):
    def __init__(self,master):
        self.master = master

        self.frame = Frame(master, bg='white')
        
        self.username = StringVar()
        self.password = StringVar()
        # All Images
        self.user_icon = PhotoImage(file="images/man-user.png")
        self.pass_icon = PhotoImage(file="images/password.png")
        self.logo_icon = PhotoImage(file="images/logo.png")

        title = Label(master, text="Login to your account", font=("times new roman", 18, "bold"), bg="white", fg="black",
                       relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(master, bg="white")
        Login_Frame.place(x=20, y=100)
        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0,column=1, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, width=18, textvariable=self.username, relief=GROOVE, font=("", 15))
        txtuser.grid(row=1, column=1, padx=10)
        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=2, column=0, padx=20, pady=20)
        txtpass = Entry(Login_Frame, bd=5, width=18, relief=GROOVE, textvariable=self.password, show='*', font=("", 15))
        txtpass.grid(row=2, column=1,
                     padx=20)
        btn_log = Button(master, text="Login", width=8, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", bd=4, command=self.login_info)
        btn_log.place(x=300, y=450)

        btn_can = Button(master, text="Cancel", width=8, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", bd=4, command=self.back)
        btn_can.place(x=100,y=450)
        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)

    def login_info(self):
        find_user = ('SELECT * FROM UserInfo WHERE Username = ? and Password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            me.showinfo("Login",
                       "Successfully logged in as buyer")
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        elif ((self.username.get())=="admin" and (self.password.get())=="admin"):
            print("success")
            me.showinfo("Login",'Successfully logged in as seller')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        elif ((self.username.get())=="insurance" and (self.password.get())=='insurance'):
            me.showinfo("Login",'Successfully logged in as Insurance')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = CheckTools(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        else:
            me.showerror('Oops!','Username Not Found.')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg="white")
            self.app = Login(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Login Page")

    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = SecondPage(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

#=======================================================================================================
            
class Registration(Frame):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, bg='white')
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        # All Images
        self.user_icon = PhotoImage(file="images/man-user.png")
        self.pass_icon = PhotoImage(file="images/password.png")
        self.logo_icon = PhotoImage(file="images/logo.png")

        title = Label(master, text="Create your Account", font=("times new roman", 18, "bold"), bg="white", fg="black",
                       relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(master, bg="white")
        Login_Frame.place(x=20, y=100)
        
        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0,column=1, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="FirstName", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, width=18, textvariable=self.firstname, relief=GROOVE, font=("", 15))
        txtuser.grid(row=1, column=1, padx=10)

        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0,column=1, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="LastName", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=2, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, width=18, textvariable=self.lastname, relief=GROOVE, font=("", 15))
        txtuser.grid(row=2, column=1, padx=10)

        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0,column=1, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=3, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, width=18, textvariable=self.username, relief=GROOVE, font=("", 15))
        txtuser.grid(row=3, column=1, padx=10)

        
        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=4, column=0, padx=20, pady=20)
        txtpass = Entry(Login_Frame, bd=5, width=18, relief=GROOVE, textvariable=self.password, show='*', font=("", 15))
        txtpass.grid(row=4, column=1,
                     padx=20)
        btn_log = Button(master, text="Register", width=8, bd=4, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", command=self.user_info)
        btn_log.place(x=300, y=550)
        
        btn_can = Button(master, text="Cancel", width=8, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", bd=4, command=self.back)
        btn_can.place(x=100,y=550)
        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)

    def user_info(self):
        self.firstname=self.firstname.get()
        self.lastname=self.lastname.get()
        self.username=self.username.get()
        self.password=self.password.get()
        c.execute('CREATE TABLE IF NOT EXISTS UserInfo(FirstName NOT NULL, LastName NOT NULL, Username UNIQUE NOT NULL, Password NOT NULL)')
        if (len(self.username)==0 or len(self.username)<=5) and (len(self.password)==0 or len(self.password)<=5):
            me.showerror('Registration Error','Fields must not be empty or username and password must be more than 5 characters')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master), bg='white')
            self.app = Registration(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Registration page")
            
        else:
            c.execute('SELECT * FROM UserInfo WHERE Username=?',(self.username,))
            conn.commit()
            if c.fetchall():
                me.showerror('User not found','Username already exists try with another username')
                self.master.withdraw()
                self.newWindow = Toplevel((self.master), bg='white')
                self.app = Registration(self.newWindow)
                self.newWindow.geometry('650x650')
                self.newWindow.title("Registration page")
            else:
                me.showinfo("Registration",
                       "Account successfully created!!")
                c.execute('INSERT INTO UserInfo(FirstName,LastName, Username,Password) VALUES(?,?,?,?)',(self.firstname, self.lastname, self.username, self.password))
                conn.commit()

                self.master.withdraw()
                self.newWindow = Toplevel((self.master), bg='white')
                self.app = Login(self.newWindow)
                self.newWindow.geometry('650x650')
                self.newWindow.title("Login page")

    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = SecondPage(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")



class SecondPage(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master, bg='white')
        #Label(master,text="Lenden: The Customer's Satisfaction",bg='white', fg='black').place(x=100,y=0)
        

        self.namaste_icon=ImageTk.PhotoImage(file="images/team.jpg")
        
        login_frame=Frame(master, bg="white")
        login_frame.place(x=60,y=50)
        logolbl1=Label(master, image=self.namaste_icon, bg='white')
        logolbl1.place(x=80,y=100)

        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)

##        self.photo = Image.open("images/namaste.png")
##        self.photo=self.photo.resize((300,300), Image.ANTIALIAS)
##        self.pic=ImageTk.PhotoImage(self.photo)
##        self.btn=Button(master, image=self.pic).place(x=100,y=0)
        Label(master,text="Lenden:",bg='white', fg='black', font=('new times roman',25)).place(x=150,y=15)
        Label(master,text="The customer's satisfaction",bg='white', fg='black', font=('new times roman',18)).place(x=150,y=55)
        
        self.photo = Image.open("images/login.jpg")
        self.photo=self.photo.resize((180,50), Image.ANTIALIAS)
        self.pic=ImageTk.PhotoImage(self.photo)
        self.btn=Button(master, image=self.pic, bd=1, command=self.logn, bg='white').place(x=200,y=410)

        self.photo1 = Image.open("images/register.png")
        self.photo1=self.photo1.resize((180,50), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, bd=2, command=self.reg, bg='white').place(x=200,y=510)
        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)
    def logn(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login window")
    def reg(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = Registration(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Signin window")




# creating tkinter window 
class UserHome(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master)
        self.tool_name = StringVar()
        #self.menubar = Menu(master)
##        #Label(master, text="Costumer's Panel", bg='white', fg='maroon', font=('new times roman',25)).place(x=200,y=20)
### Adding File Menu and commands 
##        self.file = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='File', menu = self.file) 
##        self.file.add_command(label ='New File', command = None) 
##        self.file.add_command(label ='Open...', command = None) 
##        self.file.add_command(label ='Save', command = None) 
##        self.file.add_separator() 
##        self.file.add_command(label ='Exit', command = root.destroy) 
##  
### Adding Edit Menu and commands 
##        self.edit = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
##        self.edit.add_command(label ='Cut', command = None) 
##        self.edit.add_command(label ='Copy', command = None) 
##        self.edit.add_command(label ='Paste', command = None) 
##        self.edit.add_command(label ='Select All', command = None) 
##        self.edit.add_separator() 
##        self.edit.add_command(label ='Find...', command = None) 
##        self.edit.add_command(label ='Find again', command = None) 
##  
### Adding Help Menu 
##        self.help_ = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='Help', menu = self.help_) 
##        self.help_.add_command(label ='Tk Help', command = None) 
##        self.help_.add_command(label ='Demo', command = None) 
##        self.help_.add_separator() 
##        self.help_.add_command(label ='About Tk', command = None)
#=======================================================================================================
##
##        self.photo3 = Image.open("images/l.png")
##        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
##        self.pic3 = ImageTk.PhotoImage(self.photo3)
##        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)
        
        self.photo_a = Image.open("images/calendar.png")
        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
        self.pic_a=ImageTk.PhotoImage(self.photo_a)
        Button(master, image=self.pic_a, command=self.calendar1).place(x=0,y=0)
##        self.calendar = Menu(self.menubar, tearoff = 0)
##        self.calendar.add_command( label='Calendar',command=self.calendar1)
##        self.menubar.add_cascade(image=self.pic_a, menu = self.calendar)
##        root.config(menu = self.menubar)
#=======================================================================================================

        self.photo_0 = Image.open("images/profile.png")
        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
        self.pic_0=ImageTk.PhotoImage(self.photo_0)
        Button(master, image=self.pic_0, command=self.profile2).place(x=590,y=0)
##        self.profile = Menu(self.menubar, tearoff = 0)
##        self.profile.add_command(label='Profile', command=self.profile2)
##        self.menubar.add_cascade(image=self.pic_0, menu = self.profile)
##        root.config(menu = self.menubar)
#========================================================================================================

        
        
        self.photo_ = Image.open("images/logout.png")
        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
        self.pic_=ImageTk.PhotoImage(self.photo_)
        Button(master, image=self.pic_, command=self.logOut).place(x=620,y=0)
##        self.logout = Menu(self.menubar, tearoff = 0)
##        self.logout.add_command(label='Logout', command=self.logOut)
##        self.menubar.add_cascade(image=self.pic_, menu = self.logout)
##        root.config(menu = self.menubar)
#==========================================================================================================
        self.photo = Image.open("images/search.jpg")
        self.photo=self.photo.resize((25,26), Image.ANTIALIAS)
        self.pic=ImageTk.PhotoImage(self.photo)
        self.btn=Button(master, image=self.pic, bd=0, command=self.search).place(x=413,y=20)
        self.ent = Entry(master, width=30, font=("", 12), bd=4, textvariable=self.tool_name).place(x=100, y=20)
        #self.tool_name = self.tool_name.get()
#=========================================================================================================
        self.photo1 = Image.open("images/search.png")
        self.photo1=self.photo1.resize((250,250), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, command=lambda:self.all_items(self.master)).place(x=60,y=80)
        self.lbl1=Label(master, text='All Tools', width=17, font=("", 18)).place(x=60, y=300)
#==========================================================================================================
        self.photo2 = Image.open("images/hire.png")
        self.photo2=self.photo2.resize((250,250), Image.ANTIALIAS)
        self.pic2=ImageTk.PhotoImage(self.photo2)
        self.btn2=Button(master,text='Hire Tools', image=self.pic2, command=self.hire).place(x=320,y=80)
        self.lbl2=Label(master, text='Hire Tools', width=17, font=("", 18)).place(x=320, y=300)
#=========================================================================================================   
        self.photo3 = Image.open("images/return.png")
        self.photo3 = self.photo3.resize((250,250), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.btn3 = Button(master,text='Return Tools', image=self.pic3, command=self.returns).place(x=60,y=340)
        self.lbl2=Label(master, text='Return Tools', width=17, font=("", 18)).place(x=60, y=560)
#=======================================================================================================        
        self.photo4 = Image.open("images/payment.png")
        self.photo4 = self.photo4.resize((250,250), Image.ANTIALIAS)
        self.pic4 = ImageTk.PhotoImage(self.photo4)
        self.btn4 = Button(master,text='Payment Tools', image=self.pic4, command=self.payment).place(x=320,y=340)
        self.lbl2=Label(master, text='Payment Tools', width=17, font=("", 18)).place(x=320, y=560)
#========================================================================================================

        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)

#========================================================================================================
    def search(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = SearchTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Search Tools itmes")
        Button(self.newWindow, text='Go to Home', font=("arial", 13, "bold"), width=10, bg='#1f3a93', fg='white'

               , command=self.back).place(x=250, y=350)
        c.execute('SELECT * FROM ToolsInfo WHERE ToolName=?',([self.tool_name.get()]))
        data=c.fetchall()
        if data:
            print("HELLO ")
            for value in data:
                a=value[0]
                b=value[1]
                print(a,b)
            self.lbl=Label(self.newWindow, text=data).place(x=40,y=50)
        else:
            me.showerror("Items error",'NO items found')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master), bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("All tool itmes")

    def back(self):
        self.master.withdraw()
        #self.newWindow = Toplevel((self.master),bg='white')
        self.app = UserHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("User Home")
               

    def all_items(self, home):
        self.home = home
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = AllTools(self.newWindow, self.home)
        self.newWindow.geometry('650x650')
        self.newWindow.title("All tool itmes")

    def hire(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = HireTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Hire Tools")
                                     
    def returns(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = ReturnTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Return Tools")

    def profile2(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = User1(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")

    def payment(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = PaymentTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Payment Tools")
                
    def logOut(self):
        me.showwarning("Logout",
                       "Are You sure want to LogOut?")
        self.master.withdraw()
        self.newWindow = Toplevel((self.master), bg='white')
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login Form")

    def calendar1(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = Calendar1(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Calendar")
    
#=====================================================================================================================
class AdminHome(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master)
        Label(master, text="Seller Panel", bg='white', fg='maroon', font=('new times roman',25)).place(x=200,y=20)
        
        self.menubar = Menu(master) 
### Adding File Menu and commands 
##        self.file = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='File', menu = self.file) 
##        self.file.add_command(label ='New File', command = None) 
##        self.file.add_command(label ='Open...', command = None) 
##        self.file.add_command(label ='Save', command = None) 
##        self.file.add_separator() 
##        self.file.add_command(label ='Exit', command = root.destroy) 
##  
### Adding Edit Menu and commands 
##        self.edit = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
##        self.edit.add_command(label ='Cut', command = None) 
##        self.edit.add_command(label ='Copy', command = None) 
##        self.edit.add_command(label ='Paste', command = None) 
##        self.edit.add_command(label ='Select All', command = None) 
##        self.edit.add_separator() 
##        self.edit.add_command(label ='Find...', command = None) 
##        self.edit.add_command(label ='Find again', command = None) 
##  
### Adding Help Menu 
##        self.help_ = Menu(self.menubar, tearoff = 0) 
##        self.menubar.add_cascade(label ='Help', menu = self.help_) 
##        self.help_.add_command(label ='Tk Help', command = None) 
##        self.help_.add_command(label ='Demo', command = None) 
##        self.help_.add_separator() 
##        self.help_.add_command(label ='About Tk', command = None)
#=======================================================================================================

        
        self.photo_a = Image.open("images/calendar.png")
        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
        self.pic_a=ImageTk.PhotoImage(self.photo_a)
        Button(master, image=self.pic_a, command=self.calendaar).place(x=0,y=0)
##        self.calendar = Menu(self.menubar, tearoff = 0)
##        self.calendar.add_command( label='Calendar',command=self.calendar)
##        self.menubar.add_cascade(image=self.pic_a, menu = self.calendar)
##        root.config(menu = self.menubar)
#=======================================================================================================

        self.photo_0 = Image.open("images/profile.png")
        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
        self.pic_0=ImageTk.PhotoImage(self.photo_0)
        Button(master, image=self.pic_0, command=self.profile1).place(x=590,y=0)
##        self.profile = Menu(self.menubar, tearoff = 0)
##        self.profile.add_command(label='Profile', command=self.profile1)
##        self.menubar.add_cascade(image=self.pic_0, menu = self.profile)
##        root.config(menu = self.menubar)
#========================================================================================================
        
        self.photo_ = Image.open("images/logout.png")
        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
        self.pic_=ImageTk.PhotoImage(self.photo_)
        Button(master, image=self.pic_, command=self.logOut).place(x=620,y=0)
##        self.logout = Menu(self.menubar, tearoff = 0)
##        self.logout.add_command(label='Logout', command=self.logOut)
##        self.menubar.add_cascade(image=self.pic_, menu = self.logout)
##        root.config(menu = self.menubar)

#=========================================================================================================

        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)
        
        self.photo1 = Image.open("images/search.png")
        self.photo1=self.photo1.resize((250,250), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, command=self.all_tools).place(x=60,y=150)
        self.lbl1=Label(master, text='All Tools', width=17, font=("", 18)).place(x=60, y=370)
        
        self.photo2 = Image.open("images/hire.png")
        self.photo2=self.photo2.resize((250,250), Image.ANTIALIAS)
        self.pic2=ImageTk.PhotoImage(self.photo2)
        self.btn2=Button(master, image=self.pic2, command=self.upload).place(x=320,y=150)
        self.lbl2=Label(master, text='Upload Tools', width=17, font=("", 18)).place(x=320, y=370)

        self.lbl=Label(master,text="@copyright from developers of lenden", bg="white").place(x=150,y=620)

    def all_tools(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = AllTools1(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("All tools")

    def upload(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = UploadTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")

    def profile1(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = User(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")
                
    def logOut(self):
        me.showwarning("Logout",
                       "Are You sure want to LogOut?")
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login Form")

    def calendaar(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Calendar")
    

#===========================================================================================================

class UploadTools(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master)
        self.tool_name = StringVar()
        self.tool_description = StringVar()
        self.tool_condition = StringVar()
        self.tool_halfday = StringVar()
        self.tool_fullday = StringVar()
        Label(master, text="Upload Tools", bg='white', fg='Maroon', width=20,font=("arial", 25)).place(x=140,y=10)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)
    
        self.label_name = Label(master, text="Name of Tool", bg='white', width=20,font=("arial", 17))
        self.label_name.place(x=30,y=110)
        self.entry_toolname = Entry(master,bd =5,font=("arial", 13), textvariable=self.tool_name)
        self.entry_toolname.place(x=280,y=110 ,width=200, height=38)
        self.label_tooldes = Label(master, text="Tool Description", bg="white", width=20,font=("arial", 17))
        self.label_tooldes.place(x=30,y=170)
        self.entry_tooldes = Entry(master,bd =5, font=("arial", 13), textvariable=self.tool_description)
        self.entry_tooldes.place(x=280,y=170,width=200, height=38)
        self.label_toolcondition = Label(master, text="Tool Condition", bg='white', width=20, font=("arial", 17))
        self.label_toolcondition.place(x=23, y=230)
        self.entry_toolcondition = Entry(master, bd=5, font=("arial", 13), textvariable=self.tool_condition)
        self.entry_toolcondition.place(x=280, y=230, width=200, height=38)
        self.label_rate = Label(master, text="Tool Rate", bg='white', width=20,font=("arial", 17))
        self.label_rate.place(x=150,y=300)
        self.label_fullrate = Label(master, text="Half Day Rate", bg='white', width=20,font=("arial", 17))
        self.label_fullrate.place(x=80,y=350)
        self.entry_toolrate = Entry(master, bd=5, font=("arial", 13), textvariable=self.tool_halfday)
        self.entry_toolrate.place(x=320, y=350, width=90, height=38)
        self.label_halfrate = Label(master, text="Full Day Rate",width=20, bg='white', font=("arial", 17))
        self.label_halfrate.place(x=80,y=400)
        self.entry_toolrate2 = Entry(master, bd=5, font=("arial", 13), textvariable=self.tool_fullday)
        self.entry_toolrate2.place(x=320, y=400, width=90, height=38)
        Button(master, text='Upload tool',font=("arial", 13,"bold"),width=10,bg='maroon',fg='white', command=self.uptools).place(x=50,y=475)
        Button(master, text='Upload image',font=("arial", 13,"bold"),width=10,bg='maroon',fg='white', command=self.upload_image).place(x=250,y=475)
        Button(master, text='Cancel',font=("arial", 13,"bold"),width=10,bg='maroon',fg='white', command=self.back).place(x=450,y=475)
        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)

    def uptools(self):
        self.tool_name = self.tool_name.get()
        self.tool_description = self.tool_description.get()
        self.tool_condition = self.tool_condition.get()
        self.tool_halfday = self.tool_halfday.get()
        self.tool_fullday = self.tool_fullday.get()
        if (len(self.tool_name)==0 or len(self.tool_description)==0 or len(self.tool_condition)==0 or len(self.tool_halfday)==0 or len(self.tool_fullday)==0):
            me.showerror('Incorrect Credientitals','No fields must be empty')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UploadTools(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Upload tools")
        else:
            me.showinfo("Uploads", 'Tools successfully uploaded')
            c.execute('CREATE TABLE IF NOT EXISTS ToolsInfo(ToolName NOT NULL, ToolDescription NOT NULL, ToolCondition NOT NULL, ToolHalfDay NOT NULL, ToolFullDay NOT NULL)')
            c.execute('INSERT INTO ToolsInfo(ToolName, ToolDescription, ToolCondition, ToolHalfDay, ToolFullDay) VALUES(?,?,?,?,?)',
                    (self.tool_name, self.tool_description, self.tool_condition, self.tool_halfday, self.tool_fullday))
            conn.commit()
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home page")
    

    def upload_image(self):
            me.showwarning("Before Uploading TooolImage!",
                    "You should upload details of tool first then you need to upload Tool Image.\n If you have uploaded ToolDetails then Click OK  to continue")
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UploadImage(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Upload Tools Form")
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

class UploadImage(Frame):
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.master.resizable(False, False)

    def create_widgets(self):
        self.select = Button(self.master,text='Select Image', font=("arial", 13, "bold"), bg="green", fg='white',command=self.select_image)
        self.select.pack()
        self.canvas = Canvas(self.master, width= 400, height=400, bg="grey")
        self.canvas.pack()
        self.store = Button(self.master, text='Store Image', font=("arial", 13, "bold"), bg="#e37b17", fg='white',command=self.store_image)
        self.store.pack()

    def select_image(self):
        global file_path
        file_path = filedialog.askopenfilename()
        des = Image.open(file_path)
        bg_image = ImageTk.PhotoImage(des)
        self.canvas.bg_image = bg_image
        self.canvas.create_image(200 , 200, image=self.canvas.bg_image)
        print(file_path)
    def store_image(self):
        self.store = file_path
        file = open("Text File Handling\image.txt", "a")
        file.write("ToolImage:    ")
        file.write(self.store)
        file.write("\n")
        file.close()
        me.showinfo("Successfully Uploaded ToolImage!", "Your selected image is uploaded in ToolImage Database.")
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Admin Home")



#==================================================================================================
class AllTools(Frame):
    def __init__(self, master, home):
        self.home = home
        self.master=master
        self.frame=Frame(master)


        self.pay_icon=ImageTk.PhotoImage(file="images/view.jpg")
        login_frame=Frame(master, bg="white")
        login_frame.place(x=0,y=0)
        logolbl1=Label(master, image=self.pay_icon, bg='white')
        logolbl1.place(x=0,y=0)



        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=500, y=0)

        self.lab=Label(master, text='ALL Tools',font=('new times roman',18), bg='white', fg='blue').place(x=150,y=20)
        Button(master, text='Go to Home', font=("arial", 13, "bold"), width=10, bg='maroon', fg='white', command=self.back).place(x=250, y=550)
        c.execute('SELECT * FROM ToolsInfo')
        data=c.fetchall()
        if data:
            for elem in data:
                self.a=elem[0]
                self.b=elem[1]
                self.d=elem[2]
                self.e=elem[3]
                self.f=elem[4]
            labl1=Label(master,text='Tool Name',bg='white',fg='blue').place(x=20,y=100)
            lbl2=Label(master, text='Tool Description',bg='white',fg='blue').place(x=20,y=130)
            lbl3=Label(master, text='Tool Condition',bg='white',fg='blue').place(x=20,y=160)
            lbl4=Label(master, text='Tool HalfDay rate',bg='white',fg='blue').place(x=20,y=190)
            lbl5=Label(master, text='Tool FullDay rate',bg='white',fg='blue').place(x=20,y=220)
            labl=Label(master, text=(self.a),bg='white',fg='blue').place(x=200,y=100)
            lab2=Label(master, text=(self.b),bg='white',fg='blue').place(x=200,y=130)
            lab3=Label(master, text=(self.d),bg='white',fg='blue').place(x=200,y=160)
            lab4=Label(master, text=(self.e),bg='white',fg='blue').place(x=200,y=190)
            lab4=Label(master, text=(self.f),bg='white',fg='blue').place(x=200,y=220)
        else:
            Labl=Label(master, text="No items Uploaded yet", bg='white').place(x=150,y=150)
            
    def back(self):
            self.master.destroy()
            self.home.deiconify()
##            self.newWindow = Toplevel((self.master),bg='white')
##            self.app = UserHome(self.newWindow)
##            self.newWindow.geometry('650x650')
##            self.newWindow.title("User Home")

class AllTools1:
    def __init__(self, master):
        self.master=master
        self.frame=Frame(master)


        self.pay_icon=ImageTk.PhotoImage(file="images/view.jpg")
        login_frame=Frame(master, bg="white")
        login_frame.place(x=0,y=0)
        logolbl1=Label(master, image=self.pay_icon, bg='white')
        logolbl1.place(x=0,y=0)



        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=500, y=0)

        self.lab=Label(master, text='ALL Tools',font=('new times roman',18), bg='white', fg='blue').place(x=150,y=20)
        Button(master, text='Go to Home', font=("arial", 13, "bold"), width=10, bg='maroon', fg='white', command=self.back).place(x=250, y=550)
        c.execute('SELECT * FROM ToolsInfo')
        data=c.fetchall()
        if data:
##            file=open('/home/niraj/Desktop/final/Text File Handling\image.txt')
##            f=file.readlines() 
##            imgd=ImageTk.PhotoImage([f])
##            panel=Label(image=imgd,height=28,width=30).pack()
            for elem in data:
                self.a=elem[0]
                self.b=elem[1]
                self.d=elem[2]
                self.e=elem[3]
                self.f=elem[4]
            #labl_img=Label(master, text=self.img).place(x=50,y=50)
            labl1=Label(master,text='Tool Name',bg='white',fg='blue').place(x=20,y=100)
            lbl2=Label(master, text='Tool Description',bg='white',fg='blue').place(x=20,y=130)
            lbl3=Label(master, text='Tool Condition',bg='white',fg='blue').place(x=20,y=160)
            lbl4=Label(master, text='Tool HalfDay rate',bg='white',fg='blue').place(x=20,y=190)
            lbl5=Label(master, text='Tool FullDay rate',bg='white',fg='blue').place(x=20,y=220)
            labl=Label(master, text=(self.a),bg='white',fg='blue').place(x=200,y=100)
            lab2=Label(master, text=(self.b),bg='white',fg='blue').place(x=200,y=130)
            lab3=Label(master, text=(self.d),bg='white',fg='blue').place(x=200,y=160)
            lab4=Label(master, text=(self.e),bg='white',fg='blue').place(x=200,y=190)
            lab4=Label(master, text=(self.f),bg='white',fg='blue').place(x=200,y=220)
        else:
            Labl=Label(master, text="No items Uploaded yet", bg='white').place(x=150,y=150)
            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")



class AllTools2:
    def __init__(self, master):
        self.master=master
        self.frame=Frame(master)


        self.pay_icon=ImageTk.PhotoImage(file="images/view.jpg")
        login_frame=Frame(master, bg="white")
        login_frame.place(x=0,y=0)
        logolbl1=Label(master, image=self.pay_icon, bg='white')
        logolbl1.place(x=0,y=0)



        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=500, y=0)

        self.lab=Label(master, text='ALL Tools',font=('new times roman',18), bg='white', fg='blue').place(x=150,y=20)
        Button(master, text='Go to Home', font=("arial", 13, "bold"), width=10, bg='maroon', fg='white', command=self.back).place(x=250, y=550)
        c.execute('SELECT * FROM ToolsInfo')
        data=c.fetchall()
        if data:
##            file=open('/home/niraj/Desktop/final/Text File Handling\image.txt')
##            f=file.readlines() 
##            imgd=ImageTk.PhotoImage([f])
##            panel=Label(image=imgd,height=28,width=30).pack()
            for elem in data:
                self.a=elem[0]
                self.b=elem[1]
                self.d=elem[2]
                self.e=elem[3]
                self.f=elem[4]
            #labl_img=Label(master, text=self.img).place(x=50,y=50)
            labl1=Label(master,text='Tool Name',bg='white',fg='blue').place(x=20,y=100)
            lbl2=Label(master, text='Tool Description',bg='white',fg='blue').place(x=20,y=130)
            lbl3=Label(master, text='Tool Condition',bg='white',fg='blue').place(x=20,y=160)
            lbl4=Label(master, text='Tool HalfDay rate',bg='white',fg='blue').place(x=20,y=190)
            lbl5=Label(master, text='Tool FullDay rate',bg='white',fg='blue').place(x=20,y=220)
            labl=Label(master, text=(self.a),bg='white',fg='blue').place(x=200,y=100)
            lab2=Label(master, text=(self.b),bg='white',fg='blue').place(x=200,y=130)
            lab3=Label(master, text=(self.d),bg='white',fg='blue').place(x=200,y=160)
            lab4=Label(master, text=(self.e),bg='white',fg='blue').place(x=200,y=190)
            lab4=Label(master, text=(self.f),bg='white',fg='blue').place(x=200,y=220)
        else:
            Labl=Label(master, text="No items Uploaded yet", bg='white').place(x=150,y=150)
            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = CheckTools(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")
            
            
            
#======================================================================================================
    
class SearchTools(Frame):
    def init__(self,master):
        self.master=master
        self.frame=Frame(master)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)

        Button(master, text='Go to Home', font=("arial", 13, "bold"), width=10, bg='#1f3a93', fg='white'

               , command=self.back).place(x=250, y=350)
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")
        
        #self.tool_name = self.tool_name.get()
##    def foo(self):
##        find_tools = ('SELECT * FROM ToolsInfo WHERE ToolName = ?')
##        c.execute(find_tools,[(self.tool_name.get())])
##        data = c.fetchall()
##        if data:
####            for elem in data:
####                a=elem[0]
####                b=elem[1]
####                d=elem[2]
####                e=elem[3]
####                f=elem[4]
####                self.lbl=Label(master, text=('Tool Name\t',a)).pack()
####                self.lb2=Label(master, text=('Tool Description\t',b)).pack()
####                self.lb3=Label(master, text=('Tool Condition', d)).pack()
####                self.lb4=Label(master, text=('Tool Half Day Rate', e)).pack()
####                self.lb5=Label(master, text=('Tool Full Day Rate', f)).pack()
        #self.gui=Label(master, text="hello and welcom to the world of python").place(x=10,y=20)
##        else:
##            lbl=Label(master, text='NO items found').pack()
                


#========================================================================================================

class HireTools(UploadTools):
    def __init__(self,master):
        global tool_name
        global want_rider
        self.master=master
        self.frame=Frame(master)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)

        self.hire_icon=ImageTk.PhotoImage(file="images/hiring.png")
        login_frame=Frame(master, bg="white")
        login_frame.place(x=0,y=20)
        logolbl1=Label(master, image=self.hire_icon, bg='white')
        logolbl1.place(x=15,y=150)

        self.label_head = Label(master, text="HIRE TOOL", width=20, font=("new times roman", 27),bg='white', fg='blue').place(x=100,y=25)

        
        self.label_toolname = Label(master, text="Tool Name", width=20, font=("arial", 17),bg='white', fg='blue')

        self.label_toolname.place(x=30, y=165)
        self.entry_toolname = Entry(master, bd=5, font=("arial", 13))


        self.entry_toolname.place(x=280, y=165, width=200, height=38)
        self.label_hireDate = Label(master, text="Hire Date", width=20, font=("arial", 17),bg='white', fg='blue')

        self.label_hireDate.place(x=30, y=235)

        self.Date = date.today()

        self.entry_hireDate = Entry(master, bd=5, font=("arial", 13))

        self.entry_hireDate.place(x=280, y=235, width=200, height=38)

        self.entry_hireDate.insert(0, self.Date)

        self.label_hireDays = Label(master, text="Hire Days", width=20, font=("arial", 17),bg='white', fg='blue')

        self.label_hireDays.place(x=23, y=305)

        self.entry_hireDays = Entry(master, bd=5, font=("arial", 13))

        self.entry_hireDays.place(x=280, y=305, width=200, height=38)

        self.entry_hireDays.insert(0, " Max 3 Days")

        self.label_rate = Label(master, text="Tool Rate", width=20, font=("arial", 17),bg='white', fg='blue')

        self.label_rate.place(x=30, y=375)

        self.tool_rate = Entry(master, bd=5, font=("arial", 13))

        self.tool_rate.place(x=280, y=375, width=90, height=38)

        self.tool_rate.insert(0, "200")

        self.label_fullrate = Label(master, text="Full Day", width=20, font=("arial", 10),bg='white', fg='blue')

        self.label_fullrate.place(x=243, y=418)

        self.tool_rate2 = Entry(master, bd=5, font=("arial", 13))

        self.tool_rate2.place(x=390, y=375, width=90, height=38)

        self.tool_rate2.insert(0, "100")

        self.label_halfrate = Label(master, text="Half Day", width=20, font=("arial", 10),bg='white', fg='blue')

        self.label_halfrate.place(x=353, y=418)

        Button(master, text='Hire This Tool', font=("arial", 13, "bold"), width=15, bg='maroon', fg='white'

               , command=self.hire_tools).place(x=100, y=480)
        Button(master, text='Cancel', font=("arial", 13, "bold"), width=10, bg='maroon', fg='white'

               , command=self.cancel).place(x=320, y=480)

    def hire_tools(self):
        self.nameTool = self.entry_toolname.get()

        self.HireDate = self.entry_hireDate.get()

        self.HireDays = self.entry_hireDays.get()

        self.FullRate = self.tool_rate2.get()

        self.HalfRate = self.tool_rate.get()
        if (len(self.nameTool)==0 or len(self.HireDays)==0):
            me.showerror("Tool Upload Error","Please insert the correct credientials")
        else:
            self.nameTool = self.entry_toolname.get()

            self.HireDate = self.entry_hireDate.get()

            self.HireDays = self.entry_hireDays.get()

            self.FullRate = float(self.tool_rate2.get())

            self.HalfRate = float(self.tool_rate.get())

##            self.InsurancePlus = self.HalfRate + 10.00
##
##            self.InsurancePlus2 = self.FullRate + 10.00

            self.Date = date.today()

            c.execute('CREATE TABLE IF NOT EXISTS MyTools(ToolName NOT NULL, ToolDescription NOT NULL, ToolCondition NOT NULL, FullRate NOT NULL, HalfRate NOT NULL, HiredDate NOT NULL)')
            c.execute('SELECT * FROM ToolsInfo WHERE ToolName=?',(self.nameTool,))
            data=c.fetchall()
            if data:
                for i in data:
                    self.a=i[0]
                    self.b=i[1]
                    self.c=i[2]
                    self.d=i[3]
                    self.e=i[4]
                    self.curr_date = datetime.datetime.now()
                    self.g = self.curr_date.strftime('%Y-%m-%d')
                c.execute('INSERT INTO MyTools(ToolName, ToolDescription, ToolCondition, FullRate, HalfRate,HiredDate) VALUES(?,?,?,?,?,?)',
                      (self.nameTool, self.b, self.c, self.FullRate, self.HalfRate,self.g))
                c.execute("DELETE FROM ToolsInfo WHERE ToolName=?", (self.nameTool,))
                conn.commit()
                self.master.withdraw()
                self.newWindow = Toplevel((self.master),bg='white')
                self.app = Rider(self.newWindow)
                self.newWindow.geometry('650x650')
                self.newWindow.title("User Home")
            else:
                me.showerror('Not Found',"items not found")
                self.master.withdraw()
                self.newWindow = Toplevel((self.master),bg='white')
                self.app = HireTools(self.newWindow)
                self.newWindow.geometry('650x650')
                self.newWindow.title("All tool itmes")
            
    def cancel(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

    def rider(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = Rider(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")
        
             

#=========================================================================================================
class ReturnTools(HireTools):
    def __init__(self,master):
        self.master=master
        self.frame=Frame(master)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)

        self.pay_icon=ImageTk.PhotoImage(file="images/ret.jpg")
        login_frame=Frame(master, bg="white")
        login_frame.place(x=0,y=0)
        logolbl1=Label(master, image=self.pay_icon, bg='white')
        logolbl1.place(x=0,y=0)
        
        self.label_toolname = Label(master, text="Tool Name", width=20, font=("arial", 17), bg='white')

        self.label_toolname.place(x=30, y=165)
        self.entry_toolname = Entry(master, bd=5, font=("arial", 13))

        self.entry_toolname.place(x=280, y=165, width=200, height=38)
        Button(master, text='Return this Tool', font=("arial", 13, "bold"), width=15, bg='#1f3a93', fg='white'

               , command=self.return_tools).place(x=100, y=464)
        Button(master, text='Cancel', font=("arial", 13, "bold"), width=10, bg='#1f3a93', fg='white'

               , command=self.back).place(x=320, y=464)
        c.execute('SELECT * FROM MyTools')
        data=c.fetchall()
        if data:
            self.lbl=Label(master, text=data, bg='white').place(x=40,y=50)
        else:
            me.showerror("Items error",'NO items to return')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("All tool itmes")
        

    def return_tools(self):
        self.nameTool = self.entry_toolname.get()

        c.execute('SELECT * FROM MyTools WHERE ToolName=?',(self.nameTool,))
        data=c.fetchall()
        if data:
            for value in data:
                self.a=value[0]
                self.b=value[1]
                self.d=value[2]
                self.e=value[3]
                self.f=value[4]
                self.g=value[5]

            c.execute('INSERT INTO ToolsInfo(ToolName, ToolDescription, ToolCondition, ToolHalfDay, ToolFullDay) VALUES(?,?,?,?,?)',
                      (self.a, self.b, self.d, self.e, self.f))
            c.execute("DELETE FROM MyTools WHERE ToolName=?", (self.nameTool,))
            conn.commit()
            me.showinfo("Return Successful",'Successfully return your tool')
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("All tool itmes")
        else:
            me.showerror('Not Found',"items not found")
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = ReturnTools(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("All tool itmes")

            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")
        
        
        

#=========================================================================================================
class PaymentTools(Frame):
    def __init__(self,master):
        self.master=master
        self.frame=Frame(master)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)
        
##        self.pay_icon=ImageTk.PhotoImage(file="")
##        login_frame=Frame(master, bg="white")
##        login_frame.place(x=0,y=0)
##        logolbl1=Label(master, image=self.pay_icon, bg='white')
##        logolbl1.place(x=0,y=0)
        
        self.pay13 = Label(master, text="Invoice ", font=("arial", 18, "bold"),bg='white', fg='blue').place(x=250, y=30)

        c.execute('SELECT * FROM MyTools')
        data=c.fetchall()
        if data:
            for value in data:
                half_day=value[4]
                insurance_halfday=0.5*half_day
                halfday_total=half_day+insurance_halfday
                full_day=value[3]
                insurance_fullday=0.5*full_day
                fullday_total=full_day+insurance_fullday
                
            labl1=Label(master,text='Tool HalfDay rate',bg='white').place(x=20,y=100)
            lbl2=Label(master, text='Insurance FullDay rate',bg='white').place(x=20,y=130)
            lbl3=Label(master, text='Tool FullDay rate',bg='white').place(x=20,y=160)
            lbl4=Label(master, text='Insurance FullDay rate',bg='white').place(x=20,y=190)
            lbl5=Label(master, text='Total HalfDay Rate',bg='white').place(x=20,y=220)
            lbl5=Label(master, text='Total FullDay Rate',bg='white').place(x=20,y=250)
                
            labl=Label(master, text=(half_day),bg='white').place(x=200,y=100)
            lab2=Label(master, text=(insurance_halfday),bg='white').place(x=200,y=130)
            lab3=Label(master, text=(halfday_total),bg='white').place(x=200,y=160)
            lab4=Label(master, text=(full_day),bg='white').place(x=200,y=190)
            lab4=Label(master, text=(insurance_fullday),bg='white').place(x=200,y=220)
            lab4=Label(master, text=(fullday_total),bg='white').place(x=200,y=250)
      
        else:
            Labl=Label(master, text="ALL due has been cleared!!",bg="white", fg='black').place(x=200,y=200)
        self.pay_tools = Button(master, text="Go to Home", bg='maroon', fg='white', command=self.back)

        self.pay_tools.place(x=250, y=500)

            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

#===========================================================================================================

class CheckTools(Frame):
    def __init__(self, master):
        self.master=master
        self.frame=Frame((master), bg='white')
        self.menubar = Menu(master)
        Label(master, text="Insurance Panel", bg='white', fg='maroon', font=('new times roman',25)).place(x=200,y=20)

#=======================================================================================================
##
##        
##        self.photo_a = Image.open("images/calendar.png")
##        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
##        self.pic_a=ImageTk.PhotoImage(self.photo_a)
##        self.calendar = Menu(master, tearoff = 0)
##        self.calendar.add_command( label='Calendar',command=self.calendar)
##        self.menubar.add_cascade(image=self.pic_a, menu = self.calendar)
##        root.config(menu = self.menubar)
###=======================================================================================================
##
##        self.photo_0 = Image.open("images/profile.png")
##        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
##        self.pic_0=ImageTk.PhotoImage(self.photo_0)
##        self.profile = Menu(self.menubar, tearoff = 0)
##        self.profile.add_command(label='Profile', command=self.profile)
##        self.menubar.add_cascade(image=self.pic_0, menu = self.profile)
##        root.config(menu = self.menubar)
###========================================================================================================
##        
##        self.photo_ = Image.open("images/logout.png")
##        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
##        self.pic_=ImageTk.PhotoImage(self.photo_)
##        self.logout = Menu(self.menubar, tearoff = 0)
##        self.logout.add_command(label='Logout', command=self.logOut)
##        self.menubar.add_cascade(image=self.pic_, menu = self.logout)
##        root.config(menu = self.menubar)


        self.photo3 = Image.open("images/l.png")
        self.photo3 = self.photo3.resize((120,120), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.lbl2=Label(master, image=self.pic3, bd=0, bg="white").place(x=0, y=0)

        self.photo_a = Image.open("images/calendar.png")
        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
        self.pic_a=ImageTk.PhotoImage(self.photo_a)
        Button(master, image=self.pic_a, command=self.calendaar).place(x=560,y=0)


        self.photo_0 = Image.open("images/profile.png")
        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
        self.pic_0=ImageTk.PhotoImage(self.photo_0)
        Button(master, image=self.pic_0, command=self.profile1).place(x=590,y=0)

        
        self.photo_ = Image.open("images/logout.png")
        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
        self.pic_=ImageTk.PhotoImage(self.photo_)
        Button(master, image=self.pic_, command=self.logOut).place(x=620,y=0)

        self.photo1 = Image.open("images/profile.jpg")
        self.photo1=self.photo1.resize((250,250), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, command=self.profile1)
        self.btn1.place(x=60,y=150)
        self.lbl1=Label(master, text='View Profile', width=17, font=("", 18)).place(x=60, y=370)
#==========================================================================================================
        self.photo2 = Image.open("images/hire.png")
        self.photo2=self.photo2.resize((250,250), Image.ANTIALIAS)
        self.pic2=ImageTk.PhotoImage(self.photo2)
        self.btn2=Button(master, image=self.pic2, command=self.all_tools).place(x=320,y=150)
        self.lbl2=Label(master, text='All Tools', width=17, font=("", 18)).place(x=320, y=370)

        self.lbl=Label(master,text="@copyright from developers", bg="white").place(x=150,y=620)

    def logOut(self):
        me.showwarning("Logout",
                       "Are You sure want to LogOut?")
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login Form")

    def profile1(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = User(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

    def all_tools(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = AllTools2(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")


    def calendaar(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Calendar")
    

#================================================================================================================================

class User(Frame):
    def __init__(self,master):
        self.master=master
        self.frame=Frame
        Label(master, text='Profile', font=('arial', 15),bg='white', fg='maroon').place(x=200,y=20)
        Button(master, text='Go to Home', font=('arial', 12),bg='maroon', fg='white', command=self.back).place(x=200,y=450)
        c.execute('SELECT * FROM UserInfo')
        details=c.fetchall()
        if details:
            for detail in details:
                self.firstname=detail[0]
                self.lastname=detail[1]
                self.username=detail[2]
                self.password=detail[3]
                labl1=Label(master,text='First Name',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=100)
                lbl2=Label(master, text='Last Name',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=130)
                lbl3=Label(master, text='Username',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=160)
                lbl4=Label(master, text='Password',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=190)

                labl=Label(master, text=(self.firstname),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=100)
                lab2=Label(master, text=(self.lastname),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=130)
                lab3=Label(master, text=(self.username),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=160)
                lab4=Label(master, text=(self.password),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=190)

        else:
            Label(master,text='No accounts are registerd yet', bg='white').place(x=250,y=250)

            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = CheckTools(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

class User1(Frame):
    def __init__(self,master):
        self.master=master
        self.frame=Frame
        Label(master, text='Profile', font=('arial', 15),bg='white', fg='maroon').place(x=200,y=20)
        Button(master, text='Go to Home', font=('arial', 12),bg='maroon', fg='white', command=self.back).place(x=200,y=450)
        c.execute('SELECT * FROM UserInfo')
        details=c.fetchall()
        if details:
            for detail in details:
                self.firstname=detail[0]
                self.lastname=detail[1]
                self.username=detail[2]
                self.password=detail[3]
                labl1=Label(master,text='First Name',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=100)
                lbl2=Label(master, text='Last Name',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=130)
                lbl3=Label(master, text='Username',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=160)
                lbl4=Label(master, text='Password',bg='white',fg='blue', font=('new times roman',12)).place(x=20,y=190)

                labl=Label(master, text=(self.firstname),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=100)
                lab2=Label(master, text=(self.lastname),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=130)
                lab3=Label(master, text=(self.username),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=160)
                lab4=Label(master, text=(self.password),bg='white',fg='blue', font=('new times roman',12)).place(x=200,y=190)
        else:
            Label(master,text='No accounts are registerd yet', bg='white').place(x=250,y=250)

            
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

#=======================================================================================================================

class Calendar1(Frame):
    def __init__(self, master):
        self.master=master
        self.frame=Frame(master)
        Button(master, text='Go to Home',command=self.back, bg='maroon',fg='white').place(x=250, y=300)
        cal = Calendar(root, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2020, month=1, day=22, bg='midnight blue', height=200).pack(fill='both')
    def back(self):
            self.master.withdraw()
            self.newWindow = Toplevel((self.master),bg='white')
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("User Home")

class Rider(Frame):
    def __init__(self,master):
        global entry_toolname
        global want_rider
        self.master=master
        self.frame=Frame(master)
        Label(master, text='Rider Profile', bg='White', fg='maroon',font=('new times roman',18)).place(x=150,y=10)
        Label(master, text='id', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=50)
        Label(master, text='Name', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=80)
        Label(master, text='Email', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=110)
        Label(master, text='Contact', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=140)

        Label(master, text='001', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=50)
        Label(master, text='Aayush Khanal', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=80)
        Label(master, text='ayushkhanal@gmail.com', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=110)
        Label(master, text='**********', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=140)
        
        Label(master, text='id', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=200)
        Label(master, text='Name', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=230)
        Label(master, text='Email', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=260)
        Label(master, text='Contact', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=290)

        Label(master, text='002', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=200)
        Label(master, text='Santosh Shahi Thakuri', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=230)
        Label(master, text='santoshshahi@gmail.com', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=260)
        Label(master, text='**********', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=290)

                
        Label(master, text='id', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=340)
        Label(master, text='Name', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=370)
        Label(master, text='Email', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=400)
        Label(master, text='Contact', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=430)

        Label(master, text='003', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=340)
        Label(master, text='Roshan Bist', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=370)
        Label(master, text='roshanbist@gmail.com', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=400)
        Label(master, text='**********', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=430)

        Label(master, text='id', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=480)
        Label(master, text='Name', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=510)
        Label(master, text='Email', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=540)
        Label(master, text='Contact', bg='White', fg='blue',font=('new times roman',10)).place(x=10,y=570)

        Label(master, text='004', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=480)
        Label(master, text='Niraj Poudel', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=510)
        Label(master, text='nirajpoudel@gmail.com', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=540)
        Label(master, text='**********', bg='White', fg='blue',font=('new times roman',10)).place(x=100,y=570) 

        Button(master, text="Cancel", bg='maroon', fg='white', command=self.back).place(x=100, y=600)
        Button(master, text="Wanna Continue", bg='maroon', fg='white', command=self.next).place(x=300, y=600)

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = HireTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("User Home")

    def next(self):
        self.master.withdraw()
        self.newWindow = Toplevel((self.master),bg='white')
        self.app = HireTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("User Home")
        me.showinfo("Hire Success","Successfully hire the tool")
        
            
        

root=Tk()
root.title('Shared Power')
root.geometry('650x650')
#obj=MainPage(root)
#obj.progressBar()
#Login(root)
#Registration(root)
#UserHome(root)
#AdminHome(root)
SecondPage(root)
#UploadTools(root)
#SearchTools(root)
#AllTools1(root)
#HireTools(root)
#ReturnTools(root)
#PaymentTools(root)
#CheckTools(root)
#User(root)
#Calendar1(root)
#Rider(root)
root.configure(bg="white")
root.mainloop()
