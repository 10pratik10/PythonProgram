# For counting the number of characters in the string
info = "its rest of the files that were modified and counting the number of characters"
print(len(info))
### 73

# Does the string end with the particular last word (ie, characters)
print(info.endswith("characters"))
### True

# Does the string begin with the particular last word (ie, characters)
print(info.startswith("rest"))
### False 
# Because string didn't begin with the word "rest")

# For counting the number of preferred characters in the string (for ex: r (case sensitive))
print(info.count("r"))
### 5

# For capitalizing the the word in the string
print(info.capitalize())
### Its rest of the files that were modified and counting the number of characters
# Check the line 2, first characters is small case, after compiling, the characters turn into upper case

# For finding the words/characters in the string
print(info.find("modified"))
### 32
# The word "modified" is located at 32 characters

# For replacing the the word in the string
print(info.replace("file", "folder"))
### its rest of the folders that were modified and counting the number of characters

# For creating the new line
tales = "Name: Pratik \nRoll no: 34 \nAddress: Pune \nGender: None"
print(tales)