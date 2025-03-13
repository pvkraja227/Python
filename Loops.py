# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     print(fruit)
#     print(fruit.upper())
#     print(fruit.lower())
#     print(fruit.capitalize())
#     print(fruit+" pie")

import random
# for i in range(5): # repeats 5 times starting from 0
#     print(i)
# for i in range(0, 5): print(i) # prints from 0 to 5-1=4
# for i in range(0, 5, 2): print(i) # prints from 0 to 5-1=4, with difference 2
# total=0
# for number in range(0, 201):
#     total += number
# print(total)

# to find average of heights:
# import random
# heights = input("Enter the heights separated by spaces: \n").split()
# heights = [int(h) for h in heights]
# total_height = sum(heights)
# items = len(heights)
# avg = round(total_height / items, 2)
# print(f"Average height: ", avg)

# try:
#     heights = [int(h) for h in input("Enter heights: ").split()]
#     avg = sum(heights) / len(heights)
#     print(f"Average height: {avg:.2f}")
# except ValueError:
#     print("Error: Please enter only numbers.")

# import random
# heights = input("Enter the heights separated by spaces: \n").split()
# for h in range(len(heights)):
#     heights[h]=int(heights[h])
# print(heights)
# sums=0
# for i in range(len(heights)):
#     sums=sums+heights[i]
# print(sums)
# items = len(heights)
# avg = round(sums / items, 2)
# print(f"Average height: ", avg)

# HIGHEST AND LOWEST OF NUMBERS:
# import random
# scores = input("Enter the scores separated by spaces: \n").split()
# highest = max(scores)
# lowest = min(scores)
# print("The highest score is:", highest)
# print("The lowest score is:", lowest)

# import random
# scores = input("Enter the 2 digit scores separated by spaces: \n").split()
# for t in range(len(scores)):
#     scores[t] = float(scores[t])
# highest=0
# lowest=99
# for s in range(len(scores)):
#     if scores[s]>highest:
#         highest = scores[s]
# for k in range(len(scores)):
#     if scores[k]<lowest:
#         lowest = scores[k]
# print(f"highest: {highest}")
# print(f"lowest: {lowest}")

# add even numbers between 0 to target:
# import random
# target=int(input("enter target number: \n"))
# if target % 2 ==0:
#     target = target
# else:
#     target = target + 1
# total = 0
# for i in range(0, target, 2):
#     total += i
# print(total)

# add even numbers between 0 to target (inclusive):
# import random
# target=int(input("enter target number: \n"))
# if target % 2 ==0:
#     target = target + 1
# else:
#     target = target
# total = 0
# for i in range(0, target, 2):
#     total += i
# print(total)

# FIZZ BUZZ
# import random
# target=int(input("enter target number greater than 0: "))
# if target > 0:
#     for i in range(1,target+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# else:
#     print("enter valid number")


# import random
# target=100
# for i in range(1,target+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

## PASSWORD GENERATOR
# import random
# import string
#
# lower_letters = list(string.ascii_lowercase)
# upper_letters = list(string.ascii_uppercase)
# numbers = list(string.digits)
print(numbers)
# symbols = list(string.punctuation)
print(symbols)
# nr_letters=int(input("How many letters do you want? "))
# nr_symbols=int(input("How many symbols do you want? "))
# nr_numbers=int(input("How many numbers do you want? "))
# password=[]
# for i in range(1, nr_letters+1):
#     password+=random.choice(lower_letters + upper_letters)
# print(password)
# for j in range(1, nr_numbers+1):
#     password+=random.choice(numbers)
# print(password)
# for k in range(1, nr_symbols+1):
#     password+=random.choice(symbols)
# print(password)
Shuffle password list
# random.shuffle(password)
# print(password)
Convert list to string
# password = "".join(password)
# print(password)
Output final password
# print("Generated Password:", password)
