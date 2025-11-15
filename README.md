## a program which saves students information such as name, email, classes and saves that to a database, it has a searcher file which attempts to track user information using data such as name or student ID.

main is the user interface which contains all the code put together and running perfectly.
to run main make sure all the other files are downloaded because it will call on those files to run.
student.py contains 2 different classes, student and module which configuires all the students information and then connects to the database to add them together.
test.py makes sure the information is saved properly
searcher.py is to make querying the information easy and safe and for error handling.
mySQLdatavase.py creates the database/ all information is currently stored locally

the student Table uses Id as a primary key because students should be unique and no student should have the same ID twice.
the module class can have many modules connected to one student id.

