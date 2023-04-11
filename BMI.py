# Ask the user for their weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI using the formula: BMI = weight (kg) / height^2 (m^2)
bmi = weight / (height ** 2)

# Interpret the BMI value
if bmi < 18.5:
    interpretation = "underweight"
elif bmi >= 18.5 and bmi < 25:
    interpretation = "normal weight"
elif bmi >= 25 and bmi < 30:
    interpretation = "overweight"
else:
    interpretation = "obese"

# Print the calculated BMI and interpretation
print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI interpretation is: {interpretation}")
