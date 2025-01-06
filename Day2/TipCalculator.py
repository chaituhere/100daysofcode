# Day 2: DataTypes, Numbers, Operations, Type Conversions, F-Strings
# Tip Calculator Project
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
amount_per_person = total_bill / people

print(f"Each person should pay: ${amount_per_person:.2f}")
