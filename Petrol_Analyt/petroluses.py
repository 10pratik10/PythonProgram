#THIS PROJECT IS MADE BY PRATIK BAGALE TO ANAYLISE THE PETROL USES ------

print("PETROL USES ANAYLISTS")
petrol_prices = input("Enter the current petrol price per litre: ")
amount_of_petrol = input("Enter the amount of Petrol in the vehicle: ")
amount_of_petrol = int(amount_of_petrol)
mileage = input("Enter the mileage of the vehicle: ")
mileage = int(mileage)
dist1 = input("Enter the distance 1: ")
dist1 = float(dist1)
dist2 = input("Enter the distance 2: ")
dist2 = float(dist2)
dist3 = input("Enter the distance 3: ")
dist3 = float(dist3)
dist4 = input("Enter the distance 4: ")
dist4 = float(dist4)

#Now we have collected all the information -------
#We will now analyze and calculate the results ------

daily_dist = (dist1 + dist2 + dist3 + dist4)
perLitreUses = mileage/daily_dist
days_left = perLitreUses * amount_of_petrol
days_left = int(days_left)
#Int is added because days are not decimal/float values ------

print("You have ", days_left, " days left for refueling")
#We got result for number of days left
