#printing the value of a variable
age = 21
print(age)
#str() function is used to convert the integer value of age to a string so that it can be concatenated with other strings in the print statement.
print("My age is " + str(age) + " years old.")
#, can also be used to concatenate strings and variables in the print statement without the need for type conversion.
print("you are", age, "years old.")
#f-string is used to format the string and include the value of age in the output. `` -> ${} equivalent in other programming languages.
print(f"You are {age} years old.") 
print("-----------------------------------")


#? Integer data type
#Integer data type is used to store whole numbers without any decimal points.

age = 21
players = 2
quantity = 10

print("Age:", age)
print("Players:", players)
print("Quantity:", quantity) 
print("-----------------------------------")

#?Float data type
#Float data type is used to store numbers with decimal points.
gpa = 3.5
distance = 10.5
price = 99.99

print("GPA:", gpa)
print("Distance:", distance)
print("Price:", price)
print("-----------------------------------")

#?String data type
#String data type is used to store text or characters. Strings are enclosed in single quotes ('') or double quotes (").
name = "John"
food = 'Pizza'
email = "bro@example.com"

print("Name:", name)
print("Food:", food)
print("Email:", email)
print("-----------------------------------")

#?Boolean data type
#Boolean data type is used to store True or False values. It is often used in conditional statements and logical operations.
is_student = True
is_adult = False

print("Is student:", is_student)
print("Is adult:", is_adult)
print("-----------------------------------")

#Multiple variable assignment
x, y, z = 10, 20, 30
print("x:", x)
print("y:", y)
print("z:", z)
print("-----------------------------------")

#Nonetype data type
#Nonetype data type is used to represent the absence of a value or a null value. It is often used to indicate that a variable has no value assigned to it.
result = None
print("Result:", result)
print("-----------------------------------")
#String slicing
#String slicing is used to extract a portion of a string by specifying the start and end indices
text = "Hello, World!"
print("Original text:", text)
print("Sliced text:", text[0:5])
print("Sliced text:", text[0::2]) #slicing with step

