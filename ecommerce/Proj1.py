#print ( 'I','Love',sep='_',end='\t')
#print ('My','India' )
#a=int(input('Enter a'))
#print(a)
#print(type(a))

#for i in range (0,15,1):
   #print(i)

#Continue and break----------------------
# a=int(input("enter the number"))
# for i in range(0,10,1):
#     if i == 5:
#         continue
#     if i == 6:
#         break
# print(i, end=' \n')
#While loop------------------------------
# a=0
# while a in range (0,10):
#     print (a)
#     a+=1
#List
#Lst = [10,20,30,40]
#print (10*2 in Lst)
#print (Lst[-1])
#print (Lst [1])
#List = ["apple","bag","cat","dog"]
#List.append("egg")
#print(List.pop)
#print(type(List[1]))
#print(List)

#tuple
#tuple=(1,2,3)
#print(max(tuple))
#print(tuple)

#pop
#Lt = [1,2,3]
#print(Lt)
#a=Lt.pop(0)
#print(Lt,a)

#slicing
#a='aeroplane'
#print(a.title())
#print(a[1:10:3])

#Palindrome
#a=str(input("Enter the name"))
#b=(a[::-1])
#c=(a[0:10:1])
#if a==b:
 #   print('its a palindrome',b )
#else:
 #   print('Not a palindrome',b)

# Tup=(10,20,30,40,50)
# print(Tup[1:5])

#MOSH
#Augmented string f'{}

# #convert from pound to kg
# a=float(input("Enter your weight in pounds"))
# b=a*0.454
# print('Your weight in pounds',a )
# print('Weight in kilogram',b)
# print(type(b))

#strings
# school_name='Drove Primary school'
# print(school_name[:-3])

 #Formatted string
# fruit_name=str(input('Enter fruit name'))
# Type_name=str(input('Enter fruit type'))
# print(f'{Type_name} {fruit_name} tastes good')

#string methods
#Student_Name='Ramya works in Accenture'
# #print(len(Student_Name))
# #print(Student_Name.join('1.'))
#print(Student_Name.find('my'))
#-- returns indices
# #print(Student_Name.replace('works','worked'))
#print('works' in Student_Name )
# -- returns the words

#Mulitple line strings
# print (''' Hello,

# Good Morning
# Hope you are doing good. please update your leave plan.
#
# Regards,
# Ashwini M
# ''')

#upper/lower
# College_name='Holy cross college'
# print(College_name.upper())
# print(College_name.lower())
# print(College_name.islower())

#Arithmetic Operators
# print(100-43)
# print(48-9)
# print(10*2)
# print(21%4) #modulus
# print(52//3) # fractions
# print(99/3)
# print(5**3)  # power

#Exercise Precedence operator
#x = (2+3) * 10 - 3
#print (x)


#Augmented Assignment operator
# a=50
# a-=3
# print(a)

# a=2
# a+=5
# print(a)

#Operator Precedence -- BODMAS
# p= 5*4-3+2 **2
# print(p)

#rounding and absolute
#import math #python 3 math module
#absolute always returns a positive number
#y=90
#x=-2.7
#print(round(y))
#print(abs(x))
#math.log2(4)

#if
# House_price= 1000000
# Good_credit=True
#
# if Good_credit:
#     print("10% deposit is required")
#     down_payment=0.1 *House_price
# else:
#     print("20% deposit is required")
#     down_payment = 0.2 * House_price
# print(f"The down payment: £{down_payment}")


#Logical Operators
# Applicant_Name="Jennifar"
# high_income = print(high_income
# good_credit=False
# if high_income or good_credit:
#     print(f"{Applicant_Name} is eligible for loan")
# else:
#     print(f"{Applicant_Name} is not eligible for loan")
#
# print('End of statement')

#NOT logical operator
#elif meaning lower limit/uppper limit
# Applicant_Name="Jennifar"
# good_credit=True
# criminal_record=True
# if good_credit and not criminal_record:
#     print(f"{Applicant_Name} is eligible for loan")
#
# print("End of Decision")

#Comparison operators
#Is_hot=input("Enter the boolean" )
# Is_hot=False
# Is_cold=True
# #Is_cold=True
# if Is_hot:
#     print('Its a hot day, drink plenty of water ')
# elif Is_cold:
#     print("It's a cold day, carry an umbrella")
# else:
#     print("It's a lovely day")

#home work
# Applicant_Name=str(input('Enter applicant name'))
# Name_len=len(Applicant_Name)
# print(Name_len)
# if Name_len <3:
#     print(f"{Applicant_Name} must be atleast 3 characters")
# elif Name_len > 50:
#     print(f"{Applicant_Name} must be only 50 characters long")
# else:
#     print("Name looks good")

#Weight converter
# Weight =int(input("Enter the weight"))
# Confirmation=input("(L)bs or (K)g:")
# if Confirmation.upper()=="L":
#     print("Your weight is", Weight*0.454,Confirmation)
# elif Confirmation=='K':
#     print("your weight is",Weight/0.454, Confirmation)
# else:
#     print("Enter L or K only")

#while loop
# secret_number=9
# Guess_count=0
# Guess_limit=3
# while Guess_count<Guess_limit:
#     Guess = int(input("Guess:"))
#     Guess_count += 1
#     if Guess==secret_number:
#         print("you win")
#         break
# else:
#     print("you failed")

#car game
#>help
#start - to start the car
#stop - to stop the car
#quit - to exit
#asd
#i dont understand
#start
#car started... Get ready go

