import os
import csv

print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

csvpath = os.path.join("Resources", "election_data.csv")

candidates = []
num_votes = 0
vote_counts = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    line = next(csvreader,None)
    for line in csvreader:
        num_votes = num_votes + 1

        candidate = line[2]
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)
percentages = []
max_votes = vote_counts[0]
max_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

print("Election Results")
print("--------------------")
print(f"Total Votes: {num_votes}")
for count in range (len(candidates)):
    print(f"candidates")
