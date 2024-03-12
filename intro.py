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

# variables must start with either a letter or an underscore

# Assigning Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the
# values into variables. This is called unpacking.

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
y = 2.0
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

if president_age >= 18 and nationality == "Kenyan":
    print("you are as successful candidate")
else:
    print("you cannot be president ")

# using the or statement
nationality = "Malawi"
if nationality == "Kenya" or nationality == "Uganda" or nationality == "Tanzania":
    print("you are qualified to play cecafa")
else:
    print("you do not qualify to play cecafa")
