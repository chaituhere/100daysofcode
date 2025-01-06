# Day 2: DataTypes, Numbers, Operations, Type Conversions, F-Strings
# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
print(round(bmi, 2))

# From Day 3: if-else concepts
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
else:
    print("Overweight")
