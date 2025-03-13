# fruits = ['apple', 'banana', 'orange', 'strawberry', '123', '456', '3.14']
# print(fruits [6])
# fruits[4]='mango' # change the value in the list
# print(fruits)
# fruits.append("jackfruit")
# print(fruits)
# fruits.remove("jackfruit")
# print(fruits)
# fruits.extend(["jackfruit", "pineapple"])
# print(fruits)
# fruits.insert(0, "tomato")
# print(fruits)
from random import random

# import random
# friends=["pvk", "krishna", "venkat", "raja", "pvkraja"]
#
# print(random.choice(friends)) # option 1
#
# random.index=random.randint(0,len(friends)-1) # option 2
# print(friends[random.index])

# dirty_dozen=["spinach", "apples", "kale", "orange", "brinjal", "jackfruit", "pumpkin"]

# fruits=["apples", "orange", "jackfruit"]
# vegetables=["spinach", "kale", "pumpkin"]
# dirty_dozen=[fruits, vegetables]
# print(dirty_dozen) # nested lists

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1]) # o/p: Kale

# who will pay the bill, randomly
# import random
# names=input("enter names: ") # pvk krish raja venky
# names_split=names.split()
# items=len(names_split)
# random_choice=random.randint(0,items-1)
# print(names_split[random_choice])

# import random
# names=input("enter names: ") # pvk, raja, krish, venky // pvk,krish,venky,raja
# names_split=names.split(",")
# items=len(names_split)
# random_choice=random.randint(0,items-1)
# print(names_split[random_choice])

# ROCK PAPER SCISSORS (RPS)
import random
game_images=["Rock", "Paper", "Scissors"]
user_choice=int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
if user_choice < 3 and user_choice >= 0:
    print(f"you chose:", game_images[user_choice])
    computer_choice=random.randint(0, 2)
    print(f"computer chose:", game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:\
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:\
        print("You lose!")
    elif user_choice > computer_choice:\
        print("You win!")
    elif user_choice < computer_choice:\
        print("You lose!")
    elif user_choice == computer_choice:\
        print("You tie!")
else:
    print("wrong choice!")

