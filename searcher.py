import sqlite3



answer = input("find user by (name or id) ")
sqr = ""
while True:
    if answer == "id":
        sqr = "select ID from students"
        break
    elif answer == "name":
        sqr = "select name from students"
        break
    else:
        print("enter name or id")
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()
r = cursor.execute(sqr)
for res in r:
    print(res[0])