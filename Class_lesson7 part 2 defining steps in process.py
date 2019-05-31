import os
import csv

os.chdir(os.path.dirname(__file__))

print(os.path.dirname(__file__))

wrestling_csv = os.path.join( "08-Par_WrestlingWithFunctions", "Resources", "WWE-Data-2016.csv")
print(wrestling_csv)

#defining the variables of wins, losses, draws and wrestler name
def print_percentages(wrestler_data):
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

#Create formulas to determine the wrestlers wins, losses and draws percentage based off total matches
    total_matches = wins + losses + draws
    win_percent = (wins / total_matches) * 100
    loss_percent = (losses / total_matches) * 100
    draw_percent = (draws / total_matches) * 100
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    print(f"Stats for {name}")
    print(f"Win percent: {str(win_percent)}")
    print(f"Loss percent: {str(loss_percent)}")
    print(f"Draw percent: {str(draw_percent)}")
    print(f"{name} is a {type_of_wrestler}")

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
