import sys
target_int = input("How many integers?")
try:
    num_ints = int(input("How many integers? "))
except ValueError:
    exit("You must input an integer.")

ints = []
while len(ints) < num_ints:
    try:
        ints.append(int(input(f"Please enter {len(ints)+1}: ")))
    except ValueError:
        print("You must enter an integer")

print("Using a for loop")
for v in ints:
    print(v)

print("Using a while loop")
while ints:
    print(ints.pop(0))