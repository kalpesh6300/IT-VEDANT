'''
String :
    Character enclosed within single, double or tripple quotes is called string.
    Each Character is encoded as ASCII or UNICODE character.
    String is represented by (str) class.

Project = "Python project"
print(type(Project))

#Define String in python
name = "Kalpesh"
print(name)

msg = 'Rutuja'
print(msg)

msg = """Hello
             Rutuja """
print(msg)

msg = """Jay Shree Ram """
print(msg)


# String indexing :   # Index Value = 0 1 2 3 4 5 6 
name= "Kalpesh"                         #   k a  l  p e s h   
print(name[0])
print(name[2])
print(name[-2])
print(name[:])  # Kalpesh
print(name[2 :]) # lpesh
print(name[0 : 2]) #ka
print(name[0 : -1]) #kalpes
print(name[1 : -1]) #alpes
print(name[: : -1]) #hseplaK
print(name[-3 : -1])


# string reassigning :
#strings are immutable.
project = "Python Project"
project = "Cython Project"
print(project)


#Deleting string :  # (can delete single item from string)
project = "Python Project"
del project
print(project)


#string Formatting :
#Escape sequence character \n  \t  \v
project = "Python Project Its works good \n Hello Everyone "
print(project)

project = "Python Project Its works good \t Hello Everyone "
print(project)

project = "Python Project Its works good \v Hello Everyone "
print(project)

#Format method :
#1 . Using Curly Braces
print ("{} and {} are two modules from PESD9".format("core web design", "SQL"))

#2. Positional Argument :                                                          #0                    #1
print ("{1} and {0} are two modules from PESD9".format("core web design", "SQL"))

#3. Keyword Argument :
print ("{x} and {y} are two modules from PESD9".format(x="core web design", y="SQL"))


#String Function :
#1. Capitalize ()  #First letter capital
project ="python project"
print(project.capitalize())

#2. upper ()
project ="python project"
print(project.upper())

#3. lower ()
project ="python project"
print(project.lower())

#4. casefold()
project ="python Project"
print(project.casefold())

#5. swapcase ()     #lower to upper  #upper to lower
project ="Python Project"
print(project.swapcase())

#6. count()
project ="python project python programming"
print(project.count())

#count(string, begin, end)
print(project.count("python", 0,30))

#isalnum()
project = "python1234" #true
print(project.isalnum())

#isalpha()
project = "python1234"
print(project.isalpha())  #false

project = "pythonprogram"
print(project.isalpha()) #true

#join()
list1 = ["Hello", "Python", "Programming"]
print(" ". join(list1))

print(":". join(list1))

#istitle  # sab ke first letter capital honge tho hi "True"
project= "Python Programming"
print(project.istitle())
'''
#len()
project= "Python Programming" # space ko bhi count karega
print(len(project))

#lstrip()
project= "         Python Programming"  #space rahega tho bhi apply karega
print(project . lstrip())

#replace()
project= "Python Programming"
print(project.replace("Python", "Cython"))

#title()
project= "python programming"
print(project . title())

#split()
project= "python programming"
print(project . split("  "))
