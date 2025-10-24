import sqlite3

# Connect to SQLite database (or create
#  it if it doesn't exist)


def creating():
  try:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Create the students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        ID TEXT PRIMARY KEY,
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


def deleting():
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute("DROP TABLE IF EXISTS students")
  cursor.execute("DROP TABLE IF EXISTS Modules")
  
creating()
deleting()