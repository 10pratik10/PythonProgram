#string1 = 'don't fuck with me'
#print(string1)
#(In 1 & 2 put comment by adding #)

#string1 will not be complile because there's three single quotation marks in between the sentence to define. In that case, computer will only identfy the word (don) and rest of the words are left in the blank state without any syntax because you leaved the rest of the word without giving any function or variable. It will cause error and it will be invalid syntax. Always keep eye on such little thing. Let's solve the issue.
#Since, Python allow to use both single ('') or double ("") quoutation mark. If there's a word with quotion mark like (don't, can't etc), we can use double quotation mark ("") for Literal (the sentence or word we want to print). Solution given below:

string2 = "don't fuck with me" 
print(string2)

#Trick to use single qoutation mark in literal.

string4 = 'don'
string5 = 't fuck with me'
print(string4 + ("'")+ string5)

#I don't suggest to use this kind of trick everytime, but it helps in logical thinking, which is more important for programming. Try to create trick of your own.
#No matter how fluent coding your have, programmer with more logical + coding skills are the best programmer.

string6 = "Pratik don't like to dance" 
print(string6)#you can use double quotation mark for any string or values. 