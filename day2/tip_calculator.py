print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_factor = (int(input("What percentage tip would you like to give?"))/100)+1
people = int(input("How many people to split the bill?"))

total_per_person = "{:.2f}".format((total_bill*(tip_factor))/people,2)


print(f"Each person should pay: ${total_per_person}")


