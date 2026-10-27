#Python uses indentation to indicate a block of code
#For example:
if 5 > 2:
    print("Five is greater than two!")

#Python will give you an error if you skip the indentication
if 5>2:
print("Five is greater than two!")
#we get an erro ^^

#you have to use the same number of spaces in the same block of code, otherwise Python will give you an error
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
#error^^

#In python, a variable is created when you assing a value to it.
# For example:
x = 5
y = "Hello, World!"

#Python has no command for declaring a variable. 
#You can cast a specific data type to a variable.
#For example:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))
print(type(z))

#Python is Case-sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"

#And you can assign the same value to multiple variables in one line
x = y = z = "Orange"

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

#Global variables are variables that are created outside of a function
#For example:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)