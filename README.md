## a program which saves students information such as name, email, classes and saves that to a database, it has a searcher file which attempts to track user information using data such as name or student ID.

student.py configuires all the students information and then connects to the database to add them together.
test.py makes sure the information is saved properly
searcher.py is to make quierying the information easy and safe 
mySQLdatavase.py creates the database/ all information is currently stored locally
sqldatabase is my version of the local data.

the student Table uses Id as a primary key because students should be unique and no student should have the same ID twice.
the module class can have many modules connected to one student id.

if you want to test the code you should run tests to see how the code comes together.