#Repetation of operators
'''print("hi * 3")'''

#Length of string
'''text = "python"
print(len(text))'''

'''name = input("piyush")
print("name")'''

'''text = "python"
print(text,())'''

#Addition of two numbers
'''a = int(input("enter first number"))
b = int(input("enter second number"))
sum = a + b 
print("sum=", sum)'''

#STRING Memberahip
'''text = "python"
print("py" in text)'''

#converting to uppercase
'''text = "piyush"
print(text.upper())'''

#coverting to lowercase
'''text = "PIYUSH"
print("PIYUSH".lower())'''

#taking integer input
'''age = int(input("enter age :"))
print("age =", age)'''

#taking float input 
'''salary = float(input("enter salary : "))
print("salary =", salary)'''

#Printing multiples values
'''name = "piyush"
age = 20 
print(name, age)'''

#Formatted printing
'''name = "Piyush"
age = 20 
print (f"name : {name}, \n age : {age}")'''

#Area of a circle 
'''pi = 3.14159
radius = float(input("enter raduius :"))
area = pi* radius* radius
print("area = ", area)'''


'''x = 10 
x+= 5
print(x)
x-=5
print(x)
x*=2
print(x)
x/=2
print(x)
x%=3
print(x)
x//=2
print(x)
x**=2
print(x)'''


#OOP program
#------------

'''class student:
    def __init__(self,name,age):
        self.name = name
        self.age= age 

obj = student("rahul", 20)

print("name:",obj.name)
print("age:",obj.age)
'''


#WAP to check entered number is even or odd;
'''n = int(input("enter number"))
if n%2 == 0:
    print("even")
else: 
    print("odd")'''

#Single Inheritance
'''class animal:
    def sound(self):
        print("animal sound")

class dog(animal):
    def bark(self):
        print("dog bark")

obj = dog()

obj.sound()
obj.bark()'''

#multilever inheritance
'''class A:
    def showA(self):
        print("class A")

class B(A):
    def showB(self):
        print("class B")

class C(B):
    def showC(self):
        print("class C")

obj = C()

obj.showA()
obj.showB()
obj.showC()'''


#class → Class
# = → Variable
# def → Method/Function
# ClassName() → Object ban raha hai
# self → Current object
# () ke andar function define karte waqt → Parameters
# () ke andar function call karte waqt → Arguments


# ==============================
# 1. CLASS
# ==============================

'''class Father:                           # Father = Class (Blueprint)

    business = "Electronics Shop"       # business = Class Variable

    def __init__(self):                 # __init__ = Constructor
                                        # self = Current Object
        self.age = 50                   # age = Instance Variable / Attribute

    def showBusiness(self):             # showBusiness = Method
        print(self.business)            # self.business = Attribute


class Mother:                           # Mother = Class

    hobby = "Cooking"                   # hobby = Class Variable

    def showHobby(self):                # showHobby = Method
        print(self.hobby)'''


# ==============================
# 2. MULTIPLE INHERITANCE
# ==============================

'''class Child(Father, Mother):            # Child = Class
                                        # (Father, Mother) = Multiple Inheritance

    def __init__(self, name):           # Constructor
                                        # self, name = Parameters

        Father.__init__(self)           # Parent Constructor Call

        self.name = name                # Instance Variable / Attribute

    def showName(self):                 # Method
        print(self.name)

    def add(self, a, b):                # a, b = Parameters
        return a + b'''


# ==============================
# 3. OBJECT
# ==============================

'''obj = Child("Piyush")'''                   # obj = Object
                                        # Child() = Object Creation (Instantiation)
                                        # "Piyush" = Argument


# ==============================
# 4. METHOD CALL
# ==============================

'''obj.showName()                          # Method Call

obj.showBusiness()                      # Inherited Method

obj.showHobby()                         # Inherited Method

print(obj.add(10, 20))'''                  # 10, 20 = Arguments


# ==============================
# 5. ATTRIBUTE ACCESS
# ==============================

'''print(obj.business)                     # Class Attribute

print(obj.hobby)                        # Class Attribute

print(obj.name)                         # Instance Attribute

print(obj.age)'''                          # Inherited Instance Attribute# ==============================


#===============================
# 1. CLASS
# ==============================

'''class Father:                           # Father = Class (Blueprint)

    business = "Electronics Shop"       # business = Class Variable

    def __init__(self):                 # __init__ = Constructor
                                        # self = Current Object
        self.age = 50                   # age = Instance Variable / Attribute

    def showBusiness(self):             # showBusiness = Method
        print(self.business)            # self.business = Attribute


class Mother:                           # Mother = Class

    hobby = "Cooking"                   # hobby = Class Variable

    def showHobby(self):                # showHobby = Method
        print(self.hobby)'''


# ==============================
# 2. MULTIPLE INHERITANCE
# ==============================

