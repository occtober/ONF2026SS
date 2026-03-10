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
