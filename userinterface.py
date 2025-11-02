import tkinter as tk
from Student import student
import searcher
from tkinter import messagebox
class interface:
    def __init__(self):
        #making the main screen
        self.screen = tk.Tk()
        self.screen.geometry("500x250")
        #making the frames
        self.main = tk.Frame(self.screen)
        self.enter = tk.Frame(self.screen)
        self.find = tk.Frame(self.screen)
        ##inializing the buttons and the starter screen
        self.all_buttons()
        self.starterscreen()

    def all_buttons(self):
        #making the buttons
        self.welcomescreen = tk.Label(self.main,text='WELCOME')
        self.enterstudent = tk.Button(self.main,text='enter student',width=25,height=2,command=self.enterscreen)
        self.findstudent = tk.Button(self.main,text='find student',width=25,height=2,command=self.findscreen)
        # all screens have a back button at the botto,
        self.back = tk.Button(self.screen,text='return',width= 25,height=2,command = self.inital_buttons)
        
        ## making find frame widgets
        self.enterlabel = tk.Label(self.find,text="ENTER ID ")
        self.findId = tk.Entry(self.find)
        self.getId = tk.Button(self.find,text='submit',command = self.getting_input,height=2,width=25)

        self.addstudent = tk.Button("press here to add a new student")
        self.addmodules = tk.Button("Press here to enter modules")


        #making enter frame widgets
        self.userlabel = tk.Label(self.enter,text='enter name')
        self.nameentry = tk.Entry(self.enter)
        self.idlabel = tk.Label(self.enter,text='enter id')
        self.identry = tk.Entry(self.enter)
        self.year = tk.Label(self.enter,text='enter year')
        self.yearentry = tk.Entry(self.enter)
        self.submit = tk.Button(self.enter,text='submit',command=self.addingto,height=25)

    def starterscreen(self):
        # makes other frames empty
        self.enter.forget()
        self.find.forget()
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

        self.addstudent.p
        #adding buttons
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
        messagebox.showinfo("student",searcher.getting_specific(self.r) +  searcher.getting_modules_grades(self.r))
       
    def addingto(self):
        name = self.nameentry.get()
        id = self.identry.get()
        year = self.yearentry.get()

        new_student = student(name,id,year)
        new_student.adding()
        messagebox.showinfo("student added :",searcher.getting_specific(new_student.getID()))
        ##return to original screen
        self.starterscreen()

s = interface()
s.screen.mainloop()