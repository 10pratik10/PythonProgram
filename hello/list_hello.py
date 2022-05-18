pratik = list()
pratik.append("Marathi")
pratik.append("English")
pratik.append("Social Science")
pratik.append("Maths")
pratik.append("Hindi")

print(pratik[3])
pratik[3] += "!"

user_info = {"first_name": "Pratik",
           "last_name": "Bagale",
           "class_name": "10",
           "roll_number": "342"}
print("We are happy invites {0} {1} from class {2}th std with roll number {3}".format(
    user_info["first_name"], user_info["last_name"], user_info["class_name"], user_info["roll_number"]))
