#imports
import sqlite3
import datetime
from colorama import init
from pyfiglet import figlet_format
import calendar
from getpass import getpass
from columnar import columnar



fancy=["""
 =========================
| THIS IS THE SELLER PANEL |
 =========================
 ""","""
 ===================
| REGISTER AS BUYER |
 ===================
 ""","""
 ================
| LOGIN AS BUYER |
 ================
 ""","""
 ================
| ENTER FIRSTNAME |
 ================
 ""","""
 ================
| ENTER LASTNAME |
 ================
 ""","""
 ================
| ENTER USERNAME |
 ================
 ""","""
 ================
| ENTER PASSWORD |
 ================
 ""","""
 =======================
| Login to your Account |
 =======================
 ""","""
 ==========================
| Welcome to the Home Page |
 ==========================
 ""","""
 ======
| EXIT |
 ======
 ""","""
 =====================
| CREATE YOUR ACCOUNT |
 =====================
 ""","""
 -------------------------------
| Please Enter correct choice!! |
 -------------------------------
 ""","""
 =================
| LOGIN AS SELLER |
 =================
 ""","""
 ==============
| DESCRIPTION |
 ==============
 ""","""
 =====================
| TERMS AND CONDITONS |
 =====================
 ""","""
 ===================
| CUSTOMER DETAILS |
 ===================
 ""","""
 ================
| RIDER DETAILS |
 ================
 ""","""
 =================
 | MAKE PAYMENTS |
 =================
 ""","""
 =================
 | RIDER PROFILE |
 =================
"""]

conn = sqlite3.connect('project.db')
c = conn.cursor()

