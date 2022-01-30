# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:17:35 2020

@author: home
"""


a = iter([1,2,3,4,5,6])
a
next(a)

for i in a:
    print(i)



        
def getCubes(n):
    listofSquares = []
    for i in range(n):
        listofSquares.append(i**3)
    return listofSquares
        
getCubes(10)        



def gencubes(n):
    for num in range(n):
        yield num**3
        
output = gencubes(5)
output        


for i in output:
    print(i)
next(output)
        

def sq(x):
    return x*x

a = sq(5)
a        

b = map(sq, [1,2,3,4,5])
b
list(b)


def calculate(var1, var2, operation):
    if operation == '+':
        return var1 + var2
    elif operation == '-':
        return var1 - var2
    else:
        return var1*var2

calculate(5,2,'+')

def calculate(var1:str, var2:str, operation='+'):
    if operation == '+':
        return var1 + var2
    elif operation == '-':
        return var1 - var2
    else:
        return var1*var2

calculate("5","2")

class Person:
    def __init__(self, name, surname, birthyear):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear
    
    def age(self, current_year):
        return current_year - self.birthyear
    
    def __str__(self):
        return "%s %s was born in %d ." % (self.name, self.surname, self.birthyear)

anvesh = Person("Anvesh", "Mishra", 1987)
print(anvesh)
print(anvesh.age(2020))



'''
    INHERITANCE
'''

# Person class is a predefined class and we are using it in this newly defined class Student
# So this person class is being called as Parent Class
# Student class is being called as Child Class
class Student(Person):
    def __init__(self, student_id, *args):
        super(Student, self).__init__(*args)
        self.student_id = student_id

anvesh = Student(1, 'Anvesh', 'Mishra', 2006)
print(anvesh.student_id)
print(type(anvesh))
print(isinstance(anvesh, Person))
print(isinstance(anvesh, object))


'''
    OVERIDING
'''
# Overloading always happens in single class
# At the same Overriding always happens in 2 different class 

class Student(Person):
    def __init__(self, student_id, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.student_id = student_id
        
    def __str__(self):
        return super(Student, self).__str__() + " And has ID: %d" % self.student_id
    
anvesh = Student(1, 'Anvesh', 'Mishra', 2006)
print(anvesh)























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
