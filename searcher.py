import sqlite3
from Student import Module

def getting_specific(ID):
    #getting a specific student
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE ID=? ",(ID,))
    student = cursor.fetchone()
    if not student:
        return f"no Student found"
    

    conn.close()
    return student

def getting_all():
    #getting all students
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ")
    student = cursor.fetchall()
    conn.close()
    return student

def getting_modules_grades(ID):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Modules WHERE ID=? ",(ID,))
    student = cursor.fetchall()
    conn.close()
    if not student:
        return f"no grades found"
    return student


if __name__ == "__main__":
    m = Module()
    print(getting_all())
    print(getting_modules_grades(0))