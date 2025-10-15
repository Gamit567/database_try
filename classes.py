## create database saver for students
import sqlite3
class student:
    def __init__(self,name,ID,year,classes):
        self.name = name
        self.ID = ID
        self.year = year
        self.classes = classes
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
        print("hello")





