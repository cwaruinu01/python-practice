print("My name is Claudia Wanjiru")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

for x in "banana":
    print(x)

print("We are the so called \"vikings\" from the North")

#lists


#lists use square brackets
fruits=["bananas","cherries","papayas","mangoes"]
print(fruits)

#properties of lists:

#ordered

#indexed
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#changeable
fruits=["apple","orange","mango"]
fruits[1]="cherries"
print(fruits)

#Allow duplicates values
fruits=["mango","apple","apple","orange","mango"]
print(fruits)

#List Length
#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#insert lists
#To insert a list item at a specified index, use the insert() method.
fruits=["mango","cherries","apples","oranges"]
fruits.insert(2,"watermelon")
print(fruits)

#Append Items
#To add an item to the end of the list, use the append() method:
fruits=["papayas","mangoes","apples"]
fruits.append("oranges")
print(fruits)

#Extend List
#To append elements from another list to the current list, use the extend() method.
fruits1=["apple","banana"]
fruits2=["orange","mango"]
fruits1.extend(fruits2)
print(fruits1)

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#removing a specific item
fruits=["papayas","mangoes","apples"]
fruits.remove("papayas")
print(fruits)

#remove specific index
fruits=["papayas","mangoes","apples"]
fruits.pop(1)
print(fruits)

#clear the list
fruits=["papayas","mangoes","apples"]
fruits.clear()
print(fruits)

#loop through a list
fruits=["papayas","mangoes","apples"]
for x in fruits:
    print(x)

#looping through the index number
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
fruit=["papayas","mangoes","apples"]
for i in range(len(fruits)):
 print(fruit[i])

#Using a While Loop
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
fruits=["papayas","mangoes","apples"]
i=0
while i<len(fruits):
 print(fruits)
 i=i+1

#looping using list comprehension
#List Comprehension offers the shortest syntax for looping through lists:
fruits=["papayas","mangoes","apples"]
[print (x) for x in fruits]

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits=["papayas","mangoes","apples","tomatoes","cherries","kiwis"]
a_letter_fruit=[]
for x in fruits:
    if "a" in x:
        a_letter_fruit.append(x)

print(a_letter_fruit)

#With list comprehension you can do all that with only one line of code:
fruits=["papayas","mangoes","apples","apricots","kiwi"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

#Condition
#The condition is like a filter that only accepts the items that valuate to True.

#Example
#Only accept items that are not "apple":
fruits=["papayas","mangoes","apples"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)



fruits=["papayas","mangoes","apples"]
if "apples" in fruits:
 print("yes")


#unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



#functions
#A function is a block of code which only runs when it is called.

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:


#Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""


