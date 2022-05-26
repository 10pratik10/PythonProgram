# For printing the list
list = [4, 6, 7, 8, 9, 10, 11, 12]
print(list)
### [4, 6, 7, 8, 9, 10, 11, 12]

# For printing the particular list
name_list = ["Pratik", "Rahul", "Raju", "Amesh", "Larry"]
print(name_list[0:2])
### ['Pratik', 'Rahul']

# For sorting out the list
l1 = [1, 9, 3, 4,12, 44, 5, 6, 7]
l1.sort()
print(l1)
### [1, 3, 4, 5, 6, 7, 9, 12, 44]

# For reversing the list 
l1.reverse()
print(l1)
### [44, 12, 9, 7, 6, 5, 4, 3, 1]

# For adding a new item to the end of the list
l1.append(86)
l1.append(69)
print(l1)
### [44, 12, 9, 7, 6, 5, 4, 3, 1, 86, 69]

# For adding the value after particular items
l2 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14]
l2.insert(9, 23)
print(l2)
### [1, 2, 3, 4, 5, 7, 8, 9, 10, 23, 11, 12, 13, 14]

# For removing the value from the list
l2.pop(3)
print(l2)
### [1, 2, 3, 5, 7, 8, 9, 10, 23, 11, 12, 13, 14]

# For removing the particular value from the list
l2.remove(12)
print(l2)
### [1, 2, 3, 5, 7, 8, 9, 10, 23, 11, 13, 14]