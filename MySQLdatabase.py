import sqlite3

# Connect to SQLite database (or create
#  it if it doesn't exist)



try:
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()

  # Create the students table
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS students (
      name TEXT,
      ID TEXT,
      year TEXT
  )
  """)

  conn.commit()
  conn.close()
  print("sucess")
except:
  print("error error")