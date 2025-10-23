## create database saver for students
import sqlite3
class student:
    def __init__(self,name,ID,year):
        self.name = name
        self.ID = ID
        self.year = year
    
    def addmodule(self,module,grade):
        ## adding module and grade into the database
        try:
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()
            try:
                c.execute("INSERT INTO Modules(id,module,grade) VALUES (?,?,?)",(self.getID(),module,grade))
                conn.commit()
                conn.close()
            except:
                print("error adding grades")
        except:
            print("error connecting to database Grades")

    def adding(self):
        ##adding into the grades
        try:
            conn = sqlite3.connect('mydatabase.db')
            try:
                conn.execute("INSERT INTO students(name,ID,year) VALUES (?,?,?)",(self.getname(),self.getID(),self.getyear()))
                conn.commit()
                conn.close()
                print("successfully added")
            except:
                print("error adding to database student")
        except:
            print("error connecting to student")
        
    ##getters if neeeded
    def getname(self):
        return self.name
    def getID(self):
        return self.ID
    def getyear(self):
        return self.year
    def getclasses(self):
        return self.classes
    def get_grade(self):
        return self.grades
    
    

    