#python is a general purpose high level programmimg language.

'''it can be used for:
   console app
   desktop application
   web application
   mobile app
   machine learning
   IOT application'''

#It is very simple and straight forward syntax.

#Python is case sensitive.

#It is an object oriented language.

#Dynamically typed.

#Indendation is used in place of curly braces.

#Use variable without declaration.

#Interpreted language.

#single comment- use #

#multiple comment- use'''  '''or """  """






                                                    #TOPICS
#Print Function-

#print("Hello world")

#or

#print('Hello world')




















#Python as a calculator-

#print(".............CALCULATOR...............")
print("Sum of two number 2+3 is")
print(2+3)
print("Subtraction of two number 2-3 is")
print(2-3)
print("Multiplication  of two number 2*3 is")
print(2*3)
print("Float Division of two number 4/2 is")
print(4/2)
print("Intger Division of two number 4//2 is")
print(4//2)                                     #for integer division use //
print("Modulus of number 5%2 is")
print(5%2)
print("Power of number 2**3 is")
print(2**3)                                     #for power use **











#Variable declaration in python-

"""num=2             
print(num)       #int
print(type(num))

num=2.5
print(num)       #float
print(type(num))

num="Kartik"
print(num)       #string-Any thing written in inverted commas is considered as string.
print(type(num))
""" 
 











#String-

#string concatenation-
"""first_name="Kartik "                           #adding space
last_name="Garg"
full_name=first_name+last_name
print(full_name)

print("one more way for string concatenation")

first_name="Kartik"
last_name="Garg"
full_name=first_name+" "+last_name               #adding space using inverted quotation
print(full_name)"""














#User Inputs-

#by using input() function-It always take only string type input

"""name=input("Enter your name\n")     #\n is use for next line
print("Entered name is "+name)"""     #use + sign because here two string is concatenate


#by using int() function-It always take only integer type input

"""num1=int(input("Enter the number\n"))
num2=float(input("Enter the number\n"))
print("Entered number is ",num1)
print("Entered number is",num2)    """        #use comma whenever you use the int type value













#two or more input in one line 

"""name,age=input("Enter your name\n"),input("Enter your age\n")
print(name)
print(age)"""

#two or more input in one line using split() function
#Note:split function is only for string not for int type value

"""name,age=input("Enter your name and age").split( )    #seperated by space
print(name)
print(age)    """                              #you can also use seperated by comma or anything else
                                            #.split(",") seperated by comma














#String Indexing-If we want to print particular letter from a word then we use string indexing

"""name="Microsoft"     #FORWARD indexing is starting from 0(Zero)
                         #M---0
print(name)              #i---1
print(name[0])           #c---2
print(name[5])           #r---3       #FORWARD
print(name[-9])          #o---4
print(name[-4]) """      #s---5
                         #o---6
                         #f---7
                         #t---8

                        #REVERSE indexing is starting from -1
                         #M---  -9
                         #i---  -8
                         #c---  -7
                         #r---  -6       #BACKWARD or REVERSE
                         #o---  -5
                         #s---  -4
                         #o---  -3
                         #f---  -2
                         #t---  -1





"""String Slicing/Selecting sub sequences--String slicing means if we want to print a word
which is generating from another word

[:] in this ':' is known Range operator.
"""

"""name="microsoft"                 #now,if we want to print micro from microsoft.then,
print(name[0:5])"""                 #index starts=0
                                    #number of times slicing=5
                                    #Note:space is count in string





















#Step Argument--If we want to print some letters from a word then we use step argument.

"""                                #index starts=0
name="microsoft"                   #number of times slicing=9
print(name[0:9:2])                 #step argument=2 gap

"""           
                                  
                                  




















"""Some Common Strings methods--
len() function
lower() function
upper() function
title() function
count() function"""


"""
name="KaRtIk GaRg"
#for finding length of the string,we use len() function
print(len(name))

#for converting all the letters of the string in lower case letter,we use lower() method
print(name.lower())

#for converting all the letters of the string in upper case letter,we use upper() method
print(name.upper())

#for converting initial letter of your string in capital letter,we use title() method
print(name.title())

#for counting the occurance of a particular letter in your string,we use count() method
print(name.count("R"))

"""












"""#if-else statement----

if statement syntax---

if condition:
    statements
    
else statement syntax---

else:
    statements"""



#Example
"""
num=int(input("Enter the number\n"))
if num//2==0:
    print("Even")
else:
    print("Odd")

"""











"""#if-elseif(elif)-else--------
num=int(input("Enter the number\n"))
if num==0:
    print("Neither negative nor positive")
elif num>0:
    print("Positive")
else:
    print("Negative")"""


"""Note:If there are more than one condition then use AND and OR there..."""















"""LOOPS------------

While loop syntax---

initilizing
while condition:
    increment/decrement"""

#Example 1: print HELLO 10 times

"""i=1
while i<=10:
    print("HELLO")
    i+=1   """                #i=i+1

#Example 2:Sum of first 10 numbers

"""sum=0                                       #sum=0 declared because garbage value
i=1
while i<=10:
    sum+=i
    i=i+1
print("Sum of first 10 number is:"+str(sum))"""   #here sum is int type therefore,we have to change
                                               #to string using str() function...
                                               #similarly,we can use int(),float() functions to change
                                               #the data type.





#for loop------

#for loop with range function---

#Example:1

"""for i in range(10):                        #start=0,no.of times=10,jump or gap=1
    print("harshit "+str(i))
print("..........................")
for i in range(0,10):                      #start=0,no.of times=10,jump or gap=1
    print("harshit "+str(i))
print("..........................")
for i in range(0,10,1):                    #start=0,no.of times=10,jump or gap=1
    print("harshit "+str(i))"""


#Example:2  Sum of num numbers

"""sum=0
num=int(input("Enter the number \n"))
for i in range(1,num+1,1):
    sum+=i
print("sum of the n natural number is: "+str(sum))"""



#for loop with slicing---
#Example:1
"""name="Kartik Garg"
for i in name[0:len(name):1]:                           
    print(i)"""

    #output
#K
#a
#r
#t
#i
#k
# 
#G
#a
#r
#g

#Example:2
"""name="Kartik Garg"
for i in name[0:len(name):1]:                           
    print(i,end="")"""

    #output
    #Kartik Garg
    
    
#Example:3
"""name="Kartik Garg"
for i in name[::-1]:            #for reverse the string               
    print(i,end="")"""

    #output
    #graG kitraK




#break and continue statements-------

#break statement--(exit from the loop)
"""for i in range(1,11):
    if i==5:
        break
    print(i)"""


#continue statement--(jump or continue after)
"""for i in range(1,11):
    if i==5:
        continue
    print(i)"""


                  












"""Functions--------for defining a function in python we use def keyword and then function name

syntax:-
          def function_name:


Functions are of two types:-
1.Pre-defines function
2.User defined function


Types of User defined function:-
1.No Return No Argument
2.No Return With Argument
3.Return Type Without Argument
4.Return Type With Argument    """




"""
#Example:Addition of two numbers using function

#function 1:no return no argument
def addition1():
    num1,num2=int(input("Enter the first number \n")),int(input("Enter the second number \n"))
    num3=num1+num2
    print("Sum of the two digits is: "+str(num3))

addition1()


print("-------------------------------------------------------------------------------------------")


#function 2:no return with argument
def addition2(num1,num2):
    num3=num1+num2
    print("Sum of the number is: "+str(num3))


num1,num2=int(input("Enter the first number \n")),int(input("Enter the second number \n"))
addition2(num1,num2)


print("------------------------------------------------------------------------------------------")


#function 3:return type without argument
def addition3():
    num1,num2=int(input("Enter the first number \n")),int(input("Enter the second number \n"))
    return num1+num2



print("sum of the number is: "+str(addition3()))


print("------------------------------------------------------------------------------------------")

#function 4:return type with argument
def addition4(num1,num2):
    return num1+num2
    


num1,num2=int(input("Enter the first number \n")),int(input("Enter the second number \n"))
num3=addition4(num1,num2)
print("Sum of the number is: "+str(num3))      """
























          





