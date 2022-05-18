hello_list = list()
hello_list.append("Marathi")
hello_list.append("English")
hello_list.append("Hindi")
hello_list.append("Geograhy")

hello_dict = {"first_name": "Liam",
              "last_name": "Fraser",
              "eye_colour": "Blue"}
print(hello_list[2])
hello_list[2] += "!"

print("{0} {1} has {2} eyes".format(
    hello_dict["first_name"], hello_dict["last_name"], hello_dict["eye_colour"]))
