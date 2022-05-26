letter = '''<name>
<address>
Hello, you have been registered as official member of our team
<date>
'''
name = input("Enter your name: \n")
address = input("Enter your address: \n")
date = input("Enter a date: \n")

letter = letter.replace("<name>", name)
letter = letter.replace("<address>", address)
letter = letter.replace("<date>", date)

print(letter)

### Sly
### Pune
### Hello, you have been registered as official member of our team
### 24 March