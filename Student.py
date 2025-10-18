## create database saver for students
import sqlite3
class student:
    def __init__(self,name,ID,year,classes,grade):
        self.name = name
        self.ID = ID
        self.year = year
        self.classes = classes
        self.grades = grade
        self.adding()
    def adding(self):
        try:
            conn = sqlite3.connect('mydatabase.db')
        except:
            print("error connecting")
        try:
            conn.execute("INSERT INTO students(name,id,year) VALUES (?,?,?)",(self.name,self.ID,self.year))
        except:
            print("error adding to database")
        
        conn.commit()
        conn.close()
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
    
    
