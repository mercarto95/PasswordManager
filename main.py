import random
import sqlite3


NUM_OF_CHARS = 10


class Person:
    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password

    def setUsername(self, username):
        self.username = username
        
    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def printInfo(self):
        print("Firstname: " + self.firstname)
        print("Lastname: " + self.lastname)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Password: " + self.password)
        
class Password:
    def __init__(self):
        pass
    
    def generateSymbols(self, numOfChars):
        string = ""
        for i in range(numOfChars):
            if(i %2 == 0):
                string += chr(random.randint(33, 46))
            else:
                string += chr(random.randint(58, 64))
        return string

    def generateUpperCase(self, numOfChars):
        string = ""
        for i in range(numOfChars):
            string += chr(random.randint(65, 90))
        return string

    def generateLowerCase(self, numOfChars):
        string = ""
        for i in range(numOfChars):
            string += chr(random.randint(97, 122))
        return string
    
    def shuffler(self, password):
        tmpList = list(password)
        random.shuffle(tmpList)
        return tmpList
    
    def autoGenerate(self, numOfChars):
        str=  (self.generateSymbols(NUM_OF_CHARS) + self.generateLowerCase(NUM_OF_CHARS) + self.generateUpperCase(NUM_OF_CHARS)) 
        return ''.join(self.shuffler(str))
    
    def view(self, db, target):
        answer = db.execute(f"SELECT * FROM passwords WHERE target = '{target}'")
        db.commit()
        print(answer)
        for row in answer:
            print("=="*20)
            print(len(row))
    
    def isExisting(self, db, target):
        answer = db.execute(f"SELECT * FROM passwords WHERE target = '{target}'")
        db.commit()
        print(answer)
        for row in answer:
            return True 
        return False
        
    
    def storeToDB(self, user, autonotification, passwordFor, password, db):
        ##print(f"INSERT INTO person ({p.firstname}, {p.lastname}, {p.username}, {p.email}, {p.password})")
        ##db.execute("INSERT INTO person VALUES ('A', 'B', 'C', 'd', 'e');")
        if( not self.isExisting(db, passwordFor)  ):
            db.execute(f"INSERT INTO passwords VALUES ('{passwordFor}', '{password}', 95);")
            db.commit()
            return True 
        return False


p1 = Password()
passw = p1.autoGenerate(NUM_OF_CHARS)

fname  = 'Jhone'
lastname = "Smith"
username = "kalleMalle"
email = "kalleMalle@gmail.com"
password = p1.autoGenerate(NUM_OF_CHARS)

p2 = Person(fname, lastname, username, email, password)
p2.printInfo()

def storeToDB(p, db):
    ##print(f"INSERT INTO person ({p.firstname}, {p.lastname}, {p.username}, {p.email}, {p.password})")
    ##db.execute("INSERT INTO person VALUES ('A', 'B', 'C', 'd', 'e');")
    db.execute("INSERT INTO person VALUES ('{p.firstname}', '{p.lastname}', '{p.username}', '{p.email}', '{p.password}');")
    db.commit()


#storeToDB (p2, conn)

def View(db):
    x = db.execute("SELECT * FROM person;")
    db.commit()
    for row in x:
        print("=="*20)
        print(f"First Name      : {row[0]}")
        print(f"Last Name       : {row[1]}")
        print(f"Username Name   : {row[2]}")
        print(f"Email           : {row[3]}")
        print(f"Passwod         : {row[4]}")

