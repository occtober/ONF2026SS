# Exercise 7: Scoped Variables Experiment

score = 0

def calculate_bonus():
    local_score = 100
    for i in range(3):
        local_score += i * 10
        print(f"After round {i+1}: score = {local_score}")
    return local_score

score = calculate_bonus()  
print(f"Global score: {score}")  
