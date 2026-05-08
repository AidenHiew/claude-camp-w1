#This is a BMI Calculator. 
# It calculates the Body Mass Index (BMI) based on the user's weight and height, and provides feedback on their BMI category.
# The BMI categories are as follows:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 25   
# Overweight: 25 <= BMI < 30
# Obesity: BMI >= 30

#the calculation of BMI is weight (kg) / (height (m) * height (m))
#user to enter weight in kg and height in cm, then convert height to meters for the calculation.
print("This is a simple BMI calculator that takes user input for weight and height, calculates the BMI, and provides feedback on the user's BMI category. The code includes comments to explain each step of the process.")

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI using the formula: weight (kg) / (height (m) * height (m))
    bmi = weight / (height_m ** 2)
    return bmi

# Get user to input weight in KG and height in CM
weight = float(input("Please enter your weight in KG:"))
height = float(input("Please enter your height in CM:"))

# Calculate BMI
bmi = calculate_bmi(weight, height)

print()

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, which is considered as underweight.")
elif bmi <25 and bmi >=18.5:
    print(f"Your BMI is {bmi:.2f}, which is considered as normal weight.")
elif bmi <30 and bmi >=25:
    print(f"Your BMI is {bmi:.2f}, which is considered as overweight.")
elif bmi >=30: 
    print(f"Your BMI is {bmi:.2f}, which is considered as obesity.")

print()

print("Thank you for using the BMI Calculator! and please stay healthy and well")



