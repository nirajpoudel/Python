from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
import time
from tkinter import messagebox
import tkinter.messagebox as me
import sqlite3
from tkinter import Frame

conn = sqlite3.connect('form.db')

c = conn.cursor()
class MainPage:
    def __init__(self,master):
        self.master=master
        super(MainPage, self).__init__()

    def progressBar(self):
        self.logo_icon=ImageTk.PhotoImage(file="images/first.png")
        title=Label(self.master, text='The ultimate shared power', fg='black', bg='white',font=('times new roman',20,'bold'))
        title.place(x=0,y=20,relwidth=1)

        login_frame=Frame(self.master, bg="white")
        login_frame.place(x=200,y=80)
        logolbl1=Label(login_frame, image=self.logo_icon)
        logolbl1.grid(row=0, column=1, pady=20)

        self.button2 = ttk.Button(self.master, text = "Lets begin the journey with us!!", command = self.start_progressbar)
        self.button2.place(x=200,y=400)
 
        self.progress_bar = ttk.Progressbar(self.master, orient = 'horizontal', length = 400, mode = 'indeterminate')
        self.progress_bar.place(x=120,y=350)
 
    def start_progressbar(self):
        self.progress_bar.start()



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
        btn_log = Button(Login_Frame, text="Login", width=8, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", bd=4, command=self.login_info)
        btn_log.grid(row=3, column=1, pady=10)

    def login_info(self):
        find_user = ('SELECT * FROM UserInfo WHERE Username = ? and Password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            me.showinfo("Login",
                       "Successfully logged in as buyer")
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        elif ((self.username.get())=="admin" and (self.password.get())=="admin"):
            print("success")
            me.showinfo("Login",'Successfully logged in as seller')
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        elif ((self.username.get())=="insurance" and (self.password.get())=='insurance'):
            me.showinfo("Login",'Successfully logged in as Insurance')
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home Page")
            
        else:
            me.showerror('Oops!','Username Not Found.')
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = Login(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Login Page")

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
        btn_log = Button(Login_Frame, text="Register", width=8, bd=4, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", command=self.user_info)
        btn_log.grid(row=5, column=1, pady=10)

    def user_info(self):
        self.firstname=self.firstname.get()
        self.lastname=self.lastname.get()
        self.username=self.username.get()
        self.password=self.password.get()
        c.execute('CREATE TABLE IF NOT EXISTS UserInfo(FirstName NOT NULL, LastName NOT NULL, Username UNIQUE NOT NULL, Password NOT NULL)')
        if (len(self.username)==0 and len(self.password)==0):
            me.showerror('Registration Error','Fields must not be empty')
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = Registration(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Registration page")
            
        else:
            me.showinfo("Registration",
                       "Account successfully created?")
            c.execute('INSERT INTO UserInfo(FirstName,LastName, Username,Password) VALUES(?,?,?,?)',(self.firstname, self.lastname, self.username, self.password))
            conn.commit()

            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app = Login(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Login page")



class SecondPage(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master, bg='white')
        

        self.namaste_icon=ImageTk.PhotoImage(file="images/namaste.png")
        
        login_frame=Frame(master, bg="white")
        login_frame.place(x=60,y=0)
        logolbl1=Label(master, image=self.namaste_icon, bg='white')
        logolbl1.place(x=50,y=0)
        
        self.photo = Image.open("images/login.jpg")
        self.photo=self.photo.resize((250,50), Image.ANTIALIAS)
        self.pic=ImageTk.PhotoImage(self.photo)
        self.btn=Button(master, image=self.pic, bd=3, command=self.logn).place(x=160,y=430)

        self.photo1 = Image.open("images/register.jpg")
        self.photo1=self.photo1.resize((250,60), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, bd=3, command=self.reg).place(x=160,y=530)
    def logn(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login window")
    def reg(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Signin window")




# creating tkinter window 
class UserHome(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master)
        self.tool_name = StringVar()
        self.menubar = Menu(master) 
# Adding File Menu and commands 
        self.file = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='New File', command = None) 
        self.file.add_command(label ='Open...', command = None) 
        self.file.add_command(label ='Save', command = None) 
        self.file.add_separator() 
        self.file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
        self.edit = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
        self.edit.add_command(label ='Cut', command = None) 
        self.edit.add_command(label ='Copy', command = None) 
        self.edit.add_command(label ='Paste', command = None) 
        self.edit.add_command(label ='Select All', command = None) 
        self.edit.add_separator() 
        self.edit.add_command(label ='Find...', command = None) 
        self.edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
        self.help_ = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Tk Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Tk', command = None)
#=======================================================================================================

        
        self.photo_a = Image.open("images/calendar.png")
        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
        self.pic_a=ImageTk.PhotoImage(self.photo_a)
        self.calendar = Menu(self.menubar, tearoff = 0)
        self.calendar.add_command( label='Calendar',command=self.calendar)
        self.menubar.add_cascade(image=self.pic_a, menu = self.calendar)
        root.config(menu = self.menubar)
#=======================================================================================================

        self.photo_0 = Image.open("images/profile.png")
        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
        self.pic_0=ImageTk.PhotoImage(self.photo_0)
        self.profile = Menu(self.menubar, tearoff = 0)
        self.profile.add_command(label='Profile', command=self.profile)
        self.menubar.add_cascade(image=self.pic_0, menu = self.profile)
        root.config(menu = self.menubar)
#========================================================================================================

        
        
        self.photo_ = Image.open("images/logout.png")
        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
        self.pic_=ImageTk.PhotoImage(self.photo_)
        self.logout = Menu(self.menubar, tearoff = 0)
        self.logout.add_command(label='Logout', command=self.logOut)
        self.menubar.add_cascade(image=self.pic_, menu = self.logout)
        root.config(menu = self.menubar)
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
        self.btn1=Button(master, image=self.pic1, command=self.all_items).place(x=60,y=80)
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
        self.newWindow = Toplevel(self.master)
        self.app = SearchTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Search Tools itmes")
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
            self.newWindow = Toplevel(self.master)
            self.app = UserHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("All tool itmes")
               

    def all_items(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AllTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("All tool itmes")

    def hire(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = HireTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Hire Tools")
                                     
    def returns(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = ReturnTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Return Tools")

    def profile(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")

    def payment(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = PaymentTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Payment Tools")
                
    def logOut(self):
        me.showwarning("Logout",
                       "Are You sure want to LogOut?")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login Form")

    def calendaar(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Calendar")
    

class AdminHome(Frame):
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master)
        
        self.menubar = Menu(master) 
# Adding File Menu and commands 
        self.file = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='New File', command = None) 
        self.file.add_command(label ='Open...', command = None) 
        self.file.add_command(label ='Save', command = None) 
        self.file.add_separator() 
        self.file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
        self.edit = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
        self.edit.add_command(label ='Cut', command = None) 
        self.edit.add_command(label ='Copy', command = None) 
        self.edit.add_command(label ='Paste', command = None) 
        self.edit.add_command(label ='Select All', command = None) 
        self.edit.add_separator() 
        self.edit.add_command(label ='Find...', command = None) 
        self.edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
        self.help_ = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Tk Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Tk', command = None)
#=======================================================================================================

        
        self.photo_a = Image.open("images/calendar.png")
        self.photo_a=self.photo_a.resize((25,26), Image.ANTIALIAS)
        self.pic_a=ImageTk.PhotoImage(self.photo_a)
        self.calendar = Menu(master, tearoff = 0)
        self.calendar.add_command( label='Calendar',command=self.calendar)
        self.menubar.add_cascade(image=self.pic_a, menu = self.calendar)
        root.config(menu = self.menubar)
#=======================================================================================================

        self.photo_0 = Image.open("images/profile.png")
        self.photo_0=self.photo_0.resize((25,26), Image.ANTIALIAS)
        self.pic_0=ImageTk.PhotoImage(self.photo_0)
        self.profile = Menu(self.menubar, tearoff = 0)
        self.profile.add_command(label='Profile', command=self.profile)
        self.menubar.add_cascade(image=self.pic_0, menu = self.profile)
        root.config(menu = self.menubar)
#========================================================================================================
        
        self.photo_ = Image.open("images/logout.png")
        self.photo_=self.photo_.resize((25,26), Image.ANTIALIAS)
        self.pic_=ImageTk.PhotoImage(self.photo_)
        self.logout = Menu(self.menubar, tearoff = 0)
        self.logout.add_command(label='Logout', command=self.logOut)
        self.menubar.add_cascade(image=self.pic_, menu = self.logout)
        root.config(menu = self.menubar)

#=========================================================================================================

        self.photo1 = Image.open("images/search.png")
        self.photo1=self.photo1.resize((250,250), Image.ANTIALIAS)
        self.pic1=ImageTk.PhotoImage(self.photo1)
        self.btn1=Button(master, image=self.pic1, command=self.all_tools).place(x=60,y=80)
        self.lbl1=Label(master, text='All Tools', width=17, font=("", 18)).place(x=60, y=300)
        
        self.photo2 = Image.open("images/hire.png")
        self.photo2=self.photo2.resize((250,250), Image.ANTIALIAS)
        self.pic2=ImageTk.PhotoImage(self.photo2)
        self.btn2=Button(master, image=self.pic2, command=self.upload).place(x=320,y=80)
        self.lbl2=Label(master, text='Upload Tools', width=17, font=("", 18)).place(x=320, y=300)

    def all_tools(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AllTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("All tools")

    def upload(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = UploadTools(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")

    def profile(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AdminHome(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Profile")
                
    def logOut(self):
        me.showwarning("Logout",
                       "Are You sure want to LogOut?")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Login(self.newWindow)
        self.newWindow.geometry('650x650')
        self.newWindow.title("Login Form")

    def calendaar(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
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
        Button(master, text='Ok!!',font=("arial", 13,"bold"),width=5,bg='Midnight blue',fg='white', command=self.uptools).place(x=298,y=464)

    def uptools(self):
        self.tool_name = self.tool_name.get()
        self.tool_description = self.tool_description.get()
        self.tool_condition = self.tool_condition.get()
        self.tool_halfday = self.tool_halfday.get()
        self.tool_fullday = self.tool_fullday.get()
        if (len(self.tool_name)==0 and len(self.tool_description)==0 and len(self.tool_condition)==0 and len(self.tool_halfday)==0 and len(self.tool_fullday)==0):
            me.showerror('Incorrect Credientitals','No fiels must be empty')
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
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
            self.newWindow = Toplevel(self.master)
            self.app = AdminHome(self.newWindow)
            self.newWindow.geometry('650x650')
            self.newWindow.title("Home page")

#==================================================================================================
class AllTools:
    def __init__(self, master):
        self.master=master
        self.frame=Frame(master)
        self.lab=Label(master, text='ALL items').pack()
        c.execute('SELECT * FROM ToolsInfo')
        data=c.fetchall()
        if data:
            for elem in data:
                a=elem[0]
                b=elem[1]
                d=elem[2]
                e=elem[3]
                f=elem[4]
                self.lbl=Label(master, text=('Tool Name\t',a)).pack()
                self.lbl=Label(master, text=('Tool Description\t',b)).pack()
                self.lbl=Label(master, text=('Tool Condition', d)).pack()
                self.lbl=Label(master, text=('Tool Half Day Rate', e)).pack()
                self.lbl=Label(master, text=('Tool Full Day Rate', f)).pack()
#======================================================================================================
    
class SearchTools(Frame):
    def init__(self,master):
        self.master=master
        self.frame=Frame(master)
        
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

class HireTools():
    pass

#=========================================================================================================
class ReturnTools():
    pass

#=========================================================================================================
class PaymentTools():
    pass

#===========================================================================================================


root=Tk()
root.title('Shared Power')
root.geometry('650x650')
#obj=MainPage(root)
#obj.progressBar()
Login(root)
#Registration(root)
#UserHome(root)
#UploadTools(root)
#SecondPage(root)
#UploadTools(root)
#SearchTools(root)
root.configure(bg="white")
#root.mainloop()
