import tkinter as tk
from Student import student,Module
import searcher
from tkinter import messagebox
import MySQLdatabase
class interface:
    def __init__(self):
        #making the main screen
        self.screen = tk.Tk()
        self.screen.geometry("500x250")
        #making the frames
        self.main = tk.Frame(self.screen)
        self.enter = tk.Frame(self.screen)
        self.find = tk.Frame(self.screen)
        self.makestudent = tk.Frame(self.screen)
        self.makemodules = tk.Frame(self.screen)
        ##inializing the buttons and the starter screen
        self.all_buttons()
        self.starterscreen()

    def all_buttons(self):
        #making the buttons
        self.welcomescreen = tk.Label(self.main,text='WELCOME')
        self.enterstudent = tk.Button(self.main,text='enter student',width=25,height=2,command=self.enterscreen)
        self.findstudent = tk.Button(self.main,text='find student',width=25,height=2,command=self.findscreen)
        # all screens have a back button at the botto,
        self.back = tk.Button(self.screen,text='return',width= 25,height=2,command = self.starterscreen)
        ## making find frame widgets
        self.enterlabel = tk.Label(self.find,text="ENTER ID ")
        self.findId = tk.Entry(self.find)
        self.getId = tk.Button(self.find,text='submit',command = self.getting_input,height=2,width=25)
        # buttons for enter user screen, each will remake the frame either enter a new student or enter a new module
        self.addstudent = tk.Button(self.enter,text="press here to add a new student",command=self.student_details)
        self.addmodules = tk.Button(self.enter,text="Press here to enter modules",command = self.module_details)
        # buttons for entering the student details. will call a function that handles the entering into the student details
        self.userlabel = tk.Label(self.makestudent,text='enter name')
        self.nameentry = tk.Entry(self.makestudent)
        self.idlabel = tk.Label(self.makestudent,text='enter id')
        self.identry = tk.Entry(self.makestudent)
        self.year = tk.Label(self.makestudent,text='enter year')
        self.yearentry = tk.Entry(self.makestudent)
        self.submit = tk.Button(self.makestudent,text='submit',command=self.addingto,height=25)
        #buttons for making the module details
        self.enterId = tk.Label(self.makemodules,text='enter ID')
        self.IDentry = tk.Entry(self.makemodules)
        self.entermodule = tk.Label(self.makemodules,text = 'enter module')
        self.moduleEntry = tk.Entry(self.makemodules)
        self.entergrade = tk.Label(self.makemodules,text='enter the grade')
        self.gradeEntry = tk.Entry(self.makemodules)
        self.Submitmodule = tk.Button(self.makemodules,text='submit',command=self.addingmodule)
       
    def starterscreen(self):
        # makes other frames empty
        self.enter.forget()
        self.find.forget()
        self.makemodules.forget()
        self.makestudent.forget()
        #getting main frame
        self.main.pack()
        self.screen.title("database system")
        #intializing initial buttons
        self.welcomescreen.pack()
        self.enterstudent.pack()
        self.findstudent.pack()
        self.back.pack(side="bottom")

    def enterscreen(self):
        self.main.forget()
        self.enter.pack()

        self.addstudent.pack()
        self.addmodules.pack()
        #adding 

    def module_details(self):
        self.enter.forget()
        self.makemodules.pack()
        self.enterId.pack()
        self.IDentry.pack()
        self.entermodule.pack()
        self.moduleEntry.pack()
        self.entergrade.pack()
        self.gradeEntry.pack()
        self.Submitmodule.pack()
    
    def addingmodule(self): 
        self.id = self.identry.get()
        self.module = self.moduleEntry.get()
        self.grade = self.gradeEntry.get()
        module = Module()
        module.addmodule(self.module,self.grade,self.id)
        messagebox.showinfo(
            "Student Info",
            f"id: {self.id}\nmodule: {self.module}\ngrade: {self.grade}"
        )

        self.starterscreen()
        
    def student_details(self):
        self.enter.forget()
        self.makestudent.pack()
        self.userlabel.pack()
        self.nameentry.pack()
        self.idlabel.pack()
        self.identry.pack()
        self.year.pack()
        self.yearentry.pack()
        self.submit.pack()
        
    def findscreen(self):
        self.main.forget()
        self.find.pack()
        self.enterlabel.pack()
        self.findId.pack()
        self.getId.pack()

    def getting_input(self):
        self.r = self.findId.get()
        grades = searcher.getting_modules_grades(self.r)
        info = "student",searcher.getting_specific(self.r)
        messagebox.showinfo("student",grades)
    def addingto(self):
        name = self.nameentry.get()
        id = self.identry.get()
        year = self.yearentry.get()

        new_student = student(name,id,year)
        new_student.adding()
        messagebox.showinfo("student added :",searcher.getting_specific(new_student.getID()))
        ##return to original screen
        self.starterscreen()

##making sure the database was created
MySQLdatabase.creating()
##running the progra,
s = interface()
s.screen.mainloop()