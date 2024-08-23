#Need of conditional statement :
#Comparision Opeators :
#if control statement :
          #if control flow statement is used to execute block of code based on certain condition.
          #It evaluates an expression that results in a boolean value (True or False).

#if statement
#if - else statement
#if elif else statement
#nested if statement
#Indantation : is a mandamental aspect of python syntax use to define the structure and hierachy of code block.
#unlike many other programming languages that uses braches() or keywords like begin end to denote code block python uses indentation.

#if statement
'''
        if (condition) :
            #if statement body (statements) if condition is true
'''
#num = int(input("Enter Number :"))
#if num > 0 :
   # print ("Number is Positive Number!!!!")
'''
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

#if - else statement :
num = int(input("Enter Number :"))
if num > 0 :
    print ("Number is Positive Number!!!!")
else :
    print("Number is Negative Number!!!!")
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
'''
email = "rutuja@gmail.com"
email_id = input ("Enter your email id : ")
if email_id == email:
    print("Correct email id")
else :
    print("Wrong email id")
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''  
per = float (input("Enter percentage :"))
if per>35 :
    print("pass")
else :
    print("fail")
 '''   

# if - elif - else statement
#core_web = int(input("Enter marks  for core_web :"))
#sql = int(input("Enter marks for sql :"))
#python = int(input("Enter marks for python :"))
#django = int(input("Enter marks django :"))
#adv_web = int(input("Enter marks adv_web :"))

#total = core_web+sql+python+django+adv_web
#per = (total/500) * 100
#print(per)
'''
if per >= 75 and per <=100 :
    print("O Grade")
elif per >= 60 :
    print("A Grade")
elif per >= 55 :
    print("B Grade")
elif per >= 35 :
    print("C Grade")    
else :
    print ("Tuzi layki nay bhava!!!")
 '''
'''
#Nested if :
if condition :
    if condition :
        statements
    else :
        statements
else :
     statements

# Write a Program to Find Greatest Among three numbers :
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))

if num1 > num2 :
   if num1 > num3 :
        print ("Num1 is greater than all Numbers")
   else :
        print ("Num3 is greater than all Numbers")
elif num2>num3 :
    print("Num2 is greater than all Numbers")
else :
    print("Num3 is greater than all Numbers")


# Write a program to find whether given number is even or odd.
# take number from user.
num = int(input("Enter your Number :"))
if num % 2==0 :
    print (num,"is Even")
else :
    print (num, "is Odd")

# Write a program to find whether given number is dividible by 7 or not.

num = int(input("Enter your Number :"))

if num / 7 == 0 :
    print (num,"is divisible by 7")
else :
    print (num, "is  not divisible by 7")

# Write a program to check whether person is eligible for voting or not
num = int(input("Enter your Number :"))
if num >18 :
    print (num,"is voting")
else :
    print (num, "is  not voting")
'''
# Company decided to give bonus to employees based on following criteria
'''
time period in company                              Bonus
more than or equal to 10 years                    20%
less than 10 and more than 5 years             10%
less than 5 years                                          4%

num = int(input("Enter your time period in company :"))

if num <=5 :
    print ("4 % bonus")
elif num <= 10 and num > 5 :
    print ("10% bonus")
else :
    print ("20% bonus")
'''
#########################################################










    
