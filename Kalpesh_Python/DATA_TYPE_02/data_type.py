'''
#Data Type:
     #Data types are used to represent the nature of the data
    # that can be stored in the vaiable

# Numeric datatype:
#int
num1=50
print(num1)
print (type(num1))

#float
num1= 20.5
print(num1)
print (type(num1))

#complex
num1 =1 + 3j
print(num1)
print (type(num1))
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
#string
#set of characters enclosed within single or double quotes or sometimes in  triple quotes
name = "Kalpesh"
print(name)
print(type(name))

name = 'Kalpesh'
print(name)
print(type(name))

name = """Kalpesh """
print(name)
print(type(name))

name = ''Rutuja 
               is the best ''
print(name)
print(type(name))

# \ is called continuation character
name = 'Kalpesh \
              Mhatre'
print(name)
print(type(name))
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
#list
list1= [10, 20, 30, 40]
print(list1)
print(type(list1))

list1= [10, 20, 30, 40, "Rutuja", 24.2]
print(list1)
print(type(list1))

#tuple
# we can't change document
tuple1 = (10, 20, 30, 40)
print(tuple1)
print(type(tuple1))

#dictionary (key value pair is their)
dict1 = {'Rutuja' : 90, 'Gauri' : 89}
print(dict1)
print(type(dict1))

#set (assign only unqiue one no duplicate)
set1 = {10,20,20,30,40}
print(set1)
print(type(set1))

#Bolean
value = True
print(value)
print(type(value))

# Taking input from user
name = input("Enter your name :")
print(name)

# Type  casting :
#It is meathod to  convert python variable datatype into another datatype
# 1. Implicit type casting
       #automatically converted from one datatype to another.

# 2. Explicit type casting
       #User can convert one datatype to another.

# 1. Implicit type casting
num = 30
print (type(num))

num1 = 40.5
print (type(num1))

result = num + num1
print (result)
print (type(result))

# 2. Explicit type casting
#string -> int (gives you output)
num = input ("Enter your number :")
print (num)
print(type(num))

#int -> float (gives you output)
num = 20
num = float(num)
print(type(num))

#float -> int (gives you output)
num = 50.4
num = int(num)
print(type(num))

#string -> int with number  (gives you output)
string = "10"
st = int (string)
print(st)
print(type(st))
'''
#string -> int with number  (error)
string = "hello"
st = int (string)
print(st)
print(type(st))

#string -> float with number  (error)
string = "20.0"
st = int (string)
print(st)
print(type(st))
