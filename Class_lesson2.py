import os
import csv

# Prompt user for video lookup
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
# Set path for file
cereal_csv_path = os.path.join("Resources", "cereal_bonus.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
