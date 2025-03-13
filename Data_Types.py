# int() non decimal
# float() decimal
# bool() True False
# str() anything between " "
# tuple()


# print("hello"[0]) o/p: h

# print("hello"[0],"hello"[1],"hello"[2],"hello"[3],"hello"[4]) o/p: h e l l 0

# print("hello"[-1]) o/p: o
# print("hello"[-5],"hello"[-4],"hello"[-3],"hello"[-2],"hello"[-1]) o/p: h e l l 0

# print(123+456) o/p: 579
# print("123"+"456") o/p: 123456 (bcz anything between quotes is a string)
# len(123) o/p: error (len function will calculate only string which is in quotes)
# print(len("123")) o/p: 3

# print(222.002+333.003) o/p: 555.005
# print(222_002+333_003) o/p: 555005 (222_002 OR 222002 are same)
# print(111.11+222.22, 11+12) o/p: 333.33 23

# num_char=len(input("what is ur name?")) pvk
# print(num_char) o/p: 3
# print(num_char + " characters long") o/p: error (print(int + string))
# print(num_char, " characters long") o/p: 3 characters long

# num_char_1=str(num_char)
# print(num_char_1+ " characters long") o/p: 4 characters long


# y=len(input())
# print(y, " characters long") o/p: 4 characters long (print (int, string))
# print(type(y)) o/p: int

# a=123
# print(type(a)) o/p: class <int>

# a=str(123)
# print(type(a)) o/p: class <str>

# a=float(123)
# print(type(a)) o/p: class <float>
# print(a) o/p: 123.0

# print(70+float(100.5)) 170.5
# print(70+int(100.5)) 170
# print(str(70)+str(80)) 7080
# print(str(70)+str(80.6)) 7080.6
# print(str(70),float(100.5)) 70 100.5
# print(int(70)+float(100.5)) 170.5
# print(str(70)+int(70)) error

# add 2 digit number
# y=two_digit_number=input()
# a=int(y[0])
# b=int(y[1])
# print("sum:",a+b)

# print("Number of letters in your Name:" + len(input("What is your name: "))) error print(str + int)
# print("Number of letters in your Name:", len(input("What is your name: ")))
# print("Number of letters in your Name: " + str(len(input("What is your name: "))))
