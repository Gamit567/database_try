
##test 1 trying to add to class

##test user
from Student import student
import searcher
##for tests
jeff = student("jeff",777,2025)
claire = student("claire",777,2025)
brianna = student("brianna",778,2026)

def add():
    jeff.adding()
    
def adding_modules():
    module = "science"
    grade = 65
    jeff.addmodule(module,grade)

def add_duplicate():
    add()


#adding_modules()

add()

searcher.getting_specific()

def Test1():
    #testing adding to database
    jeff.adding()
    brianna.adding()

def Test2():
    #test adding same Id to database
    claire.adding()
    ##should return an error
def Test3():
    #test adding a module
    module = "science"
    grade = 67
    jeff.addmodule(module,grade)

def Test4():
    #testing searcher/py
    searcher.getting_all()
    ID = input("enter a ID: ")
    searcher.getting_specific()
    searcher.getting_modules_grades(ID)

if __name__ == "__main__":
    Test1()
    Test2()
    Test3()
    Test4()
