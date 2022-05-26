from __future__ import division
from functools import total_ordering
from itertools import count

# Types of class
a = "Pratik"
b = 24
c = 35.15
d = .5

print(type(a)) ### <class 'str'>
print(type(b)) ### <class 'int'>
print(type(c)) ### <class 'float'>
print(type(d)) ### <class 'float'>

# //////////////////////////////////////////////////////////////////

# Assignment Operators
a = 9
a += 9
a /= 9
a *= 9
a += 9
print(a)
### 27.0

b = 23
c = 0
print(c/b)
### 0.0

# //////////////////////////////////////////////////////////////////

# Comparison Operators
c = (3<=9)
print(c)
### True

a = (3 != 3)
print(a)
### False

d = (4>8)
print(type(d))
### <class 'bool'>

# //////////////////////////////////////////////////////////////////

# Logical Operator
bool1 = True
bool2 = False

print("The value of bool1 and bool2 is", (bool1 and bool2))
### The value of bool1 and bool2 is False
print("The value of bool1 or bool2 is", (bool1 or bool2))
### The value of bool1 or bool2 is True
print("The value of not bool2 is", (not bool2))
### The value of not bool2 is True

# //////////////////////////////////////////////////////////////////

# Find Avg number
a = 3, 4, 2, 5, 9, 2, 3
print(sum(a)/len(a))
### 4.0

# Another way:
a=3
b=4
c=2
d=5
e=9
f=2
h=3
print((a+b+c+d+e+f+h)/7)
### 4.0

# //////////////////////////////////////////////////////////////////

# Input and find avg number and percetage of values
mark1 = input("Subject 1 Marks: ")
mark1 = int(mark1)
mark2 = input("Subject 2 Marks: ")
mark2 = int(mark2)
mark3 = input("Subject 3 Marks: ")
mark3 = int(mark3)
mark4 = input("Subject 4 Marks: ")
mark4 = int(mark4)
# mark5 = input("Subject 5 Marks: ")
# mark5 = int(mark5)
total_marks = input("Total Marks: ")
total_marks = int(total_marks)

total = (mark1+mark2+mark3+mark4)

print("Your average marks is: ",total/4)
print("Your percentage is",((total/total_marks)*100),"%") #Note: total marks should be divided by the maximum marks, and then multiplied by 100)
### OUTPUT:
# Subject 1 Marks: 76
# Subject 2 Marks: 87
# Subject 3 Marks: 67
# Subject 4 Marks: 58
# Subject 5 Marks: 64
# Total Marks: 400
# Your average marks is: 70.4
# Your percentage is 88.0 %