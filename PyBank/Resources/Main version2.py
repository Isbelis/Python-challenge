#**** Module 3-homework-Python challenge - PyBank*******


#Import Dependencies os and csv
import csv
import os

#  Set the path for my load and output files:
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output= os.path.join("Analysis", "Analysis Pybank version 2.txt")

# TRack various financila parameters
total_months = 0 
month_of_change = []
net_change_list = []
greatest_increase = [("") , 0]
greatest_decrease = [(""), 99999999999999999999999999999]
total_net = 0

#Change current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the csv using the UTF-8 encoding and convert it into a list of dictionaries 

     
with open (file_to_load) as financial_data:
     reader = csv.reader(financial_data)
     
     #read the header row
     header = next(reader)
  
# Extract firs row to avoid appeding to net_change_list
first_row = next (reader)  
total_months += 1
total_net += int(first_row[1])
prev_net = int(first_row[1])

for row in reader:
     
     # Track the total
     total_months += 1
     total_net += int(row[1])
     
     # Track the net change
     net_change = int(row[1]) - prev_net
     prev_net = int(row[1]) 
     net_change_list += [net_change]
     month_of_change += [row[0]]
     
     # calculate the greatest increase
     if net_change > greatest_increase[1]:
          greatest_increase[0] = row[0]
          greatest_increase[1] = net_change
          
     # calculate the greatest increase
     if net_change > greatest_decrease[1]:
         greatest_decrease[0] = row[0]
         greatest_decrease[1] = net_change
         
# Calculate the Average Net change
net_monthly_avg = round(sum(net_change_list) / len(net_change_list))
          
output = "----------\n"
output += f"Financial Analysis\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${total_net }\n"
output += f"Average Change: ${net_monthly_avg}\n"
output += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
output += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
with open(file_to_output,"w") as txt_file:
  txt_file.write(output)
  print(output)

