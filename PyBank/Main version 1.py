
#**** Module 3-homework-Python challenge - PyBank*******

#Import Dependencies os and csv
import csv
import os


#  Set the path for my load and output files:
Financial_data= os.path.join("Resources", "budget_data.csv")
Financial_analysis= os.path.join("Analysis", "Analysis_PyBank.txt")

# My variables from Financial analysis
total_months = 0 # Total number of months included in the dataset
total_profit_loss = 0 # The net total amount of "profit/Losses" over the entire period
# For changes  in "profit/Losses" over the entire period, and then the average of those changes. I need the following variables:
prev_net = 0 
net_changes_list = []
month_changes = [] 

#Change current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the csv using the UTF-8 encoding and convert it into a list of dictionaries 
with open(Financial_data, encoding='UTF-8') as csvfile:
  # using delimiter 
    csvReader = csv.reader(csvfile, delimiter=",")
   
    #Read the header row
    csvHeader =next(csvReader)
    
    
    
       # Extract first row to avoid appending to net_change_list
    first_row = next(csvReader)

    total_months += 1
    total_profit_loss += int(first_row[1])
    prev_net = int(first_row[1])
    
    for row in csvReader:    
    # Track total
     total_months += 1
    total_profit_loss += int(row[1])
    
    # Trackt the net change 
    net_changes = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_changes_list  += [net_changes]
    month_changes += [row[0]]
    
    # calculate variables incre and decrea
    greatest_increase = [("") , 0]# the greatest increase in profits (data and amount)over the entire period
    greatest_decrease = [(""), 99999999999999999999999999999] # the greatest decreasessin profits (data and amount)over the entire period

    if net_changes > greatest_increase[1]:
          greatest_increase[0] = row[0]
          greatest_increase[1] = net_changes
          
          # Calculate the greatest decrease
    if net_changes < greatest_decrease[1]:
          greatest_decrease[0] = row[0]
          greatest_decrease[1] = net_changes
          
     # Calculate the Average Net Change with only two decimal
    Avg_change = round(sum(net_changes_list) / len(net_changes_list),2)
    
    # Generate output Summary of Financial Analysis
output = "----------\n"
output += f"Financial Analysis\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${net_changes}\n"
output += f"Average Change: ${Avg_change}\n"
output += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
output += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
with open(Financial_analysis,"w") as txt_file:
  txt_file.write(output)
  print(output)

    
          

    
    
        

    
      
 
          
          
            
        
        
    
    