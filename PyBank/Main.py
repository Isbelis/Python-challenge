
#**** Module 3-homework-Python challenge - PyBank*******

#Dependencies
import csv
import os

# Files to load and output 
load_f = os.path.join("Resources", "budget_data.csv")
output_f = os.path.join("Analysis", "Analysis_PyBank.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = [("") ,0]
greatest_decrease = [(""), 9999999999999999999999999999]
total_net = 0


#Read the csv and convert it into a list of dictionaies
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(load_f) as financial_data:
    reader = csv.reader(financial_data)
    #Read the header row
    header =next(reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months+=1
    total_net+= int(first_row[1])
    prev_net = int(first_row[1])
    
    for row in reader:
        
        #Track the net change
        total_months+=1
        total_net+= int(row[1])
        
        # Trackt the net change 
        net_change =int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change +=[row[0]]
        
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
          greatest_increase[0] = row[0]
          greatest_increase[1] = net_change
          
          # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
          greatest_decrease[0] = row[0]
          greatest_decrease[1] = net_change
          
# Calculate the Average Net Change
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)


#print (output, ("Financial Analysis\n")
       #output += (f"Total months: {total_months}",
                 # f"Total: ${total_net}"))

#output =  "-----------------, Financial Analysis"
             # print(f"Total months:", total_months)
             # print(f"Total:", "$",total_net)
             # print(f"Average Change:", "$",net_monthly_avg)
             # print(f"Greatest Increase in Profits:", greatest_increase)
              #print(f"Greatest Decrease in Profits:", greatest_decrease)
print("Total Months:", total_months)
print("Total:,   $", total_net)
print("Average Change:,   $",net_monthly_avg)
print("Greatest Increase in Profits:", greatest_increase),
print("Greatest Decrease in Profits:", greatest_decrease),

with open(output_f) as output_file:
     output_file.write(output_f)
     print
          

#output = "Analysis\Analysis_PyBank.txt"
#output += f "net_monthly_avg: {net_monthly_avg}"

#with open(output_path) as output_file:
#output_file.write(output)
#print(output)

        #   #Generate Output SUmmary
        #   output = (
        #       print (f:Analysis_PyBank.txt)
        #   )

          
#print ("Financial Analysis", "")  
#print("Total months:", total_months)
#print("Total:", "$",total_net)
#print("Average Change:", "$",net_monthly_avg)
#print("Greatest Increase in Profits:", greatest_increase)
#print("Greatest Decrease in Profits:", greatest_decrease)
          
          
            
        
        
    
    