  Arithmetic operator 
#   Arithmetic operator = (+, -, %, *, /, **, //)
  relational operator = 
#   relational operator = (>, <, <=, >=, ==, !=)
  Logical operators   = 
#   Logical operators = (and, or, not)
  membership operator = 
#   membership operator = (in, not in)
  Assignment Operator = 
#   Assignment Operator = (=, +=, -=, *=, /=)
  Input statement = 
#   (input(x))


   OTHER
#   Tab = /t
#   Separate = sep()
#   Control flow statements 
#      conditional statement\
#         if statement
#         if , elif, else

___________________________________________________________________________________________

   Looping statement
   Finite Loop  :
#  for loop
   Infinite Loop :
#   While loop
#       while True:
#        if not condition 
#              continue
#         elif condition 1 : 
#         elif condition 2:
#             condition 3 (optional ho bhaney)
# 
#         break

#           For loop
#           for num in range(1, 10): {{This means starting is 1 and end ing is 10}}
#         #   for num in range(1, 10, 2): {{This means starting is 1, ending is 10 and 2 is step }}
#             # lIKE EXAMPLE = (1,10) ONLY INCREASE NUMBER COUNT BY 1 AND IF WE ADD STEP 2 THEN THE DEFAULT INCREASE WILL BE CHANGED TO 2


____________________________________________________________________________________________


         Function
#    Def func(parameter):
#         syntax()
#    put syntax to determine variable
#    func(parameter)
#  Function call : func(parameter is also known as argument in call. )
#  Keyword argument : func(name="str") {where name is parameter or argument, In order to specify the type like "str" is name but not other any parameter}
#  Default parameter : giving a parameter default value like if i want greeting hi as default in def func(greeting = "HI")
         Argument holder :
#                    [def func(*args)]
#                    [OUTPUT = 1, 10, 2, 50] {any num of arguments}
         Return = 
#             .return = returns value in def
#  .insert() or .append() in variable add value
#  .pop() or del function = remove from variable 
#  u can choose place by adding number where 0 is the starting 
#  variable1 = variable.pop() shows the variable that is removed
#  Tuple > once created, cannot change
          List = 
#       used to store value also denoted by [] which can be changed unlike tuple
#  from 1 part of list to another like [0,1,2,3,4] ma 2 to 4 samma chhaio bhaney ":" is used like
                #  a = [0,1,2,3,4] { position is determined by starting with 0}
                #  b = a[2:4]
        
 _________________________________________________________________________________________________________________       
        
        
          .intersection 
#               = common elements between 2 variables
                # common = variable1.intersection(variable2) or common = variable1 & variable2
#  .union = include all between 2 variables or | also perform same
#  .difference or "-" where variable1 - variable2 removes common and shows remaining in the variables
#  .items key values like
                # names = {"
                # "name"= "user"}
            #  OUTPUT = name = user
#   "name" : "User"
    # Keys       value

__________________________________________________________________________________________

            enumerate = 
#       like number ra students lai 1.) students format ma dinxa


           modules = 
#       import module , from module import packages, from module import * then del unwanted module

# MODULE LIST
# Math
# Time
# datetime
# Random : list of card suffle
# Qr code
# helper


# package : __init__.py
# Exception handling
        # try: and except variableerror: or except:
        # except: (for all error)
        # finally:


_______________________________________________________________________________________

file handling =
        # file = open("file.txt", "r")
        # open file
        # read file = r
        # write file : write new data = w
        # append file = a
        # close file
# open = opens new file if not present
#  new_file = open("new_file.txt", "w")
#  new_file.write("new content inside new file")
# /n = new line
#  new_file.writelines(line)
# /t = tab space for example = 1, 2, 3, "ram", sep=" "
# new_file.append("add new content inside new file")
# with open("new_file.txt", "a") as new_file:
#   new_file.write("new content inside new file")
# if file doesnt exits it shows file not found error
# CSV file handling
# csv module
# import csv (python inbuilt module)
# with open("file.csv", "r") as file:
#   writer = csv.reader(file)
#   writer.writerow(["name", "age"])
# w denotes write mode
# a denotes append mode
# r denotes read mode

___________________________________________________________________________________________


    lamda function = 
#  lamda function without name
#  add(Variable) = lambda x, y : x + y
#  add(2, 3)
# it is used in high order function for example map, filter, reduce etc
# map = applies function to all items in iterable like list, tuple, set etc
# filter = applies function to all items in iterable like list, tuple, set etc 
# higher order function = function that takes another function as argument
# for example : def add(function as parameter or argument):
#                 return function

_________________________________________________________________________________________

          filter()= 
# all_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_num = list[filter(lamda num: num % 2 == 0, all_num)]
# print(even_num)

__________________________________________________________________________________________________

OOP = Object oriented programming
# class =(always start with capital letter) 
          # blueprint or what type of object (like car, bike, laptop etc) u want to create
# object = product and its properties/ object related data

example =
# class Car:  
      pass
# car1 = Car() {object of class car}
# class Car:
#       def __init__(self, color, make, model):
#             print("car is created\nthe car details are:")
#             self.color = color
#             self.make = make
#             self.model = model
# farari = car("red", "toyota", "farari")   { if we dont fill the parameter for the object it shows error like red for color, toyota for make and farari for model}

class ->  new datatype with full control over other data and its behaviour
object -> 