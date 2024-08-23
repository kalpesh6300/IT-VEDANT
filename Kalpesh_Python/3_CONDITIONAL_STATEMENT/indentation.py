'''
num = int(input("Enter number :"))
if num>0 :
    print("Number is Positive")    #within if block / scope of if block
else:
    print("Number is Negative")

print ("Hello")  # Outside of if block
'''
 # Write a program in python to show whether a given number is divisible by 3 and 9.

num = int(input("Enter number :"))
if num%3==0 and num%9==0 :
     print("Number is divisible by 3 and 9")
else :
     print("Number is not divisible by 3 and 9 :")
