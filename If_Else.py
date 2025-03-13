# if else conditional statement
# if condition:
#     do this
# else:
#     do this

# print("Welcome to roller-coaster:")
# height=int(input("Enter your height in cms: "))
# if height > 120:
#     print("you can ride")
# else:
#     print("you can't ride")

# > greater than
# < less than
# >= greater than or equal
# <= less than or equal
# == equal to (checking if they are same)
# = assign a value
# != not equal to

# number=int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# nested if and elif condition
#
# if condition1:
#     if condition2:
#         do this
#     elif condition2:
#         do this
#     else:
#         do this
# else:
#     do this

# height=int(input("enter your height in cms: "))
# age=int(input("enter your age in years: "))
# if height >= 120:
#     if age < 12:
#         print("pay: $5")
#     elif age < 18:
#         print("pay: $7")
#     else:
#         print("pay: $9")
# else:
#     print("you can't ride:")

# height=float(input("Enter your height in mts: "))
# weight=float(input("Enter your weight in kgs: "))
# bmi=round(weight/(height**2),5)
# if bmi >= 18.5:
#     if bmi < 25:
#         print("BMI is normal")
#     elif bmi < 30:
#         print("BMI is slightly overweight")
#     elif bmi < 35:
#         print("BMI is obese")
#     elif bmi >= 35:
#         print("BMI is clinically obese")
# else:
#     print("BMI is underweight")

# Leap Year:
# year=int(input("Enter year: "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")
#
# year=int(input("Enter year: "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,"is a leap year")
#         else:
#             print(year,"is not a leap year")
#     else:
#         print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")
#
# bill=0
# height=int(input("Enter your height in metres: "))
# age=int(input("Enter your age in years: "))
# if height >= 120:
#     if age <12:
#         bill =5
#         print("Your bill is",bill)
#     elif age<18:
#         bill=7
#         print("Your bill is",bill)
#     else:
#         bill=12
#         print("Your bill is",bill)
#     photo=input("Do you want a photo: y or no: ")
#     if photo=="y":
#         bill=bill+3
#         print("Your bill is",bill)
#     else:
#         print("Your bill is",bill)
# else:
#     print("You are too young to ride")

# bill=0
# size=input("enter size: S/M/L: ")
# pepporoni=input("enter pepperoni: Y/N: ")
# extra_cheese=input("enter extra cheese: Y/N: ")
# if size == "S":
#     bill+=15
# elif size == "M":
#     bill+=20
# else:
#     bill+=25
# if pepporoni == "Y":
#     if size == "S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese == "Y":
#     bill+=1
# print(f"bill is ${bill}")

# weight=int(input("enter your weight: "))
# height=float(input("enter your height in mts: "))
# bmi=weight/(height**2)
# bmi=round(bmi,1)
# if bmi<18.5:
#     print("underweight")
# elif bmi>=18.5 and bmi<25:
#     print("normal weight")
# else:
#     print("overweight")

# print("Welcome to the Treasure Island !!")
# y=input("which way you want to go: left or right: ").lower()
# if y=="left":
#     x=input("now, there is a lake, select an option: swim or wait: ").lower()
#     if x=="wait":
#         z = input("now, which color door would you choose: red or blue or yellow: ").lower()
#         if z=="yellow":
#             print("You win!")
#         else:
#             print("Game Over")
#     else:
#         print("Game Over")
# else:
#     print("Game Over")

# my_favourite_num = 3.1415


name1=input("enter your name: ")
name2=input("enter your frens name: ")
name=name1+name2
print(name)
lower_name=name.lower()
t=lower_name.count('t')
r=lower_name.count('r')
u=lower_name.count('u')
e=lower_name.count('e')
first_digit=t+r+u+e
l=lower_name.count('l')
o=lower_name.count('o')
v=lower_name.count('v')
e=lower_name.count('e')
second_digit=l+o+v+e
num=int(str(first_digit)+str(second_digit))
print(num)
if num<10 or num>90:
    print("Great Couple!!")
elif num>=40 and num<=50:
    print("alrite together")
else:
    print("Not a Couple")



