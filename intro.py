# data types
"""
1.float
2.bulin...yes and no...
3.integer...whole numbers...
4.string...
"""
# learning variables
x = 3
y = "Betty"
print(x)
print(y)

#
# casting

# casing
# camel case
studentNameKenya = "Ken"

# snake case
student_name_kenya = "Ken"

print(student_name_kenya)
# case sensitive
X = 2
x = 2

A = "Mary"
a = "Mary"
"""
# variables must start with either a letter or an underscore

# Assigning Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
# Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the
# values into variables. This is called unpacking.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)
# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
"""
# Variables that are created outside a function (as in all the examples above) are known as global variables.

"""OPERATORS
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

"""
"""
Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:
Operator 	Name 	Example 	Try it
+ 	Addition 	x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	x / y 	
% 	Modulus 	x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division 	x // y
"""
"""Python Assignment Operators

Assignment operators are used to assign values to variables:
Operator 	Example 	Same As 	Try it
= 	         x = 5 	     x = 5 	
+= 	         x += 3 	 x = x + 3 	
-= 	         x -= 3      x = x - 3 	
*= 	         x *= 3 	 x = x * 3 	
/= 	         x /= 3 	 x = x / 3 	
%=         	 x %= 3 	x = x % 3 	
//= 	     x //= 3 	x = x // 3 	
**= 	     x **= 3 	x = x ** 3 	
&= 	         x &= 3 	x = x & 3 	
|= 	         x |= 3 	x = x | 3 	
^= 	         x ^= 3 	x = x ^ 3 	
>>= 	     x >>= 3 	x = x >> 3 	
<<= 	    x <<= 3 	x = x << 3
"""

x = 5
x += 3  # this is like saying x=x+3
x = x
print("my answer is", x)

# multiplication
x = 3
x *= 4  # this is like saying Xx4
print(x)
# values can only be applied to variables not vice versa, or it gives a syntax error 'e.g'
"""
y=5
5+=y
"""
y = 2
y %= 5
print("My answer is", y)
"""
Python Comparison Operators

Comparison operators are used to compare two values:
Operator 	Name 	Example 	Try it
== 	Equal 	x == y 	
!= 	Not equal 	x != y 	
> 	Greater than 	x > y 	
< 	Less than 	x < y 	
>= 	Greater than or equal to 	x >= y 	
<= 	Less than or equal to 	x <= y
"""

# equal to
x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3
y = 2
y = 60
print(y == 60)

# not equal to
p = 5
q = 3
print(p != q)
"""
Python Logical Operators

Logical operators are used to combine conditional statements:

Operator 	Description 	Example 	Try it
and  	    Returns True if both statements are true 	x < 5 and  x < 10 	
or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
"""
# or
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
# not
x = 5

print(not (3 < x < 10))

# returns False because not is used to reverse the result
# and
x = 5

print(3 < x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

# CONDITIONAL STATEMENTS
age = 12
# The if statement executes when the condition is only true
if age >= 18:
    print("You are an adult")
# the elif statement
if age >= 18:
    print("adult")
elif age <= 18:
    print("child")

    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

        # using the and statement
president_age = 12
nationality = "USA"

if president_age >= 35 and nationality == "Kenyan":
    print("you are as successful candidate")
else:
    print("you cannot be president ")

# using the or statement
nationality = "Malawi"
if nationality == "Kenya" or nationality == "Uganda" or nationality == "Tanzania":
    print("you are qualified to play cecafa")
else:
    print("you do not qualify to play cecafa")

school = "Harvard"
if school == "Harvard" or "Yale" or "Brown" or "Dartmouth" or "Princeton" or "UPenn" or "Cornell" or "Columbia" or "Wharton":
    print("You are in an Ivy League University")
else:
    print("You are not in an Ivy League University")

# how to know if a number is odd or even
x = 15
x *= 5
print(x)

x = 3
if (x % 2) == 0:
    print("x is even")
else:
    print("x is odd")

# casting

first_name = "Claudia"
last_name = "Wanjiru"
full_name = first_name + " " + last_name
print(full_name)

# integer to string
name = "Mary"
number = 60
jersey = name + " " + str(number)
print(jersey)

# string to integer
list = "20000"
lit = 30670
total = int(list) + lit
print(total)
print(list)

bucket = 20.0
book = "50.0"
total = float(book) + bucket
result = str(total) + " " + "shillings"
print(result)

# looping
# while loop
i=0
while i<=100:
    i+= 12
    print("value is",i)
"""
name=input("Enter your name: ")
while name=="":
    print("You did not enter your name")
    name=input("Enter your name: ")
print(f"Hello {name}")
"""
"""
name=input("enter your name")
nationality=input("enter your nationality ")
kenyan =0
other=0
while nationality=="Kenyan" or "kenyan"or kenyan>=0:
    print(number)
    number+=1
    name=input("enter your name")
    nationality=input("enter your nationality")
else:
    print("welcome")
"""
"""
nationality=input("nationality required")
nationality="Kenyan"
allowed=1
disallowed=1
while nationality!="Kenyan" or allowed!=1 or disallowed==1:
    print("rejected")
    disallowed+=1

"""

"""
visitors=int(input("enter number of visitors"))
kenyan_no=0
ugandan_no=0
total=0
while total<=visitors:
    nationality=input("nationality required")
    if nationality=="Kenyan":
        kenyan_no+=1
        total+=1
    else:
        ugandan_no+=1
        total+=1
print("the number of visitors is",total)
print("the number of kenyans is",kenyan_no)
print("the number of ugandans is",ugandan_no)
"""
"""
fruits={"apple,bananas,mangoes"}
print(fruits)


fruit=("apple","mangoes","tomatoes")
size=("small","medium","large")
for x in fruit:
    for y in size:
        for i in range(3):
         print(x,y)
"""
""" 
student_names=[input("enter student name"),input("enter second student name"),input("enter third student name")]
while student_names!=" ":
    print(student_names)
    student_names+=1
student_names = [input("enter student name"), input("enter second student name"), input("enter third student name")]

"""
"""
def myfunction():
    print("hello world")
myfunction()
"""
"""
item=input("enter item;")
while item=="":
    if item!="":
     print(item)
     item=input("enter item;")
    item+=1
else:
 print("done")
 """
"""
fruits ("apple,","banana")
print(fruits)
fruits==list(fruits)
fruits[1].append("mango")
fruits
"""
#functions
#creating a function
def addition(x,y):
    return x+y
#calling a function
print(addition(4,4))

#function 2
def printhellofive():
    for x in range(5):
        print("Hello")
print(printhellofive())

import calc_modules
a=200
b=300
print(calc_modules.add(a,b))
x=780
y=450
print(calc_modules.multiply(x, y))
