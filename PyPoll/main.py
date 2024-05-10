#***********************************************
# Module 3-homework-Python challenge - PYPOLL
#*************************************************
#Importing Dependecies  os and csv (my files)
#*************************************************
# Dependecies
import os
import csv


# Files to load and output 
Election_data = os.path.join("Resources", "election_data.csv")
Election_analysis = os.path.join("Analysis", "Election Results")

# My variables from Financial analysis
count_of_votes = 0
List_candidates = []
candidate = []
percent_candidate = []
total_candidate= []
total_voter = 0
last_count = 0

#Change current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the csv using the UTF-8 encoding and convert it into a list of dictionaries 
with open(Election_data, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read header row first
    csv_header = next(csvfile)
 
    
    for row in csv_reader:
        List_candidates .append(row[2])

    count_of_votes = len(List_candidates )
#print(count_of_votes)

# Name all candidates
for name in List_candidates:
    if name not in candidate:
        candidate.append(name)
        x = name

# Set first candadidate on the dandidate_vote_list for loop
candidates = List_candidates [0]

for vote in List_candidates :
        if candidates == vote:
            total_voter += 1
percent = total_voter/len(List_candidates)
percent_candidate.append(percent)
total_candidate.append(total_voter)

if last_count < total_voter:
        Winner = candidates
print(f"{candidates}: {percent:.3%} ({total_voter})")

    # Reset candidate votes to zero to name the winner
last_count = total_voter
total_voter = 0
"""
output = ("----------\n"
    "Election Results\n"
    "-------------------------\n"
    "--------------------------\n"
    "Total Votes: {count_of_votes}\n"
    "--------------------------\n"
   for candidates in candidate: 
       index = candidate.index(candidates)
   f"{candidates}: {percent_candidate[index]:.3%} ({total_candidate[index]})\n"
   "--------------------------\n"
   f"Winner: {Winner}\n"
   "---------------------\n")
"""
with open(Election_analysis,"w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {count_of_votes}\n")
    output_file.write("-------------------------\n")
    for candidates in candidate: 
        index = candidate.index(candidates)
    output_file.write(f"{candidates}: {percent_candidate [index]:.3%} ({total_candidate[index]})\n ")
    output_file.write("------------------------\n")
    output_file.write(f"Winner: {Winner}\n")
"""
with open(Election_analysis,"w") as txt_file:
    txt_file.write(output)
print (output)


# Set loop for list of candidates who recieved votes, percentage of votes, total num for each candidate, and winner
for candidates in candidate:
    for vote in List_candidates :
        if candidates == vote:
            total_voter += 1
    percent = total_voter/len(List_candidates)
    percent_candidate.append(percent)
    total_candidate.append(total_voter)

    if last_count < total_voter:
        Winner = candidates
    print(f"{candidates}: {percent:.3%} ({total_voter})")

    # Reset candidate votes to zero to name the winner
    last_count = total_voter
    total_voter = 0

# Print election winner with popular vote
print("---------------------")
print(f"Winner: {Winner}")
print("---------------------")


# Output data to PyPoll_analysis.txt
election_file = os.path.join("Analysis", "Analysis Pypoll.txt")

with open(election_file, "w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {count_of_votes}\n")
    output_file.write("-------------------------\n")
    for candidates in candidate: 
        index = candidate.index(candidates)
        output_file.write(f"{candidates}: {percent_candidate[index]:.3%} ({total_candidate[index]})\n ")
    output_file.write("------------------------\n")
    output_file.write(f"Winner: {Winner}\n")
    """