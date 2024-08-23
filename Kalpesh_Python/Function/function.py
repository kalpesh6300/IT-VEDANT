
'''#Function :
  #Fuction is a block of code defined with a name.
   We use function whenever we need to perform some task multiple times without writing the same code again.
   It can take arguments and returns the values.
   python works on 'DRY' principle.
   Don't Repeat Yourself (DRY) .
   Function improves effiecency and reduces error because of readability of a code.

  Advantages :
      1. Function encapsulate reusable code :
          This means your code more organized easy to read and promotes code reuse.

      2. Moduler code design:
          Broken down large program into small program/more.

      3. Code reusability.
      4. abstraction. 
      5. Support code maintainability.

 Types of Function :
     1. Built in function.
     2. User defined function.
  
Create a function :
    1. Use def keyword with function name to define function.
    2. Pass No. of parameters as per your requirements.
    3. Define a function with function body with a block of code is nothing butaction you wanted tp perform.
    4. Use return to return value.

def function_name (parameters1, parameters2...) :
    #function body
    return value

function_name(actual value)

#Write a program in python to show addition of two numbers:
#Create a Function with parameter :

def addition(num1,num2) :    #parameters                
    result = num1 + num2   #function body
    return result
print (addition(2, 4))

#Create a Function without any parameter :

def msg() :
    print ("Welcome to Itvedant")
msg()

 #Docstring :
     Documentation string
     Descrpitive text written by programmer to let other know what
     block of code does single line docstring , Multiple line docstring.
   
def even_number(num):  """This function is used to show whether given number is even or odd"""
    if num%2==0:
       return "even"
print(even_number(8))    

def msg():
    return "Hello"
    return "Rutuja"
print(msg())

#Scope and lifetime of variables :
In python the scope of variable is an area where a variable is declared.

#local scope
#Global scope

var="Rutuja"      #declared inside function scope => global
def var_scope() :
    local_var1 = "Kalpesh"  #declared inside function scope => local
    print(local_var1)
    print(var)
    
var_scope()

#Different Between Local and Global :

Local Variable                                               Global Variable
1. Variable declared inside the function       1. Variable declared outside of
that is not accessible from outside of              function.
function.

2. scope => local                                         2. scope => global


# function arguments :
    1. positional arguments
    2. keyword arguments
    3. default argument
    4. variable length argument

# 1. positional arguments :
       positional arguments are arguments that are passed to function in proper position.

def sub(num1,num2):      #num1 => 4   num2 => 2
    return num1-num2
print(sub(4, 2))

#2. keyword arguments :

def msg(name,surname) :
    return "Hello", name, surname
print(msg(name="Rutuja",surname="Mhatre"))

#3. default argument :

def msg(name="Ekta") :
    print("Hello", name)
msg()
msg("Rutuja")

#4. variable length argument :

def mul(num1,num2) :
    return num1*num2
print (mul(4 , 2))

   #or
  #find multiplication of multiple numbers: 
def mul(*num) :  
    result = 1
    for i in num:
        result=result*i
    return result
print (mul(4 , 2))
print (mul(4 , 2, 3))
print (mul(4 , 2, 3, 4))
print (mul(4 , 2, 3, 4, 5))

#find addition of multiple numbers:
def mul(*num) :  
    result = 0
    for i in num:
        result=result+i
    return result
    
print (mul(4 , 2))
print (mul(4 , 2, 3))
print (mul(4 , 2, 3, 4))
print (mul(4 , 2, 3, 4, 5))

#Recursive Function :
   A function call itself again & again.

# Find factorial numbers: 
def factorial(num) :  
    result = 1
    for i in range (num, 0, -1):
        result = result * i
    return result
print (factorial (5))

          #or both are right 

def factorial(num) :  
    result = 1
    for i in range (1, num+1):
        result = result * i
    return result
print (factorial (5))       


#Recursion :
def fact (num) :            #fact(5)
    if num == 0 :             #5==0 -> no
        return 1
    else :
        return num*fact(num-1)  #5*fact(5-1) -> 5*fact(4)       #5*4*fact(4-1)
print (fact(5))    
   

#Swapping of two numbers :
num1 = 20
num2 =40
print("Before Swapping :",num1, num2)

#Using temp variable 
temp = num1
num1 = num2
num2 = temp
print("After Swapping :",num1, num2)

#Without using any other variable
num1,num2=num2,num1
print(num1,num2)


#Write a program in python to show fibonacci sequence : ******
#0, 1, 1, 2, 3, 5, 8, 13
#num1, num2 =>0, 1
#num3=num1+num2

iterations = int(input("Enter iteration :"))
num1, num2 =0, 1
count = 0
if iterations<=0 :
    print("Enter Positive Number")
elif iterations ==1 :
    print(num1)
while(count < iterations ) : #0<6                                  #1<6                                #2<6
    print(num1)                  #0                                       #1                                     #2
    result = num1 + num2   #0+1 => result = 1             #1+1 => result = 2            #2+1 => result = 3
    num1 = num2                #1,  num1= 0 => 1              #num1 = 1                        #num1 = 2
    num2 = result                #num2 = 1, num2 = 1         #num2 = 2                        #num2 = 3
    count = count +1           #count = 1                          #count = 2                        #count = 3

#########################################################
#0, 1, 1, 2, 3, 5  <= Output
def recur(num) :
    if num<=1:
        return num
    else:
        return recur(num-1) + recur(num-2)
iterations = 6
if iterations <= 0 :
    print("Positive Number")
else:
    for i in range (iterations):   #i in range (6) => (0, 5) => i=> 0
        print(recur(i))
#########################################################

#Advantages of using recursive function:
    1. Reduce length of code
    2. Redability of code improves due to code reduction
    3.Useful for complex problem

#Anonymous Function :
    Anonymous function is also called as lambda function
    A function without name is called as anonymous function
#Syntax :
    lambda arguments : expression
    
#lambda function consist of number of arguments but only one expression.    
 
#difference between lambda function and normal function :
num = 20
result = lambda num1 : num1**2
print(result (num))

#Show addition of given three numbers 40, 50 ,60 ?
num1 = 40
num2 = 50
num3= 60
result = lambda num1,num2,num3 : (num1+num2+num3)
print(result (num1,num2,num3))

#Write a program in python to find square of number where number is present
list1= []
terms= int(input ("Enter Number how many numbers :"))
for i in range (terms):
    num = int(input("Enter Numbers :"))
    list1.append(num)
print(list1)    

result = list(map(lambda num:num**2,list1))
print(result)

#Module :
Module refers to the python files which contains python code, variables, functions and classes.
A file where python cdode is defined with .py extension is called as module.

#Two types of modules :
    1. Built in module
    2. User defined module.
    
#Moduler programming :
    Moduler programming is the practice of segmentations single, complicated
    coding task into multiple simpler easy sub tasks.

Advantages :
    1. Simplification
    2. Flexibile
    3. Resuability of code
    4. Scope

Create a module :

import claculator
result = claculator.add(2,4)
print(result)

result = claculator.addition(2, 4, 3, 5, 6)
print(result)

result = claculator.substraction(5, 3)
print(result)

result = claculator.multiplication(5, 3)
print(result)


#How to import module?
#import module_name
#from modulename import *
#* symbol : used to import all names from module

import math
print(math.factorial(5))

from math import sqrt
print(sqrt(36))

from math import *
print(ceil(12.5))   #13
print(ceil(12.3))   #13
print(ceil(12.7))   #13

print(floor(12.3))  #12
print(floor(12.5))  #12
print(floor(12.7))  #12

print(pow(2,4))  #16.0  (always give you in float number)
print(cos(23.4))  #-0.16123796432418885
print(pi)  #3.141592653589793


import random
#print (random.randint(1000, 9999))

#print(random.random())
#Return the next random floating- point number in tn range 0.0 <= X < 1.

#print (random.random()*100)  #85.69918585407467

list1= [2, 4, 5, 6, 7, 8, 9, 1]  
print(random.choice(list1))   # output -> 9 

(random.shuffle(list1))
print(list1)                           # output -> [1, 9, 5, 8, 7, 2, 6, 4]


import os
#print(os.listdir())

#current working directory
#print (os.getcwd())
#os.mkdir("python_project")  #make directory
#os.rmdir("python_project")  #remove directory

path = "kalpesh"
os.chdir(path)
print(os.getcwd())

import sys
print(sys.version)
##############################################################
import datetime
dt1=datetime.datetime(2024,4,5)
#print(dt1)
#print(datetime.MAXYEAR)
#print(datetime.MINYEAR)

cdt = datetime.datetime.now()
print(cdt)
print(cdt.year)
print(cdt.month)
print(cdt.day)
print(cdt.hour)

##############################################################

#packages :
    Collection of python modules under a common namespace.

    It is directory that contains a specific file_init_.py
    and one or more modules files and sub packages.
#collection of modules
#modules that are related to each other are mainly put in same packages

pip install django 

#pip
#package installer :
It allows you to install and manage additional libraries and dependencies
that are not distuributed as part of standerds library.
 '''
#######################IMPORTANT QUESTION TO LEARN########################################
#What is a python script and advantages of python?
# what is dynamically type language?
# What is pep8 and explain it significant ?
# What does python scope ? local scope and global scope
# What are an list and tuples? what are the key different ?
# What are the modules and packages ?
# What is the DOSC
#What is silcing ?
# How is python interpreted ?
#What is lambda function ?
#what is pip ?
#Can you convert list to dictinary object ?
#HDLC models
#Recursive Function
#How to convert string to number ?
# What is a python path in a python ?
  -> Python path  is enviormental variable that tells python where to look for modules and packages that are not ina standard library .
#Explain list comparsion with example?
#What is Map Function ?
  
#######################IMPORTANT QUESTION########################################

#Write a python program to interchange first and last element in a list ?
# Write a python program to print even length in a string ?
# Write a python program to find a second smallest number in a list ?
# Write a python program to
