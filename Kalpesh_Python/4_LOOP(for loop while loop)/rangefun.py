'''
# Range :
#Range is a function in python is used to generate sequence of numbers.
#Commonly used wih for loop to iterate over sequence.
syntax:
    range(start,stop,step)
start :
    1.This represent start value.
    2. inclusive / Include.
    3. (optional).

stop :
    1. This represents stop value.
    2. Exclusive / Exclude.

step :
    1. This represents step value.
    2. Incremented/Decremented by some value.
    3. Default increment is 1.

#Need of loop :
    A loop is programming construct that allow repeated exceution of block of code.
    It iterates over a sequence of instructions until sepecific condition is met.

1. For loop :
    Repeat the block of statement a fixed number of times.

 2. While loop:
     Exceutes until a condition is True.


for loop :
    Repeat the block of statement a fixed number of times
Syntax :
 1.   for i in range (value) :
        statement/s
        
 2.   for i in sequence :
        statement 1
        statement 2
        statement 3
        .
        .
        .
        statement n

 3.  for i in range (sequence) :
       statement/s
    

1.   for i in range (value) :     (iterating_variable = i )
        statement/s

for i in range(5) :
    print(i)
print("\n")

for i in range(1, 10) :
    print(i)
print("\n")

for i in range(1, 11, 2) :
    print(i)
print("\n")

for i in range(10, 0, -1) : 
    print(i)
print("\n")    

for i in range(11) : 
    print(i, end=" ") ->  #Horizontal karne ke liye use kiya jaata hai (end= " ")
    
 2.   for i in sequence :
        statement 1
 
string_1 = "Hello Python"
for i in string_1 :
    print(i)
print("\n")

string_1 = "Hello Python"
for i in string_1 :
    print(i, end=" ")
print("\n")    

list1=[10, 20, 30, 40, 50]
for i in list1 :
    print(i)
print("\n")

list1=["Hello", 10,  20.5, True]
for i in list1 :
    print(i)
print("\n")

tuple1= (10, 20, 30, 40, 50)
for i in tuple1 :
        print(i)
print("\n")

list1=[10, 20, 30, 40, 50]
for i in range(len(list1)):
    print(list1 [i])
print("\n")

#Write a program in python to show even numbers from given list.
list1=[10,20,33,44,30,60,70]
even_list=[]
odd_list=[]
for i in list1 :
    if i % 2 == 0 :
        even_list.append(i)
    else :
         odd_list.append(i)
print("Even :",even_list)
print("Odd :",odd_list)


#nested for loop

for i in range(1,6):
    print("i",i)
    for j in range(4,8):
        print("j",j)
    print()

#write a program to find square of number from given list

list1=[2,5,7,4,9]
square_list=[]

for i in list1:
    result=i*i
    square_list.append(result)
    print(square_list)

#write a program to find sum of N numbers where N is provided by user.

num=int(input("Enter number:"))
result=0

for i in range(1,num+1):
        result+=i                   #result=result+i
        print(result)


#write a program in python to find factorial of given number ?
        
num=int(input("Enter number:"))
result=1

for i in range(1,num+1):
        result*=i                   #result=result*i
        print(result)
    

#write a program in python to find average of list of numbers.?
#write a program in python to find reverse number?
#find largest number from given list?
#find even number and find square of this even number?
#find occurence of given number?
#find out common number between two list?
#write a python program to show multiplication table?
#write a python program to show prime numbers within given range
#wap to show given number is armstrong number?

# Neasted for loop :

# While Loop :
#While loop is a control flow statement in python used for iterating a block of code repeatedly as long as specified condition is true.

syntax :
Initialization of variable
while (condition) :
         statement/s
         increment/decrement

Q. What is difference between for and while loop ?    

num = 10
while (num>0) :
        print(num)
        num = num -1
print ("hello")        
        
     
#Write a program to show factorial of number  using while loop?
num=int(input("Enter number:"))
i=1
fact = 1
while(i<=num) :
        fact = fact * i
        print (fact)
        i = i+1
print (fact)

#Write a program in python to show some of digits of number?               
num=int(input("Enter number:"))   #123    
sum1=0

while(num>0) :                               #123>0                             #12>0 
        rem = num % 10                    #123%10 -> 3                  #12%10 -> 2
        sum1 = sum1 + rem               #sum1 = 0 + 3 -> 3
        num = num//10
print (sum1)

#Write a program in python to show reverse of number?    
num=int(input("Enter number:"))  #321     
while(num>0) :
        rem = num % 10
        print(rem,end="")
        num = num//10

# Loop ControL Statement :
1. break
       python stops the cureent loop control flow transfered to the following lines of code immediately following the loop.
                         Or
       if there is need to stop working of loop even if loop condition is true we use break keyword.
2.continue
3.pass

#BREAK
num=1
while (num<=10):
        if num==5:
                break
        print(num)
        num=num+1
print("hello")

#CONTINUE
         It skips the current iteration of a loop immediately jump to next iteration.

#Count occurence of letter 'a' in given string
name = input("Enter Name :")  #kalpesh
count = 0
for char in name :
        if char != 'a' :
               continue
        else :
                count = count+1
        print(char, end= " ")


name = input("Enter Name :")  #kalpesh count 'a' only ....
count = 0
for char in name :
        if char != 'a' :
               continue
        else :
                count = count+1
        print(count, end= " ")


for i in range(10) :
        if i==5:
                continue   # (skip the current iterations) ('5' ko nahi lega aapni gang m)
        else:
                print(i)
'''                
# find even numbers given range using continue?
'''
for i in range(10) :
        if i % 2!=0:
                continue   # (skip the current iterations) ('5' ko nahi lega aapni gang m)
        else:
                print(i)
'''
#PASS :
'''
  It is null statement .
  Nothing happened when this statement is occured in given block of code.
 syntax:
 
list1=[10, 20, 30, 40]
for i in list1 :
        pass #(Stop karna )
'''
#Patterns with loops :
'''
Steps:
        1. Decide the number of rows and columns
        2. Decide how many columns in given pattern.
        3. Iterate rows
        4. Iterate Columns. 
        5. Print star or number or character.
        6. Add a new line after each iteration of the outer loop.
           print()
   '''