#Blank apostrophe is for strings only
#dont repeat yourself -- dry
# Manual_code=''
# Final_code='quit'
# while Manual_code!= Final_code:
#     Manual_code = str(input(">")).lower()
#     if Manual_code =='start':
#         print('car is started.. Ready to go')
#     elif Manual_code =='stop':
#         print("To stop the car")
#     elif Manual_code=="help":
#         print('''
# start - start the car
# stop - stop the car
# Quit - quit to exit''')
#     elif Manual_code == Final_code:
#         print("To exit")
#         break
# else:
#         print("I don't understand")

#If condition is default true or takes from the initialisation of the program
#Extended project
#
# Manual_code=''
# Final_code='quit'
# started=False
# while True:
#     Manual_code = str(input(">")).lower()
#     if Manual_code =='start':
#         if started:
#             print('car is already started.. Ready to go')
#         else:
#             started = True
#             print('car is started')
#     elif Manual_code =='stop':
#         if not started:
#             print("car is already stopped")
#         else:
#             started = False
#             print('car is stopped')
#     elif Manual_code=="help":
#         print('''
# start - start the car
# stop - stop the car
# Quit - quit to exit''')
#     elif Manual_code == Final_code:
#         print("To exit")
#         break
# else:
#         print("I don't understand")


#For loop
#price =[10,20,30]
#import math
#price = [10, 2, 3]
# a = 0
# for i in [10, 2, 3]:
#     a += i
# print(a)

# for x in range(2):
#     print("XXXXX")
#     for y in range(1):
#         print("XX")
# print("XX")

# #Mosh code
# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     print("X" * i)


#Greater no in the list
# n = [5, 2, 1, 7, 4]
# b = n [0]
# for i in n:
#     if i > b:
#         b=i
# print (b)

#remove duplicate in the list
# n=[5, 4, 3, 4, 2, 3, 3]
# unique=[]
# for i in n:
#     if i not in unique:
#        unique.append(i)
# print(unique)

#Coordinates
# coordinates = [4, 3, 5]
# [x, y, z] = coordinates
# print([x, y, z])

#Tuples
# apple=(1,2,3)
# print(apple)

# #Dictionary
# Client ={
# "name" : "Raja",
# "age" : "39", "Is_Indian" : True}
# Client["Birthyear"]= "1983"
# print(Client[ "Birthyear"])
# phone=(input("Phone:"))
# output=""
# number ={"1": "one",
#          "2": "two",
#         "3": "three"}
# for i in phone:
#     output+=number.get(i,"!") + " "
# print(output)

# a=input("<")
# b=a.split(' ')
# print(b)

#emoji
# message = input(">")
# words=message.split(' ')
# emoji={":)" : "😊",
#  ":(" : "😒",
#   "super":"👌"}
# output=""
# for i in words:
#       output+=emoji.get(i,i)+ " "
# print(output)

#Functions - postitional, keyword arguments
#Positional arguments first

# def good_morning(first_name, last_name):
#      print(''' Hello,
#      Good Morning!
#      Nice Meeting you''')
#      print(f'{first_name}, {last_name}sent this letter')
#
#
# good_morning("Ashwini", "Rajasekaran"), '\n'
# good_morning("George", last_name="phil")

# def square(number):
#     result = number * number
#     return result
#
# print(square(5))

# print L
# number =[2, 2, 2, 2, 2, 2, 2, 10]
# for L in number:
#     print("X" * L)

#Handling exceptions
# try:
#     Age=int(input("Enter age"))
#     print(f'My age is {Age}')
# except ValueError:
#     print("Age should be integer only")

#person name and talk
# class Person:
#     def talk(self):
#         print (f"she likes to talk {self}")
#     def Name(name):
#         print(f'My name is {name}')
#
# fname=Person
# fname.name="Ashwini"
# talk(Bandi)

# person object
# name attribute
# talk method
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print("talk")

# customer = Person("Ashwini")
# customer.talk()
# print(customer.name)

#inheritence
# class Animals():
#     def carnivores(self):
#         print("Carnivores are meat eaters")
# class WildAnimals():
#     def omnivores (self):
#         print("Omnivores are meat/veg eaters")
#
#
# class Dinosaur(Animals):
#     def dino(self):
#         print("Dino dont exist")
#
# class Dog(WildAnimals):
#       pass
#
#
# Dnsr = Dinosaur()
# Dnsr.dino()
# Dog1=Dog()
# Dog1.omnivores()
    
#from greaterno import Find_max
# from greaterno import Find_max
# class Utils:
#     numbers=[1, 3, 4, 7, 9]
#     max = Find_max(numbers)
#     print(max)
#greaterno is the module and Finc_max is the function in it
#from proj.package and then module and then retrieve the function
#python 3 module index
#External library > Python 310 > Lib > Zoneinfo > Random

# import random
# members =["Ashwini", "Raji", "yash"]
# leader = random.choice(members)
# print (leader)

# import random
# for i in range (3):
#     print(random.randint(10, 20))
#class only has objects

# import random
# #
# #
# # class Dice:
# #     def roll(self):
# #         for i in range(1):
# #             x = random.randint(1, 6)
# #             y = random.randint(1, 6)
# #             return x,y
# #
# #
# # play = Dice()
# # print(play.roll())

#Absolute path C:/User/My Computer/ Proj1 and Relative path (ecommerce.py)
#not working
# from pathlib import Path
#
# path = Path("Proj1")
# print(path.exists())

#xl

