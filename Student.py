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
            #connecting to database
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()
            try:
                ##inserting values
                c.execute("INSERT INTO Modules(id,module,grade) VALUES (?,?,?)",(self.getID(),module,grade))
                conn.commit()
                conn.close()
                return "success at adding modules"
            except:
                #catching a error trying to insert the vakues
                conn.close()
                return "error adding grades"
                
        except:
            #error trying to connect to database
            return "error connecting to database Grades"

    def adding(self):
        ##adding into the grades
        try:
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            try:
                ##instead check if the id already exists
                cursor.execute("SELECT * FROM students WHERE id = ?",(self.getID(),))
                check = cursor.fetchall()
                if not check:
                    cursor.execute("INSERT INTO students(name,ID,year) VALUES (?,?,?)",(self.getname(),self.getID(),self.getyear()))
                    conn.commit()
                    conn.close()
                    return "successfully added"
                else:
                    print("students with this ID already exists")
            except:
                return "error adding to database student" + self.getname() + self.getID()
        except:
            return"error connecting to student"
        
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
    
    

    