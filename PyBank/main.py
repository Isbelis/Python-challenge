#**** Module 3-homework-Python challenge - PyBank*******

#Import Dependencies os and csv
import csv
import os

#  Set the path for my load and output files:
Financial_data = os.path.join("Resources", "budget_data.csv")
Financial_analysis = os.path.join("Analyisis", "Analysis_PyBank.txt")

# My variables from Financial analysis
Count_of_Months = 0 
Change_Month = []
netchange_list = []
Greatest_incre = [("") , 0]
Greatest_decre = [(""), 9999999999999]
Total_net = 0
net_changes = 0
#Change current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the csv using the UTF-8 encoding and convert it into a list of dictionaries 
with open(Financial_data, encoding='UTF-8') as csvfile:
  # using delimiter 
    csvReader = csv.reader(csvfile, delimiter=",")
   
    #Read the header row
    csvHeader =next(csvReader)
    
    
       # Extract first row to avoid appending to netchange_list
    first_row = next(csvReader)

    Count_of_Months += 1
    Total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    for row in csvReader:    
    
    # Track total
     Count_of_Months += 1
     Total_net += int(row[1])
    
 # Trackt the net change 
     net_changes = int(row[1]) - previous_net 
     previous_net = int(row[1])
     netchange_list += [net_changes]
     Change_Month += [row[0]]
          
        
    # calculate variables incre and decrea
    
     if net_changes > Greatest_incre[1]:
          Greatest_incre[0] = row[0]
          Greatest_incre[1] = net_changes
          
          # Calculate the greatest decrease
     if net_changes < Greatest_decre[1]:
          Greatest_decre[0] = row[0]
          Greatest_decre[1] = net_changes
          
     # Calculate the Average Net Change with only two decimal
Avg_change = sum(netchange_list) / len(netchange_list)
    
    # Generate output Summary of Financial Analysis
output = ("----------\n"
    f"Financial Analysis\n"
    f"Total Months: {Count_of_Months}\n"
    f"Total: ${Total_net}\n"
    f"Average Change: ${Avg_change:.2f}\n"
    f"Greatest Increase in Profits: {Greatest_incre[0]} (${Greatest_incre[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_decre[0]} (${Greatest_decre[1]})\n")
 
with open(Financial_analysis,"w") as txt_file:
 txt_file.write(output)
print(output)
  