'''class Child(Father, Mother):            # Child = Class
                                        # (Father, Mother) = Multiple Inheritance

    def __init__(self, name):           # Constructor
                                        # self, name = Parameters

        Father.__init__(self)           # Parent Constructor Call

        self.name = name                # Instance Variable / Attribute

    def showName(self):                 # Method
        print(self.name)

    def add(self, a, b):                # a, b = Parameters
        return a + b'''


# ==============================
# 3. OBJECT
# ==============================

'''obj = Child("Piyush")'''                   # obj = Object
                                        # Child() = Object Creation (Instantiation)
                                        # "Piyush" = Argument


# ==============================
# 4. METHOD CALL
# ==============================

'''obj.showName()                          # Method Call

obj.showBusiness()                      # Inherited Method

obj.showHobby()                         # Inherited Method

print(obj.add(10, 20))'''                  # 10, 20 = Arguments


# ==============================
# 5. ATTRIBUTE ACCESS
# ==============================

'''print(obj.business)'''                     # Class Attribute

'''print(obj.hobby)'''                        # Class Attribute

'''print(obj.name)'''                         # Instance Attribute

'''print(obj.age)'''                          # Inherited Instance Attributeage 


#====================
#IF-Else elif concept
#====================


'''age = int(input("enter the number: "))
if age>0:
    if age>18 and age<75:
        print("you can vote")
    elif age>75:
        print("time aa gaya hai")
    else: 
        print("not eligible")
else:
    print("have you gone mad, why are you passing nagative number'''

#===================
#nested if statement
#===================
'''age = 20 
citizen = True

if age >=18:
    if citizen:
        print("eligible for voting")'''

#========
#Loops in python
#========

#for loop
'''for i in range(1,6):
    print(i)'''

#while loop
'''i = 1

while i<5:
    print(i)
    i+=1'''

#use of for loop with break keywords
'''for i in range(2,21,2):
    print(i)'''

#using "for" Loop for printing multiple time
'''for i in range (50):
    print("piyush")'''


#=====================
#if_elif_else statement
#======================

'''marks = 80
if marks >=90:
    print("grade A+")
elif marks >=80:
    print("grade A")
elif marks >=70:
    print("grade B")
elif marks >=60:
    print("grade C")
else:
    print("fail")'''


'''age = 66
citizen = True

if age >= 18:
    if citizen:
        print("Eligible for voting")'''


'''username = input("enter username: ")
password = input("enter password: ")

if username == "piyush":
    if password == "1234":
        print("login successfull")
    else:
        print("wrong pasword")
else:
    print("invailed username")'''



'''for i in range(1, 5):  # 1,2,3
    print(" " * (5 - i) + "*" * (2 * i - 1))'''


'''for i in range(8):
    if i == 0 or i == 3:
        print("*****")
    elif i<3:
        print("*   *")
    else:
        print("*")


st = {1,2,3,4,5,6,6}
sum = 0
for i in st :
    sum = sum+i
    print(sum)

for i in range(8):
    if i == 0 or i == 3:
        print("*****")
    elif i<3:
        print("*   *")
    else:
        print("*")

for i in range(8):
    if i == 0 or i == 7:
        print("*****")
    else:
        print("  *  ")''' 


'''def total_marks(student_name, *marks):
    print("student :", student_name)
    print("marks :", marks)
    marks_len=len(marks)
    total = 0

    for marks in marks:
        total +=marks
    per = total/500*100
    average=total/marks_len 

    print("total marks :", total)
    print("Percentage =", round(per,2), "%")
    print("average marks", average)
total_marks("Rahul", 80, 75, 90, 85)
print()
total_marks ("Priya", 95, 88, 91)
print()'''

#===============
#Lambda Function
#===============

'''average = lambda a, b, c :(a+b+c)/3
print(average(10,20,30))'''

'''check = lambda a,b,c : "Largest number is : " +str(max(a,b,c))
print(check(20,40,70))'''

'''check = lambda a,b,c :"Largest number is : " +str(max(a,b,c))
print(check(20,40,70))'''

'''students = [
    ("Amit", 75),
    ("Riya", 92),
    ("Karan", 81)
]
sorted_students = sorted(
    students,
    key = lambda x: x[1]
)
print(sorted_students)'''

# Question: filter emoloyees earning above ₹50000

'''lst = [12000, 50000, 30000, 55000, 52000]
result = list(filter(lambda a: a>= 50000, lst ))
print(result)'''


'''with open("hello.txt", "w") as d:
    d.write("i have to go for a very urgent work" \
    ", so i will come tomarrow")

with open("hello.txt", "r") as f:
    print(f.read(6))
    f.seek(17)
    print(f.read(18))'''

'''with open("student txt", "a")as file:
    file.write("\nNIELIT A-Level")'''


'''from calculator import introduction as i
i.hello()
i.piyush()'''


import math
print(math.sqrt(100))

from math import sqrt
print(sqrt(64))

















