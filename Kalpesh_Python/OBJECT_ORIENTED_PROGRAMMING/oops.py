# Class :
'''
 A class is a user define blueprint or prototype from which objects are created.
 Class is a blue print or code template for objects creation, which binds the data members(attributes) and method into single units.

# What is an Object?
Object is an instance of a class .
Object have two charactertics they have (states) and (behavior).
Object represents one class but with different (states) and (behavior).
States means (attributes) or (data member) and Behavior represents (method).
Every objects has following properties :
-Identity
-State
-Behavior
'''
#How to create a class ?
'''
Syntax :
    class class_name :
        "This is docstring"
        <statement 1 ..>
        <statement 2 ..>
        <statement N..>
'''        
#How to create a object ?
'''
 Syntax :
      object_name = classname (arguments)

class student:
    pass
#Create an Object :
obj1 = student()
print(obj1)        
'''

# What is Constructor in python ?
'''
A constructor is special method used to create and (initialized) and (object) .
This method is define in the class :
    1. The constructor is executed automatically when at the time  object creation.
    2. The primary use of this method is to declare and (initialized data members) or (instance variable).
    3. Syntax :
        def __init__(self) :
            # def - it is a keyword used to define a function.
            #__init__(): this method is a reserve method, this method gets call as soon as an object of a class is instantiated.
            # self :  refers to the current object .

#types of constructor :
 1. default constructor .
 2. non parameterized constructor.
 3. parameterized constructor.

#1. default constructor :-
class student :
    def show(self) :
        print("This is show method")
stud1 = student()
stud1. show()

#2. non parameterized constructor :-
class student :
    def __init__(self) :
        self.name = "Rutuja"
        self.address = "Bhiwandi"
        
    def show(self) :
        print(self.name, self.address)
        
stud1 = student()
stud1. show()
'''
#3. parameterized constructor :-
'''
class student :
    def __init__(self,roll,name,address,contact) :
        self.roll =roll
        self.name = name
        self.address = address
        self.contact = contact
        
    def show(self) :
        print("Roll number is :",self.roll, "Name is :",self.name, "Address is :",self.address, "Contact is :",self.contact)
        
stud1 = student(1, "Kalpesh", "Bhiwandi", 7620067160)
stud1. show()

stud2 = student(2, "Ekta", "Kalyan", 8706503954)
stud2. show()
'''
#Destructor :
'''
  Destructor is called when an object is a (deleted) or (destroy) .
  syntax :
  def __del__(self) :  #that object is deleted .
      
 #instance variable in a python :-
  If the value of variable varies from object to object then this variable called as instance variable .

#example :-
class student :
    def __init__(self,roll,name,address,contact) :
        self.roll =roll
        self.name = name
        self.address = address
        self.contact = contact
        
    def show(self) :
        print("Roll number is :",self.roll, "Name is :",self.name, "Address is :",self.address, "Contact is :",self.contact)
        
stud1 = student(1, "Kalpesh", "Bhiwandi", 7620067160)
print(stud1.roll, stud1.name)
'''
##############################################
#class variable :-
#example :-
'''
class student :
    institute_name = "ITVEDANT"
    def __init__(self,roll,name,address,contact) :
        self.roll =roll
        self.name = name
        self.address = address
        self.contact = contact
        
    def show(self) :
        print("Roll number is :",self.roll, "Name is :",self.name, "Address is :",self.address, "Contact is :",self.contact, student.institute_name)
        
stud1 = student(1, "Kalpesh", "Bhiwandi", 7620067160)
stud1. show()

stud2 = student(2, "Ekta", "Kalyan", 8706503954)
stud2. show()
'''
#####################  MultiLevel Inheritance  ##############################
'''
class First:                  #grandparent
    def getnum(self) :
        self.num = int(input("Enter Number : "))
        
class Second (First) :   #parent
    def getnum1 (self) :
        self.num1 = int(input("Enter Number :"))
        
class result_of_number(Second) : #child
    def result (self) :
        addition = self.num + self.num1
        print("Addition :", addition)

res = result_of_number()
res.getnum()
res.getnum1()
res.result()
'''
##################### ( Hierarchical Inheritance ) ##############################
#More than one child derived from single paranet class .
'''
class vehicle :
    def info (self) :
        print("This is vehicle class")

class Car(vehicle) :
    def car_info (self) :
        print("This is car info")        

class Bike(vehicle) :
    def bike_info (self) :
        print("This is bike info")    

bk = Bike ()
bk.bike_info()
bk.info()

cr = Car ()
cr.car_info()
cr.info()
'''
##################### ( Hybrid Inheritance ) ##############################
'''
class vehicle :                 #grandparent
    def info (self) :
        print("This is vehicle class")

class Car(vehicle) :        #parent
    def car_info (self) :
        print("This is car info")        

class Bike(vehicle) :       #parent
    def bike_info (self) :
        print("This is bike info")

class Truck(vehicle) :    #child
    def truck_info (self) :
        print("This is truck info")

class Tempo(vehicle) :    #child
    def tempo_info (self) :
        print("This is tempo info")        

bk = Bike ()
bk.bike_info()
bk.info()

cr = Car ()
cr.car_info()
cr.info()

##continue aahee step wrong aastil
'''
######################################################################
'''
#Super() :-
When a class inherits all properties and behavior from the parent class is called inheritance.
In child class we can refer parent class by using super () function.
The super () function returns a temporary object of parent class that allows us to call parent class method inside a child class method.

benefits :
    not require to remember or specify the parent class name to access its method.

    super ()  - single , multiple

#example :-

class company:
    def company_name(self) :
        return "ITVEDANT"
    
class Employee (company):
    def info(self) :
         c_name = super() . company_name()
         print("Company name", c_name)

emp = Employee ()
emp.info()
'''
######################################################################

#Decorator :-
'''
def div (num,num1) :
   print (num/num1)

#print(div(4,2))
#print(div(2,4))

def newdiv(func) :
    def inner (num,num1) :
        if num<num1:
            num,num1=num1,num
        return func(num,num1) 
    return inner
    
#div1=newdiv(div)
#div1 (2,4)

#or

@newdiv
def div (num,num1):
     print(num/num1)

div(2,4)
'''

#######################( Encapsulation ) #############################
'''
It is process of bundelling data member and methods into single unit.
Using encapsulation,
we can hide an object internal representation from the outside.
This is called as information hiding.

Encapsulation allows us to restrict accessing variable and methods directly.

1.public
2.protected
3.private

1.public :
    Accessible anwhere from outside of class.
    
2.protected :
    Accessible within that class and its subclasses.
    
3.private :
    Accessible within that class.
 '''
#1.public :-
class Employee :
    def __init__(self,name,project,salary):
        self.name=name          
        self.project=project      
        self.salary=salary       
        
emp=Employee("Renuka","Django project",20000)
print(emp.name,emp.project,emp.salary)

#2.private:-
# Access private member outside of a class using two way #
#1. Using instance method (self):-
class Employee :
    def __init__(self,name,project,salary):
        self.name=name          
        self.project=project      
        self.__salary=salary        #private
    def show (self) :
       print(self.name,self.project,self.__salary)
       
emp=Employee("Rutuja","Django project",20000)
emp.show()

#2. Name mangeling :-
class Employee :
    def __init__(self,name,project,salary):
        self.name=name          
        self.project=project      
        self.__salary=salary        #private
       
emp=Employee("Gauri","Django project",20000)
print (emp._Employee__salary)