#---------------------------------------------------------This is admin Panel-----------------------------------------------------------------------------------------
class AdminPanel:
    def __init__(self):
        pass
    def create_table1(self):
        c.execute('CREATE TABLE IF NOT EXISTS ToolsInfo(NameOfTool NOT NULL, ToolType NOT NULL, ToolDescription NOT NULL, ToolCondition NOT NULL, HalfDayRate NOT NULL, FullDayRate NOT NULL, UploadDate NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS MyToolsInfo(NameOfTool NOT NULL, ToolType NOT NULL, ToolDescription NOT NULL, ToolCondition NOT NULL, HalfDayRate NOT NULL, FullDayRate NOT NULL, UploadDate NOT NULL)')
    def admin_login(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        if self.username == 'admin' and self.password == 'admin':
            print("successfully logged in as seller\n")
            print(fancy[0])
            self.homepage_seller()
        else:
            print("You don't have Super User Permission!!\n")
            choice = input("\nPress Enter or any key to redirect back to Home Page!! ")
            if choice == '':
                self.admin_login()
            else:
                self.display_text()
                
                
    def homepage_seller(self):
        print('\n1.Items\n2.Calendar\n3.Profile\n4.Upload Tools\n5.Rider Profile\n6.logout')
        choice = input("\nEnter the choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print('Username: ',self.username,'\n','Password: ',self.password)
            choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
            if choice=='':
                self.homepage_seller()
            else:
                self.homepage_seller()
        elif choice == '4':
            self.upload_tools()
        elif choice == '5':
            self.rider_profile()    
        elif choice == '6':
            choice=input("\nDo you really want to log out?: ")
            if choice=="yes":
                print("\nSuccessfully Logged out!!\n")
                self.details()
            else:
                self.homepage_seller()

        else:
            print(fancy[11])
            self.homepage_seller()
            
    def upload_tools(self):
        self.name_of_tool = input("Name of Tool: ")
        self.tool_type = input('Type: ')
        self.tool_description = input("Tool Description: ")
        self.tool_condition = input("Tool Condition: ")
        self.tool_rate_halfday = float(input('Tool Rate\n\tHalf day: '))
        self.tool_rate_fullday = float(input('\tFull day: '))
        self.up_date = datetime.datetime.now()
        self.upload_date = self.up_date.strftime('%Y-%m-%d')
        c.execute('INSERT INTO ToolsInfo (NameOfTool, ToolType, ToolDescription, ToolCondition, HalfDayRate, FullDayRate,UploadDate) VALUES(?,?,?,?,?,?,?)',
        (self.name_of_tool, self.tool_type, self.tool_description, self.tool_condition, self.tool_rate_halfday, self.tool_rate_fullday,self.upload_date))
        conn.commit()
        choice=input("Press Enter or any key to redirect back to Home Page!! ")
        if choice=="":
            self.homepage_seller()
        else:
            self.homepage_seller()
            
    def rider_profile(self):
        data = [
        ['id', '1',],
        ['Name', 'Aayush Khanal'],
        ['Email', 'ayushkhanal@gmail.com'],
        ['Contact', "9809823406"]
                ]

        data1 = [
        ['id', '2',],
        ['Name', 'Santosh Shahi'],
        ['Email', 'santoshshahi@gmail.com'],
        ['Contact',"9857458495"]
                ]

        data2 = [
        ['id', '3',],
        ['Name', 'Roshan Bist'],
        ['Email', 'roshanbist@gmail.com'],
        ['Contact', "9845432540"]
                ]

        data3 = [
        ['id', '4',],
        ['Name', 'Niraj Poudel'],
        ['Email', 'nirajpoudel@gmail.com'],
        ['Contact', "9801123432"]
                ]

        print('\t\t',fancy[18])
        print(columnar(data),'\n')
        print(columnar(data1),'\n')
        print(columnar(data2),'\n')
        print(columnar(data3))
        choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
        if choice=="":
            self.homepage_seller()
        else:
            self.homepage_seller()

##    def rate(self):
##        conn = sqlite3.connect('project.db')
##        c = conn.cursor()
##        c.execute('CREATE TABLE IF NOT EXISTS InvoiceInfo(HalfDayRate NOT NULL, FullDayRate NOT NULL, InsuranceHalfDay NOT NULL, InsuranceFullDay NOT NULL, TotalAmount NOT NULL)') 
##        c.execute('SELECT * FROM ToolsInfo')
##        rows=c.fetchall()
##        if rows:
##            for price in rows:
##                dataa=[
##                    ['Half Day Rate',price[4]],
##                    ['Full Day Rate', price[5]],
##                        ]
##            print(columnar(dataa))
##        for row in rows:
##            self.tool_rate_halfday=float(row[4])
##            self.tool_rate_fullday=float(row[5])
##            self.insurance_half_day_amount=float(0.5*self.tool_rate_halfday)
##            self.insurance_full_day_amount=float(0.5*self.tool_rate_fullday)
##            self.total_amount=10000
##            c.execute('INSERT INTO InvoiceInfo (HalfDayRate, FullDayRate, InsuranceHalfDay, InsuranceFullDay, TotalAmount) VALUES(?,?,?,?,?)',(self.tool_rate_halfday, self.tool_rate_fullday, self.insurance_half_day_amount, self.insurance_full_day_amount,self.total_amount))
##            conn.commit()
##            value=c.fetchall()

                   
#----------------------------------------------------------This is User Panel-------------------------------------------------------------------------------
class UserPanel(AdminPanel):
    def __init__(self):
        pass
    def details(self):
        self.text="Welcome to the shared Power"
        print(figlet_format(self.text, font="standard"))
        choice = input("Press Enter to Continue!!!")
        if choice == '':
            self.display_text()
        else:
            sys.exit()
    def display_text(self):
        print('1.',fancy[12],'2.', fancy[1], '3.', fancy[2], '4.', fancy[9])
        choice=input('Please choose one of the above option: ')
        if choice == '1':
            print(fancy[12])
            self.admin_login()
        elif choice == '2':
            print(fancy[1])
            self.user_info()
        elif choice == '3':
            print(fancy[2])
            self.login_info()
        elif choice == '4':
            print(fancy[9])
            sys.exit()
        else:
            print(fancy[11])
            self.display_text()
    def create_table2(self):
        c.execute('CREATE TABLE IF NOT EXISTS UserInfo(Firstname NOT NULL,Lastname NOT NULL, Username UNIQUE NOT NULL, Password NOT NULL, Date NOT NULL, Time NOT NULL)')
    def user_info(self):
        self.firstname = input("|FirstName|: ")
        self.lastname = input("|LastName|: ")
        self.username = input("|UserName|: ")
        self.password = input("|Password|: ")
        self.date_time()
        c.execute('INSERT INTO UserInfo (Firstname, Lastname, Username, Password, Date, Time) VALUES(?,?,?,?,?,?)',
                  (self.firstname, self.lastname, self.username, self.password, self.current_date, self.current_time))
        conn.commit()
        print("Account successfully created!!")
        print(fancy[7])
        self.login_info()
    def date_time(self):
        self.curr_date = datetime.datetime.now()
        self.current_date = self.curr_date.strftime('%Y-%m-%d')
        self.current_time = self.curr_date.strftime('%H:%M:%S %P')

    def login_info(self):
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        self.username = input("|Username| : ")
        self.password = input("|Password| : ")
        c.execute('SELECT * FROM UserInfo WHERE username=? AND password=?',(self.username,self.password))
        conn.commit()
        if c.fetchall():
            print("Successfully logged in!!")
            print(fancy[8])
            self.home_items()
        else:
            print("User not found!!\n")
            choice = input('Press Enter to Retry!! or Press any key to go back!!')
            if choice == '':
                self.login_info()
            else:
                self.display_text()

    def home_items(self):
        print('\n1.All Items\n2.Calendar\n3.Profile\n4.Search Tools\n5.My tools\n6.Return Tool\n7.Payment\n8.Logout\n')
        choice = input("Enter what is your choice: ")
        if choice == '1':
            self.items()
        elif choice == '2':
            pass
        elif choice == '3':
            self.profile()
        elif choice == '4':
            self.search()
        elif choice == '5':
            self.my_tools()
        elif choice == '6':
            self.Return_tool()
        elif choice == '7':
            self.payment()
        elif choice == '8':
            choice=input("\nDo you really want to log out?: ")
            if choice=="yes":
                print("\nSuccessfully Logged out!!\n")
                self.display_text()
            else:
                self.home_items()
        else:
            print(fancy[11])
            self.home_items()
    def items(self):
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToolsInfo')
        items=c.fetchall()
        if items:
            for elem in items:
                dta=[
                     ["Name of Tool\t\t ",elem[0]],
                     ["Tool Type\t\t ",elem[1]],
                     ["Tool Description\t ",elem[2]],
                     ["Tool Condition\t\t ",elem[3]],
                     ["Tool Rate Half-Day\t ",elem[4]],
                     ["Tool Rate Full-Day\t ",elem[5]],
                     ["Tool Upload Date\t",elem[6]]
                    ]
                print(columnar(dta))
        else:
            print("\nNo items are added yet!!")
        choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
        if choice=='':
            self.home_items()
        else:
            self.home_items()
    def Calendar(self):
        pass
    def profile(self):
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        c.execute('SELECT * FROM UserInfo WHERE username = ? AND password = ?',(self.username, self.password))
        conn.commit()
        value = c.fetchall()
        if value is not None:
            for elem in value:
                data=[
                    ["FirstName:\t ",elem[0]],
                    ["LastName:\t ",elem[1]],
                    ["UserName:\t ",elem[2]],
                    ["Password:\t ",elem[3]]
                    ]
                print(columnar(data))
                choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
                if choice=="":
                    self.home_items()
                else:
                    self.home_items()
    def search(self):
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        self.tool_type = input("Enter Type: ")
        self.name_of_tool = input("Enter Search: ")
        c.execute('SELECT * FROM ToolsInfo WHERE NameOfTool = ? AND ToolType = ?',(self.name_of_tool, self.tool_type))
        conn.commit()
        data = c.fetchall()
        if data:
            for elem in data:
                print(fancy[13])
                dta=[
                     ["Name of Tool\t\t ",elem[0]],
                     ["Tool Type\t\t ",elem[1]],
                     ["Tool Description\t ",elem[2]],
                     ["Tool Condition\t\t ",elem[3]],
                     ["Tool Rate Half-Day\t ",elem[4]],
                     ["Tool Rate Full-Day\t ",elem[5]],
                     ["Tool Upload Date\t",elem[6]]
                    ]
                print(columnar(dta))
    
                choice=input("\nDo you want to hire?: ")
                if choice == 'yes':
                    file=open('nj.txt')
                    f=file.readlines()
                    print(fancy[14])
                    for values in f:  
                        print(values)
                    
                    choose = input("\nDo you want to continue or go back?: ")
                    if choose=="yes":
                        c.execute("DELETE FROM ToolsInfo WHERE NameOfTool=?", (self.name_of_tool,))
                        conn.commit()
                        choice = input("\nDo you want delivery or not?: ")
                        if choice=="yes":
                            address=input("Enter your address: ")
                            contact=input('Enter your contact: ')
                            print(fancy[15])
                            print('Customer Address: ',address)
                            print('Customer Contact: ',contact)
                            print(fancy[16])
                            Rider_id = '123'
                            print("Rider id:\t",Rider_id)
                            Rider_name = 'Roshan Bist'
                            print('Rider Name\t',Rider_name)
                            print("\nYou will get your items delivered within 24 hours\nThank You!!")
                            choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
                            if choice=='':
                                self.home_items()
                            else:
                                self.home_items()

                        else:
                            print("\nWe have our office in Baneshwor near Samsad Bhawan, Koteshwor and Kirtipur. Please visit there to get it.\nThank you!!")
                            choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
                            if choice=='':
                                self.home_items()
                            else:
                                self.home_items()


                    else:
                        print(fancy[8])
                        self.home_items()
                else:
                    self.home_items()
        else:
            print("Product not found!!")
            choice=input("\nPress Enter to continue or Press any key to go back: ")
            if choice=='':
                self.search()
            else:
                self.home_items()

    def my_tools(self):
        c.execute('SELECT * FROM MyToolsInfo')
        tools=c.fetchall()
        if tools:
            for tool in tools:
                a=[
                    ['Tool Name',tool[0]],
                     ['Tool type',tool[1]],
                     ['Tool Description',tool[2]]
                     ]
                print(columnar(a))
        else:
            print("\nNo tools Added yet!!")
            choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
            if choice=="":
                self.home_items()
            else:
                self.home_items()
        
    def Return_tool(self):
        print("My tools")
        choice=input("\nDo you want rider or not?: ")
        if choice=="yes":
            print(fancy[16])
            Rider_id = '2'
            print("Rider id:\t",Rider_id)
            Rider_name = 'Roshan Bist'
            print('Rider Name\t',Rider_name)
            Rider_contact = '9812987645'
            print('Rider Contact\t',Rider_contact)
            print("\nHe will pick items from you!!\nThank You")
        else:
            print("\nVisit to our nearby office and return your tool!!")
        choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
        if choice=="":
            self.home_items()
        else:
            self.home_items()
        
            
    def payment(self):
        print(fancy[17])
        print("----------------------")
        choice=input("\nDo you want to print bill or not? :")
        if choice == 'yes':
            print("Here is your downloaded bill")
        else:
            print("\nThank you")
            self.home_items()
        choice=input("\nPress Enter or any key to redirect back to Home Page!! ")
        if choice=="":
            self.home_items()
        else:
            self.home_items()

            
a=AdminPanel()
a.create_table1()
r=UserPanel()
r.create_table2()
r.details()





















 
