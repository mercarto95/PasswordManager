from inspect import modulesbyfile
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from numpy import disp
from password import *
from resultWindow import *

myDatabase = sqlite3.connect('./db/mydb.db')
counterOfAccounts = 0




class App:
    global counterOfAccounts
    def __init__(self, root):
        global counterOfAccounts
        passwordObj = Password()
        #setting title
        root.title("Password Manager")
        #setting window size
        width=600
        height=580
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_169=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_169["font"] = ft
        GLabel_169["fg"] = "#333333"
        GLabel_169["justify"] = "center"
        GLabel_169["text"] = "Welcome to password manager"
        GLabel_169.place(x=110,y=10,width=356,height=30)

        def insertToMessageBox( messageFor):
            global counterOfAccounts
            counterOfAccounts += 1
            messageFor = str( counterOfAccounts ) + ". " + messageFor
            GListBox_216.insert("end",  messageFor) 
        
        def readValuesFromDatabase(db):
            GListBox_216.delete(0, "end")
            result = passwordObj.view(db, "some" , all=True)
            print( "Result =  ", result)
            for i in result:
                print(i)
                insertToMessageBox(i)
            
        def destroy():
            root.destroy()
        

        def dispkay():
            passwordFor = GLineEdit_845.get()
            GLineEdit_845.delete(0, 'end')
            print(passwordFor)
            if(passwordFor != ""):
            ## neet to ggenerate new password :
                generatedPassword = passwordObj.autoGenerate(10)
                print("Password : ", generatedPassword)
                messagebox.showinfo('Information', "Your Password: "+  generatedPassword)
                insertToMessageBox(passwordFor)
                answer = passwordObj.storeToDB('95', 'mercarto95', passwordFor, generatedPassword, myDatabase)
                print("Anser = ", answer)
                if(answer is False):
                    displayMessage("A password for this target is alreadt exiting!")
        
        def displayMessage(message):
            messagebox.showerror( "OBS", message)

        GButton_976=tk.Button(root)
        GButton_976["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=12)
        GButton_976["font"] = ft
        GButton_976["fg"] = "#000000"
        GButton_976["justify"] = "center"
        GButton_976["text"] = "Generate New Password"
        GButton_976.place(x=80,y=150,width=171,height=50)
        GButton_976["command"] = dispkay 

        GLabel_303=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_303["font"] = ft
        GLabel_303["fg"] = "#333333"
        GLabel_303["justify"] = "center"
        GLabel_303["text"] = "Fetch an Existing password"
        GLabel_303.place(x=110,y=240,width=264,height=30)

        GLabel_531=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_531["font"] = ft
        GLabel_531["fg"] = "#333333"
        GLabel_531["justify"] = "left"
        GLabel_531["text"] = "Email"
        GLabel_531.place(x=20,y=280,width=85,height=48)

        GLineEdit_182=tk.Entry(root)
        GLineEdit_182["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_182["font"] = ft
        GLineEdit_182["fg"] = "#333333"
        GLineEdit_182["justify"] = "center"
        GLineEdit_182["text"] = "your.email@mail.com"
        GLineEdit_182.place(x=160,y=280,width=407,height=48)

        GLabel_58=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#333333"
        GLabel_58["justify"] = "left"
        GLabel_58["text"] = "Password"
        GLabel_58.place(x=20,y=350,width=85,height=48)

        GLineEdit_136=tk.Entry(root)
        GLineEdit_136["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_136["font"] = ft
        GLineEdit_136["fg"] = "#333333"
        GLineEdit_136["justify"] = "center"
        GLineEdit_136["text"] = "Password"
        GLineEdit_136.place(x=160,y=360,width=407,height=48)

        GListBox_216=tk.Listbox(root)
        GListBox_216["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GListBox_216["font"] = ft
        GListBox_216["selectmode"] = "MULTIPLE"
        GListBox_216["justify"] = "left"
        GListBox_216["fg"] = "#333333"
        #GListBox_216["justify"] = "center"
        # GListBox_216.insert("end", "1" "KALLE")
        GListBox_216.place(x=160,y=430,width=307,height=63)

        GLabel_890=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "left"
        GLabel_890["text"] = "Password for?"
        GLabel_890.place(x=10,y=430,width=121,height=46)

        def match(text):
            target = ""
            wanted = False
            for i in range ( len(text) ):
                print("i = ", text[i])
                if(text[i] == '.'):
                    wanted = True
                    j = i + 2
                    print(j)
                    for i in range(j,  len(text)):
                        target += text[i]
                    break
            return target
                
    

        def fetchPassword():
            email = GLineEdit_182.get()
            password = GLineEdit_136.get()
            GLineEdit_182.delete(0, 'end')
            GLineEdit_136.delete(0, 'end')
            selected = ""
            for i in GListBox_216.curselection():
                selected = GListBox_216.get(i)
            if(email == "" or password == "" or selected ==""):
                displayMessage("Please Fill All Requirements!")
                return
            if( passwordObj.checkAuthentification(email, password, myDatabase) ):
                selected = match(selected)
                print(selected)
                returnedPassword = passwordObj.view(myDatabase, selected)
                print(returnedPassword)
                #displayMessage(returnedPassword)
                showPassword(returnedPassword)
                
            else:
                print("Wrong Pasword!!!")
                displayMessage("Wrong Password!!!")
        
        
        
        def deleteAllPasswords():
            choice = messagebox.askquestion( title="Danger!!!!" , message="Are you sure you want to delete all passwords?!")
            if choice == "yes":
                email = GLineEdit_182.get()
                password = GLineEdit_136.get()
                GLineEdit_182.delete(0, 'end')
                GLineEdit_136.delete(0, 'end')
                if(email == "" or password == "" ):
                    displayMessage("Please Enter you Email & Password !!")
                    return
                if( passwordObj.checkAuthentification(email, password, myDatabase) ):
                    passwordObj.deleteAllPasswords(myDatabase)
                    readValuesFromDatabase(myDatabase)
                else:
                    displayMessage("Wrong Password Or Email!!!")
                print("YES!")
            else:
                print("NO!")
            #
            

        GButton_841=tk.Button(root)
        GButton_841["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=13)
        GButton_841["font"] = ft
        GButton_841["fg"] = "#000000"
        GButton_841["justify"] = "center"
        GButton_841["text"] = "Fetch "
        GButton_841.place(x=480,y=430,width=108,height=52)
        GButton_841["command"] = fetchPassword

        deletaAllPass=tk.Button(root)
        deletaAllPass["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=13)
        deletaAllPass["font"] = ft
        deletaAllPass["fg"] = "#000000"
        deletaAllPass["justify"] = "center"
        deletaAllPass["text"] = "Delete All Passwords "
        deletaAllPass.place(x=160,y=510,width=178,height=52)
        deletaAllPass["command"] = deleteAllPasswords

        deletaAllPass=tk.Button(root)
        deletaAllPass["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=13)
        deletaAllPass["font"] = ft
        deletaAllPass["fg"] = "#000000"
        deletaAllPass["justify"] = "center"
        deletaAllPass["text"] = "Close "
        deletaAllPass.place(x=370,y=510,width=128,height=52)
        deletaAllPass["command"] = destroy

        GLabel_142=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_142["font"] = ft
        GLabel_142["fg"] = "#333333"
        GLabel_142["justify"] = "left"
        GLabel_142["text"] = "Password for: "
        GLabel_142.place(x=20,y=60,width=135,height=36)

        GLineEdit_845=tk.Entry(root)
        GLineEdit_845["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_845["font"] = ft
        GLineEdit_845["fg"] = "#333333"
        GLineEdit_845["justify"] = "center"
        GLineEdit_845["text"] = "Password for..."
        GLineEdit_845.place(x=180,y=60,width=338,height=39)

        GButton_12=tk.Button(root)
        GButton_12["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=13)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "Store Password"
        GButton_12.place(x=320,y=150,width=171,height=50)
        GButton_12["command"] = self.GButton_12_command
        readValuesFromDatabase(myDatabase)

    def GButton_976_command(self):
        print("command")


    def GButton_841_command(self):
        print("command")


    def GButton_12_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
