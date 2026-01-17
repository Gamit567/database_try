import tkinter as tk
from tkinter import ttk
from tkinter import font
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
        self.main = ttk.Frame(self.screen)
        self.enter = ttk.Frame(self.screen)
        self.find = ttk.Frame(self.screen)
        self.makestudent = ttk.Frame(self.screen)
        self.makemodules = ttk.Frame(self.screen)
        ##inializing the buttons and the starter screen
        self.all_buttons()
        self.starterscreen_pack()

    def all_buttons(self):
        bold_font = font.Font(family="Arial", size=12, weight="bold")
        #making the buttons
        self.welcomescreen = ttk.Label(self.main,text='WELCOME',font=bold_font)
        self.enterstudent = ttk.Button(self.main,text='enter student',command=self.enterscreen_pack)
        self.findstudent = ttk.Button(self.main,text='find student',command=self.findscreen_pack)
        # all screens have a back button at the botto,
        self.back = ttk.Button(self.screen,text='cancel',command = self.starterscreen_pack)
        ## making find frame widgets
        self.enterlabel = ttk.Label(self.find,text="ENTER ID ")
        self.findId = ttk.Entry(self.find)
        self.getId = ttk.Button(self.find,text='submit',command = self.getting_input)
        # buttons for enter user screen, each will remake the frame either enter a new student or enter a new module
        self.addstudent = ttk.Button(self.enter,text="press here to add a new student",command=self.student_details_pack)
        self.addmodules = ttk.Button(self.enter,text="Press here to enter modules",command = self.module_details_pack)
        # buttons for entering the student details. will call a function that handles the entering into the student details
        self.userlabel = ttk.Label(self.makestudent,text='enter name')
        self.nameentry = ttk.Entry(self.makestudent)
        self.idlabel = ttk.Label(self.makestudent,text='enter id',font=bold_font)
        self.identry = ttk.Entry(self.makestudent)
        self.year = ttk.Label(self.makestudent,text='enter year',font=bold_font)
        self.yearentry = ttk.Entry(self.makestudent)
        self.submit = ttk.Button(self.makestudent,text='submit',command=self.adding_student)
        #buttons for making the module details
        self.enterId = ttk.Label(self.makemodules,text='enter ID',font=bold_font)
        self.IDentry = ttk.Entry(self.makemodules)
        self.entermodule = ttk.Label(self.makemodules,text = 'enter module',font=bold_font)
        self.moduleEntry = ttk.Entry(self.makemodules)
        self.entergrade = ttk.Label(self.makemodules,text='enter the grade',font=bold_font)
        self.gradeEntry = ttk.Entry(self.makemodules)
        self.Submitmodule = ttk.Button(self.makemodules,text='submit',command=self.addingmodule)
        self.entryboxes_list = [self.findId,self.nameentry,self.identry,self.yearentry,self.IDentry]
        ### clear  all entry boxes:
        
    def starterscreen_pack(self):
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

    def enterscreen_pack(self):
        self.main.forget()
        self.enter.pack()

        self.addstudent.pack()
        self.addmodules.pack()
        #adding 

    def module_details_pack(self):
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
        self.id = self.IDentry.get()
        self.module = self.moduleEntry.get()
        self.grade = self.gradeEntry.get()
        m2 = Module()
        if not self.id or not self.module or not self.grade:
            messagebox.showerror("error","one or more boxes have been left empty")
        else:
            m2.addmodule(self.module,self.grade,self.id)
            messagebox.showinfo(
                "Student Info",
                f"id: {self.id}\nmodule: {self.module}\ngrade: {self.grade}"
            )
        for e in (self.IDentry,self.moduleEntry,self.gradeEntry):
            e.delete(0,tk.END)
        
        
    def student_details_pack(self):
        self.enter.forget()
        self.makestudent.pack()
        self.userlabel.pack()
        self.nameentry.pack()
        self.idlabel.pack()
        self.identry.pack()
        self.year.pack()
        self.yearentry.pack()
        self.submit.pack()
        
    def findscreen_pack(self):
        self.main.forget()
        self.find.pack()
        self.enterlabel.pack()
        self.findId.pack()
        self.getId.pack()

    def getting_input(self):
        self.r = self.findId.get()
        grades = searcher.getting_modules_grades(self.r)
        info = searcher.getting_specific(self.r)
                
        self.findId.delete(0,tk.END)
        messagebox.showinfo(info,grades)

    def adding_student(self):
        name = self.nameentry.get()
        id = self.identry.get()
        year = self.yearentry.get()
        if not name or not id or not year:
            messagebox.showerror("error","one or more boxes have been left empty")
        else:
            new_student = student(name,id,year)
            new_student.adding()
            messagebox.showinfo("student added :",searcher.getting_specific(new_student.getID()))
            ##return to original screen
            self.starterscreen_pack()
        for e in (self.nameentry,self.identry,self.yearentry):
            e.delete(0,tk.END)

        
##making sure the database was created

if __name__ == "__main__":
    MySQLdatabase.creating()
    ##running the progra,
    s = interface()
    s.screen.mainloop()