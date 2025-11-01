

import sqlite3

from Student import student
import searcher

##for tests
jeff = student("jeff",777,2025)
claire = student("claire",777,2025)
brianna = student("brianna",778,2026)

### for the purpose of the tests the database should be clear and unfixed


def testsetup():
    print("setting up tests ...")
    ## we will make sure that jeff and clair and brianna are not in the database already
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE ID IN (?,?)",("777","778"))
    cursor.execute("DELETE FROM Modules where ID IN (?,?)",("777","778"))
    conn.commit()
    print("current database: ",searcher.getting_all())

def Test1():
    
    #testing adding to database
    jeff.adding()
    brianna.adding()
    print("current database is now",searcher.getting_all())

def Test2():
    #test adding same Id to database
    print("attempting to add clair with the same id as jeff")
    claire.adding()
    #should return an error
def Test3():
    #test adding a module
    module = "science"
    grade = 67
    jeff.addmodule(module,grade)
    brianna.addmodule(module,grade+18)
    print("current module table: ",searcher.getting_modules_grades(777),searcher.getting_modules_grades(778))


def Test4():
    #testing searcher/py
    searcher.getting_all()
    ID = input("enter a ID: ")
    print(searcher.getting_specific(ID))
    print(searcher.getting_modules_grades(ID))

if __name__ == "__main__":
    testsetup()
    Test1()
    Test2()
    Test3()
    Test4()
