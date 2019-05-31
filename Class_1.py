# Creates a variable with a string "Frankfurter"
title = "Ayrton Bayer"
name = input("what is your name?")
age = int(input("how old are you?"))
# Creates a variable with an integer 80
years = 25
hourly_wage = 15
# Creates a variable with the boolean value of True
satisfied = True
expert_status = True
# Prints a statement adding the variable
print("Nick is a professional " + title)
daily_wage = (str(hourly_wage)*8)
# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")