import sqlite3


def getting_specific():
    answer = input("find user by id ")
    
    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE ID=? ",(answer,))
    student = cursor.fetchall()
    print(student)