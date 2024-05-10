
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
net_changes = []
month_changes = [] 

#Change current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the csv using the UTF-8 encoding and convert it into a list of dictionaries 
with open(Financial_data, encoding='UTF-8') as csvfile:
  # using delimiter 
    csvReader = csv.reader(csvfile, delimiter=",")
   
    #Read the header row
    csvHeader =next(csvReader)
    print(f"CSV Header: {csvHeader}")
    
    
 
          
          
            
        
        
    
    