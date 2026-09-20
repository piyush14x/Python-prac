from xxlimited import new


"""print("===== Arithmetic Operators =====")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)"""



#print("===== Calculator =====")

'''num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator!")'''   # Inherited Instance Attribute

#============================
    # String Functions
#============================

'''str = "I am a coder."'''

'''str.endswith("er.")'''      # returns True if string ends with substring

'''str.capitalize()'''         # capitalizes 1st character

'''str.replace(old, new)'''    # replaces all occurrences of old with new

'''str.find(word)'''           # returns 1st index of 1st occurrence

'''str.count("am")'''          # counts the occurrence of substring

'''str = "I am a coder."'''

'''print(str.endswith("er."))'''      # True
'''print(str.capitalize())'''         # I am a coder.
'''print(str.replace("coder", "developer"))'''  # I am a developer.
'''print(str.find("coder"))'''        # means first word of coder is at index 7
'''print(str.count("am"))'''          # mean how much time this word is present in the string, here it is 1 time.   


'''p = float(input("principal: "))
r = float(input("rate: "))
t = float(input("time: "))

si = (p * r * t)/100

print("simple interser =" ,si)'''




'''username = input("enter username: ")
password = input("enter password: ")

if username == "piyush":
    if password == "1234":
        print("login successfull")
    else:
        print("wrong pasword")
else:
    print("invailed username")
for i in range(8):
    if i == 0 or i == 3:
        print("*****")
    elif i<3:
        print("*   *")
    else:
        print("*")'''


'''st = {1,2,3,4,5,6,6}
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


'''class Father:                           # Father = Class (Blueprint)

    business = "Electronics Shop"       # business = Class Variable

    def __init__(self):                 # __init__ = Constructor
                                        # self = Current Object
        self.age = 50                   # age = Instance Variable / Attribute

    def showBusiness(self):             # showBusiness = Method
        print(self.business)'''            # self.business = Attribute


def total_marks(student_name, *marks, max_per_subject=100):
    """
    Calculate and display total, percentage, and average marks for a student.
    Args:
        student_name (str): Name of the student.
        *marks (int/float): Variable number of subject marks.
        max_per_subject (int): Maximum marks per subject (default 100).
    """
    if not marks:
        print(f"No marks provided for {student_name}.")
        return
    total = sum(marks)
    num_subjects = len(marks)
    max_total = num_subjects * max_per_subject
    percentage = (total / max_total) * 100
    average = total / num_subjects
    print(f"Student      : {student_name}")
    print(f"Marks        : {marks}")
    print(f"Total Marks  : {total}/{max_total}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Average      : {average:.2f}")
    print("-" * 30)


if __name__ == "__main__":
    total_marks("Rahul", 80, 75, 90, 85)
    total_marks("Priya", 95, 88, 91)
         