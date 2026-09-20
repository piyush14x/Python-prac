#WAP to input 2 int numbers, a and b.
#Print True if a is greater than or equal to b. If not print False.


'''a = int(input("enter first :"))
b = int(input("enetr second number :"))

print(a >= b)''' #    a is greater than b, so it will show true
                 #    a is not greater than b, it will show false


# -----------------------
# WAP to input side of a square & print its area.
# -----------------------
'''side = float(input ("enter square side : "))
print("area =", side * side)'''

"""str1 = "apna"
str2 = "college"
final_str = str1+str2
print(final_str)"""

#to know the length of string we use len() function
from typing import final


'''str1 = "apna"
len1 = len (str1)
print (len1)

str2 = "college"
len2 = len(str2)
print (len2)
final_str = str1+str2
print("final_str =", len(final_str))
print(len(final_str))'''

# escape sequence characters is use for next line (\n and \t for tab space)  
'''str1 = "This is a string. \nwe are creating it in python."
print(str1)'''


#-------------------
#-------------------
# Slicing of string 
#-------------------
#-------------------

'''str = "piyush saini"
print(str[0:6])''' #p i y u s h   s a i n i
                   #0 1 2 3 4 5 6 7 8 9 10 11 
'''print(str[7:12])
print(str[7:len(str)])'''


'''str = "piyush saini"
             #p i y u s h   s a i n i
             #0 1 2 3 4 5 6 7 8 9 10 11 

print(str[:12])
print(str[7:])'''


'''str = "piyush saini"
print(str[::2])'''   #every second word will be printed

'''str = "manifestation become future"
print(str.endswith("future"))''' #True

light = "yellow"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("watch")




