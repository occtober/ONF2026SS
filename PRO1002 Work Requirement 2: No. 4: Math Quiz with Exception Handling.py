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
