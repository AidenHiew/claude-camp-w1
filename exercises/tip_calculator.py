#Tips Calculator
#This Calculator is to allow user to calculate the tip amount needing to pay for the meal.
#While in Australia we don't pay tips, but in US it seems like a norm. 
#In this calculator, we'll allow userto input the meal cost, the tips percentage. 

print("Welcome to the Tips Calculator!")
print ("I know it is not easy to calculate the tips, but this shoudl help you out")

meal_cost = float(input("How much was your meal? $"))
tips_percentage = float(input("How much tips percentage would you like to give?"))

print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tips percentage: {tips_percentage}%")

tips_amount = (meal_cost * tips_percentage/100)

print(f"Therefore, Tips amount is: ${tips_amount}")                  

print("The Waiting staff will be very happy to receive your tips, have a great day!")
