import os
import csv

# Prompt user for video lookup

os.chdir(os.path.dirname(__file__))
# Set path for file
cereal_csv_path = os.path.join("01-Stu_CerealCleaner", "Resources", "cereal_bonus.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header =next(csvfile)
    print(f"Header: {csv_header}")

    for row in csv_reader:

        if float (row[7]) >= 5:
            print(row)