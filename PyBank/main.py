import os
import csv
import pathlib

#define file path
budget_data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "PyBank", "Resources", "budget_data.csv")

#open the csv file
with open(budget_data_path, "r") as budget_csv:

    #look at the csv file's budget data and setting it up as a list
    data = list(csv.reader(budget_csv))
    #this is skipping the header
    data = data[1:]

#print(data)        
            
total_months = len(data)    
total_amount = 0
profit_loss_column = []   

for row in data:
    #this is adding up all the volumes in the profit colum
    #total_amount = total_amount + int[(row[1])]
    total_amount += int(row[1])
    profit_loss_column.append(int(row[1]))

#print(total_amount)   
#print(total_months)

#the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_loss_column)
date_increase = data[profit_loss_column.index(greatest_increase)][0]

#the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(profit_loss_column)
date_decrease = data[profit_loss_column.index(greatest_decrease)][0]

#calculating the average change
average_loss = total_amount / total_months
