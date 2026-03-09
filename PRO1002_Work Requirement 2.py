# Exercise 3: Simple Class and Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")    

class Student(Person): 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student ("Jea", 33, "ABC3333")                   
student.greet()
print(f"Student ID: {student.student_id}")

print()



# Exercise 4: Math Quiz with Exception Handling
import random

a = random.randint(1, 50)
b = random.randint(1, 50)

print(f"Math Quiz: What is {a} + {b}?")
answer = input("Your answer: ")

try:
    answer = int(answer)
except ValueError: 
    print("Invalid input! Please enter a valid number next time.")
else: 
    if answer == a + b:
        print("Correct! Good job!")
    else: 
        print(f"Oops, the answer was {a + b}.")



# Exercise 7: Scoped Variables Experiment
name = "outer"
print(f"Global scope - name ='{name}'")

def show_scope():
    name = "Inner"
    print(f"Inside show_scope() - name ='{name}' ")
    
    def nested():
        name = "nested"
        print(f"Inside nested() - name ='{name}'")

    nested()
    print(f"Back in show_scope() - name ='{name}'") 

show_scope()
print(f"Global scope after calling show_scope() - name ='{name}'")

print()       
