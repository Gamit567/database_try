
import tkinter as tk



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

    def enterscreen(self):
        self.main.forget()
        self.enter.pack()
    def findscreen(self):
        self.main.forget()
        self.find.pack()

s = interface()
s.screen.mainloop()