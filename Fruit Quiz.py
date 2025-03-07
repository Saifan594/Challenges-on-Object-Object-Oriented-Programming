print("\033c")

import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {"apple": "red",
                       "orange": "orange",
                       "watermelon": "green",
                       "banana": "yellow"}
    
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            
            print(f"What is the color of {fruit}?")
            user_answer = input()
            
            if user_answer.lower() == color:
                print("Correct answer!")
            
            else:
                print("Wrong answer!")
            
            option = int(input("Enter 0, if you want to play again. Otherwise enter 1: "))
            if option:
                break

print("Welcome to Fruit Quiz")
fq = FruitQuiz()
fq.quiz()