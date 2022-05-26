supershop_list = list()
supershop_list.append("Banana")
supershop_list.append("Appple")
supershop_list.append("Mango")
supershop_list.append("Fruity")
supershop_list.append("Chicken")
supershop_list.append("Bubbly")
supershop_list.append("5-star")

print(supershop_list[3])
supershop_list[3] += "!"

#Indenfy the customer
customer_id = {"customer_name": "Jackson Sharma",
               "payment_method": "cash", "customer_type": "new"}

print("Thank you for buying", supershop_list[3], "Welcome to the BigBoss supershop Mr. {0} , you have prefered to pay by {1} and as a {2} customer we want you come again to unlock exicting offers".format(
    customer_id["customer_name"], customer_id["payment_method"], customer_id["customer_type"]))
