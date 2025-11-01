import tkinter as tk
import Student
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
        self.all_buttons()
        self.inital_buttons()

    def all_buttons(self):
        #making the buttons
        self.welcomescreen = tk.Label(self.main,text='WELCOME')
        self.enterstudent = tk.Button(self.main,text='enter student',width=25,height=2,command=self.enterscreen)
        self.findstudent = tk.Button(self.main,text='find student',width=25,height=2,command=self.findscreen)
        # all screens have a back button at the botto,
        self.back = tk.Button(self.screen,text="return",width= 25,height=2,command = self.inital_buttons)
        
        ## making enter frame widgets
        self.enterlabel = tk.Label(self.find,text="ENTER ID ")
        self.findId = tk.Entry(self.find)
        self.getId = tk.Button(self.find,text="submit",command = self.getting_input)
        
    def inital_buttons(self):
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
        #adding buttons
        self.enterlabel.pack()
        self.findId.pack()
        self.getId.pack()
    def findscreen(self):
        self.main.forget()
        self.find.pack()
    def getting_input(self):
        self.r = self.findId.get()
        messagebox.showinfo("student",searcher.getting_specific(self.r) +  searcher.getting_modules_grades(self.r))
       

        

s = interface()
s.screen.mainloop()