#To show star pattern vertically
'''
for i in range (1,6) :
        print("*")
'''
#To show star pattern horizontally
'''
for i in range (1,6) :
        print("*", end=" ")
     
############
for i in range(1,6) :  #outer loop        
         for j in range(1,i+1) :   #inner loop
                 print("*", end=" ")
         print()        

#To show square pattern horizontally
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
for i in range(1,6) :  #outer loop        
         for j in range(1,6) :   #inner loop
                 print("*", end=" ")
         print()        

#To show Half pyamid pattern
num = int(input("Enter Number:"))
for i in range (1, num) :
     for j in range (1, i+1) :
        print("*", end=" ")
     print()

# To show inverted pyramid
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*

for i in range(6, 0, -1) :  #outer loop        
         for j in range(1,i+1) :   #inner loop
                 print("*", end=" ")
         print()
#################################
num = int(input("Enter Number:"))
for i in range (1, num) :
     for j in range (1, i+1) :
        print(j, end=" ")
     print()
# Output
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
################################
num = int(input("Enter Number:"))
for i in range (1, num) :
     for j in range (1, i+1) :
        print(i, end=" ")
     print()     
# Output
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
################################

# To show Mix pyramid :
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
for i in range (1, 6) :
     for j in range (1, i+1) :
        print("*", end=" ")
     print()  
for i in range(6, 0, -1) :         
     for j in range(1,i+1) :   
         print("*", end=" ")
     print()
 
##############################
#To Show Output
Enter Number:6
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9
  
num = int(input("Enter Number:"))
for i in range (1, num) :
     for j in range (i) :
        print(i+j, end=" ")
     print()
 ############################

# To Show Character Half Pyramid:
num = int(input("Enter Number:"))
ascii_value =65
for i in range (1, num) :
     for j in range (i) :
        alpha = chr(ascii_value)  
        print(alpha, end=" ")
     ascii_value =ascii_value + 1   
     print()

num = int(input("Enter Number:"))
k=2*num-2
for i in range (0, num) :
     for j in range (0, k) :
        print(end=" ")
     k=k-1   
     for j in range (0, i+1) :
          print("*", end=" ")
     print(" ")     

     # Output :
          *  
         * *  
        * * *  
       * * * *  
      * * * * *  
     * * * * * *
 '''
num = int(input("Enter Number:"))
k=2*num-2
for i in range (num,-1,-1) :
     for j in range (k,0,-1) :
        print(end=" ")
     k=k+1   
     for j in range (0, i+1) :
          print("*", end=" ")
     print(" ")     

          
