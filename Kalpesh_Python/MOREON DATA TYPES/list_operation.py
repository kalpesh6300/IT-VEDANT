
'''
List :

    List is a collection of different types of data.

    Characteristics of list :
        1. Ordered:
            Lists are in Order.
        2. Changeable :
            List are mutable.
        3. Lists Elements are accessed by index value.
        4. Heterogeneous:
            Different types of data included in lists.
        5. Duplicate Element :
            Lists allow duplicate element.

# How to create list?
#empty lists

lists=[]
print(type(lists))

list1=list()
print(type(list1))

lists = [1, 2, 3, 4, 5, 6]
print(lists)
print(type(lists))

lists =[1, "priya", 3.14, True]
print(lists)
print(type(lists))

lists =[1, "priya", 3.14, 3.14, True] # Duplicate Value also Print()
print(lists)
print(type(lists))

lists =["Mobile", "Laptop", "Mouse", "Laptop Bag"]
print(lists)

#Indexing List :
#Slice Operator is used []
Print(type(lists[0])) # Return Datatype (str) *****
print(lists[0]) #Mobile
print(lists[1]) #Laptop
print(lists[2]) #Mouse
print(lists[3]) #Laptop Bag
print(lists[-2]) #Mouse

#Accessing elements of lists :
Print(lists[0 : 2])
Print(type(lists[0 : 2])) # Return Datatype (list) *****

#Iterating a List :
lists = ["Python Programming ", "SQL", "Core web Design", "Django"]
for i in lists:
    print(i)

#Iterating with index :           example:  0  1  2  3 <- index Value
for i in range (len (lists)):      #lists = [1, 2, 3, 4]  <- List Value
    print(lists [i])

# Adding element into Lists :
1 . insert
2 . append
3 . extend

#1 . insert() :
  #Add element at specified location.
  #syntax :
  #insert(index, value)

list1 = ["Red", "Green", "Yellow", "White", "Blue", "Black"]
list1.insert(2, "Violet")
print(list1)

#2 . append() :
#Add element at end of given list. (last m add hoga)
list1 = ["Red", "Green", "Yellow", "White", "Blue", "Black"]
list1.append("Brown")
print(list1)

#3 . extend() :
# add list of element.
list1 = ["Red", "Green", "Yellow", "White", "Blue", "Black"]
list1.extend(["Gray", "Orange", "Pink"])
print(list1)

#Modify the Lists :
lists = ["Python Programming ", "SQL", "Core web Design", "Django"]
lists[1] = 20
print(lists)

lists = ["Python Programming ", "SQL", "Core web Design", "Django"]
lists[2 : 3] = 30,40
print(lists)

#Removing an element from list :
1 . remove ()   remove the first occurance of an element. #value
2 . pop(index)  remove and return the item at given index.
3 . clear()      Only removes values and return empty list .  
4 . del            delete that lists.


lists = ["Python Programming ", "SQL", "Core web Design", "Django", 88]
lists.remove(88)        #exact value => None
print(lists)

lists.pop(3)              #index value => return deleted value
print(lists)

lists.clear()             # Only removes values and return empty list 
print(lists)

lists.del()               #delete that lists.
print(lists)


#Concatenating List :
#+
#exend ()

#+
list1 = [1, 2, 3, 4]
list2 = [2, 4, 9, 16]
print(list1 + list2)

#extend()
list1.extend(list2)
print(list1)


# Copying List :
# =   => deep copy   ****
list1 = [1, 2, 3, 4]
list2 = list1
print(list2)

# .append()
list1.append(5)
print(list1)
print(list2)

#copy()  => shallow copy   ****
list3 = [1, 2, 3, 4]
list4 = list3.copy()
print (list4)

list3.append(45)
print(list3)    #[1, 2, 3, 4, 45]
print(list4)    #[1, 2, 3, 4]


#sort in Ascending sort() :
list1 = ["Priya", "Python Programming","Abhishek", "Django"]
list1.sort()
print(list1)

#reverse () :
list1.reverse()
print(list1)

#Built in function :
list1 = [55, 66, 77, 88, 77]
print(max(list1))
print(min(list1))
print(sum(list1))

#count() check occurances of specified element.
print(list1.count(77))

#index()  => return index value of specified element.
list1 = [55, 66, 77, 88, 77]
print(list1.index(55))


#list Comprehensions :
#This is simpler method to create a list using and exisiting list
syntax:
ouput_list = {expression(variable) for variable in inputlist
                     [if variable condition1] [if variable condition2]}   


#print first 5 numbers:
num = int(input("Enter Number :"))
newlist = [i for i in range(num)]
print (newlist)


list1 = [1, 2, 3, 4]
for i in list1 :
    print(i**2)
    
new_list =[i**2 for i in list1]    
print(new_list)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []
for i in list1 :
    print(i)
    if i%2==0 :
        new_list.append(i**2)
print(new_list)

# or

new_list = [i**2 for i in list1 if i%2==0]    #list Comprehensions :
print(new_list)


#Multidimensional List :
# list within list
                #0                  1                    2
list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print (list1 [0][2])

list1[0].extend([20, 30, 40])
print(list1)


#Tuple :
#Tuples are ordered collection of hetrogeneous data that are unchangable.

tuple1=()
print(type(tuple1))

tup= tuple()
print(type(tup))

tuple1 = (1, 2, "Priya", True)
print(tuple1)
print(type(tuple1))

tuple1= ("Priya",)  #****  (, for assign is tuple)
print(type(tuple1))

tuple1 = ("Python", "Sql", "Core web", "Django", "Sql")
print(tuple1.count("Sql"))

print(tuple1.index("Sql"))

# IMPORTANT => Different between List and Tuple ?
List                                                       Tuple
1.list is mutable.                                    1.Tuple is immutable.
2.list element enclosed within [].           2.Elements enclosed within ()parenthisis.
3.lists are slower than tuple.                  3.Tuples are faster than list.
4.list consume more memory .                4.Consume less memory as compared to list
5.Elements can be modified after           5.can't change elements.
   the assignment.

#set
set is an unorderd collection of data items that are unique
set is defined with {}

set1={1,2,3,4,4,5}
print(set1)
print(type(set1))

set1=set()         #empty set
print(type(set1))

set1={1,2,3,4,4,5}
set1.add("kalpesh")
print(set1)

set1.update([6, 7])
print(set1)

set1.remove(6)
print(set1)
'''

