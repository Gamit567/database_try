import sqlite3


def getting_specific(ID):
    #getting a specific student
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE ID=? ",(ID,))
    student = cursor.fetchone()
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
    return student


if __name__ == "__main__":
    print(getting_modules_grades(0))