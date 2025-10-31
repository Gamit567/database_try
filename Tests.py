
##test 1 trying to add to class

##test user
from Student import student
from searcher import getting_specific

jeff = student("jeff",777,2025)


def add():
    jeff.adding()
    
def adding_modules():
    module = "science"
    grade = 65
    jeff.addmodule(module,grade)

def add_duplicate():
    add()


#adding_modules()

add()

getting_specific()