#tuple packing
tuple1= 10, 20, 30, 40
print(type(tuple1))

#tuple unpacking
num1, num2, num3, num4 = tuple1
print(num1, num2, num3, num4)
'''



######################################################################
Q1)What is PEP-8 ?
1. Python Enhancement Praposal (PEP8).
2. It provide convince for writting clean and readable abd consitent python code.

Q2) What is different betwwen append and extend and insert ?

Q3) What is different between

Q4) Can you explain how python impliments dynamic typing.
   -> Python impliments dynamic typing by allowing variables to reference object without explicit type declaration.
   -> The type of variable is determine as runtime.

######################################################################
#Removing An Element from Set :
1. remove () :
    Remove Single item.
    Throws Key error if an item is not found.

2.discard () :
   remove single item
   not throws keyerror if an item is not found

3.pop () :
   remove random element.

4.clear () :
   empty set

5.del set1 :
   delete set

#1. remove () :
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set1.remove(31)               #remove () throws eroor if element not found
print(set1)

#2.discard () :
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set1.discard(4)               
print(set1)   

#3.pop () :
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set1.pop()               
print(set1)

#4.clear () :
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set1.remove()               
print(set1)

#5.del set1 :
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
del set1              
print(set1)


#set operations:
operation                     symbol
1. union                            |
2. intersection                  &
3. difference                     -
4. symmetric difference    ^

#1. union  
set1 = {2, 4, 6, 8, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.union (set2)
print(set3)
#or
set3 = set1| (set2)
print(set3)

#2. intersection
set1 = {2, 4, 6, 8, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.intersection (set2)
print(set3)
#or
set3 = set1 & (set2)
print(set3)

#3. difference
set1 = {2, 4, 6, 8, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.difference (set2)
print(set3)
#or
set3 = set1 - (set2)
print(set3)

#4. symmetric_difference
set1 = {2, 4, 6, 8, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.symmetric_difference (set2)
print(set3)
#or
set3 = set1 ^ (set2)
print(set3)

#Dictionary :
#Dictionary are collection of elements in key value pair.
#Dictionary is mutable.
#Dictionary is mapping between key and value pair.
#Unordered 3.6 /

#Creating a Dictionary :
#1. Using a curly braces dict {}
emp = {"name": "rutuja","address":"kalyan"}
print(emp)

#Creating Dictionary :
1. {}
2. dict ()
3. using sequence

emp = dict([('name' , 'rutuja'),('address' , 'kalyan')])
print(emp)

dict1={}
print(type(dict1))

#accessing element from dict
1. []
2.get ()

#1. []
emp = {"name": "rutuja","address":"kalyan"}
print(emp['name'])

#2.get ()
print(emp.get('name'))

emp = {"name": "rutuja","address":"kalyan"}
print(emp.keys())
print(type(emp.keys()))
print(emp.values())

#Iterating a Dictionary :
student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98}
for key in student :
   print(key, ":", student[key])

print(student.items())
   
#keys are unique values can be duplicate :
student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98,"Core Web Design" : 89}
print(student)

#Adding an element in dictionary :
1. Using key value pair assignment.
2. Update method

student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98}
student['Django'] = 97
print(student)
#or
student.update({"React" : 89, "js" : 90})
print(student)

#set default :
student.setdefault("Profile Building", 40)
print(student)

#removing an element from dict:
1.pop() : return and remove the item with the key and retuen its value if key not found => throw keyerorr.
2.popitem(): return and remove last inserted item from the dictionary.
3.del key : particular key delete.
4. clear
5.del dict1

#1.pop() : 
student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98,"Core Web Design" : 89}
student.pop("Sql")
print(student)

#2.popitem():
student.popitem()
print(student)

#3.del key :
del student ['Core Web Design']
print(student)

#4. clear :
student.clear()
print(student)

#copy dictionary :
student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98,"Core Web Design" : 89}
dict2 = student.copy()
print(dict2)

#Dictionary Comprehension :
output_dict = {key:value for key, value in iterable[if key, value condition :]}

numbers = [1, 2, 3, 4, 5]
dict1={}
for i in numbers :
   if i%2==0 :
      dict1[i] = i**2
print(dict1)

      or  #Dictionary Comprehension
      
result = {i : i**2 for i in numbers if i%2==0}  
print(result)

# Examples :
# Q1)write a program to sum all subject marks in a dictionary (addition) :
student = {"Core Web Design" : 89, "Python" : 99, "Sql" : 98}
print(sum(student.values()))

#Q2) Take a string a user
name = "Kalpesh Mhatre"
dict1={}
for i in name :
    dict1[i] = dict1.get(i , 0) +1
print(dict1)
'''
