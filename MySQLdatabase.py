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
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS Modules(
        id TEXT,
        module TEXT,
        grade TEXT
    )                        
    """)

  conn.commit()
  conn.close()
  print("success creating files")
except:
  print("error error")