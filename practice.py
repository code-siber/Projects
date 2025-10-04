# # PROJECTS
# #Function to print("hello world")
# def prints(message):
#     print(message)
# prints("hello world")

# #Print name 5 time
# def prints(name, times = 1):
#     for i in range(times):
#         print(name)
# prints("my name", 5)

# #print 1- 10
# def prints(numbers):
#     number = 2
#     for number in range(1, numbers):
#         print(number)
# prints(11)

# # Function to display a multiplication table of 2.
# def numver():
#     for num in range(1, 11):
#         print(f"2 x {num} = {2*num}")
# numver()

# # Function to print a line of stars (****).
# def star():
#     print("****")
# star()

# # Function to greet the user with “Good Morning”.
# def to_greet(greet):
#     print(greet)
# to_greet("Good Morning")

# # Function to print the even numbers between 1–20.
# def even():
#     for num in range(1, 21):
#         if num % 2 == 0:
#             print(num)
# even()

# # Function to print a triangle pattern of stars.
# def stars():
#     for i in range(1, 6):
#         print("*" * i)
# stars()

# Function to calculate and print sum of numbers from 1–50.
# def sum_num():
#     total = 0
#     for num in range(1, 51):
#         total += num
#     print("total", total)
# sum_num()

# find the letter is vowel letter or not
# string = "Anshul"
# def vowl(string):
#     for vowel in string:
#         if vowel.lower() in ["a", "e", "i", "o", "u"]:
#             print(vowel)
# vowl(string)

# # Function that takes a number and prints its square.
# number = int(input("enter number for square: "))
# def sq(number):
#     print(number**2)
# sq(number)

#  Function that takes a number and prints its cube.
# num = float(input("enter a number: "))
# def func(num):
#     print(num ** 3)
# func(num)

# Function that takes two numbers and prints their sum.
# def func(num1, num2):
#     total = num1 + num2
#     print("total sum of number",total)
# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))
# func(num1, num2)

# Function that takes two numbers and prints the larger.
# def larg(num1, num2):
#     if num1 > num2 :
#         print(f"Num1 = {num1} is the largest")
#     else:
#         print(f"num2 = {num2} is the largest")
# num1 = float(input("enter 1st number:"))
# num2 = float(input("enter 2nd number:"))
# larg(num1, num2)

# Function that takes name as parameter and prints “Hello, ”.
# def func(name):
#     print(name)
# func("hello")

# Function that takes age as parameter and checks if eligible to vote
# def able(age):
#     if age >= 18:
#         print("you are eligible to vote.")
#     else:
#         print("you are not eligible to vote.")

# age = int(input("enter your age : "))
# able(age)

# function that takes number and shows their multiplication table
# def multi(number):
#     for num in range (1, 11):
#         print(f"{number} x {num} = {number * num}" )
# number = int(input("enter number: "))
# multi(number)

# function that takes string and prints separately each
# def func(strng):
#     for each in strng:
#         print(each)
# func("anshul")

#function that creates lines of stars
# def func(stars):
#     for i in stars:
#         print(i)
# func("**********")

# def comp(menu):
#     print(menu)
#     choice = input("enter your choice: ")
#     num1 = float(input("enter num: "))
#     num2 = float(input("enter num: "))
#     if choice.lower() in ["1", "add"]:
#         print(f"ADD = {num1 + num2}")
#     elif choice.lower() == ["2" , "multiply"]:
#         print(f"MULTI = {num1 * num2}")
#     elif choice.lower() == ["3" , "sub"]:
#         print(f"SUB = {num1 - num2}")
#     elif choice.lower() == ["3" , "sub"]:
#         print(f"DIV = {num1 / num2}")
#     elif choice.lower() =="ok":
#         print("ok")
# comp("""
#     1.) add
#     2.) multiply
#     3.) sub
#     4.) divide
#     5.) ok
#     """)

# my_list = [1, 2, 3]
# value = int(input("enter the number:, "))
# try:
#     removed = my_list.remove(value)  # element not in list
#     print(f"new list, {my_list}")
# except ValueError:
#     print("Error: Element not found in list!")
# except():
#     print("something went wrong")
squares = []
num_list = [1, 2, 3, 4, 5]
squares = [ num**2 for num in num_list if num >= 2]
print(squares)  