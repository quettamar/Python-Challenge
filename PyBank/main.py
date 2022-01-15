from audioop import avg
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
            
total_months = len(data)    
total_amount = 0
profit_loss_column = []  
profit_change = []
profit_loss = 0

for row in data:
    #this is adding up all the volumes in the profit colum
    #total_amount = total_amount + int[(row[1])]
    total_amount += int(row[1])
    profit_loss_column.append(int(row[1]))

    profit_change.append(int(row[1])-profit_loss)
    profit_loss = int(row[1])
    
    

#the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_change)
date_increase = data[profit_change.index(greatest_increase)][0]

#the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(profit_change)
date_decrease = data[profit_change.index(greatest_decrease)][0]

#calculating the average change
total_change = sum(profit_change)
#come back and figure out why you're getting a positive number
profit_average_change = total_change / total_months

#create a txt file with the budget analysis results
f = open(r"C:\\Users\marqu\OneDrive\Desktop\Repositories\Python-Challenge\PyBank\Analysis\budget_results.txt", "w")

f.write(f"Financial Analysis\n")
f.write("----------------------\n")
f.write(f"Your profit is: ${total_amount}\n")
f.write(f"Total Months {total_months}\n")
f.write(f"Average  Change: ${profit_average_change}\n")
f.write(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})\n")
f.write(f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})\n")

print(f"Financial Analysis")
print("-"*25)
print(f"Your profit is: ${total_amount}")
print(f"Total Months: 86 months")
print(f"Average  Change: ${profit_average_change}")
print(f"Greatest Increase in Profits was in {date_increase} for ${greatest_increase}.")
print(f"Greatest Decrease in Profits was in {date_decrease} for ${greatest_decrease}.")

f.close