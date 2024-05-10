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

# Define my variables:

Total_votes = 0   # total of votes
Cands_list = []   # list of candidates
net_change_list = []
greatest_increase = [("") ,0]
greatest_decrease = [(""), 9999999999999999999999999999]
total_net = 0

#**********************************************
 # make a function to separate the responsibility
def calculate_percents(inp_row):
    # do more work (check if attendees > 0)
    if (int(inp_row[1]) != 0):
        public_perc = int(inp_row[2]) / int(inp_row[1])
    else:
        public_perc = 0

    if (int(inp_row[3]) != 0):
        nonprofit_perc = int(inp_row[4]) / int(inp_row[3])
    else:
        nonprofit_perc = 0

    if (int(inp_row[5]) != 0):
        profit_perc = int(inp_row[6]) / int(inp_row[5])
    else:
        profit_perc = 0

    # combine in a dictionary
    data = {
        "Public Percent": public_perc,
        "Non-Profit Percent": nonprofit_perc,
        "Profit Percent": profit_perc
    }

    return (data)



# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(inp_list):
    # do work
    mean = sum(inp_list) / len(inp_list)
    return mean

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))


    # -*********************************************
  