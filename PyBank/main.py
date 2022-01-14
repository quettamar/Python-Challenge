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

print(data)        
            
total_months = len(data)    
total_amount = 0
profit_loss_column = []   
profit_change = 0

for row in data:
    #this is adding up all the volumes in the profit colum
    #total_amount = total_amount + int[(row[1])]
    total_amount += int(row[1])
    profit_loss_column.append(int(row[1]))
    

#print(total_amount)   
print(total_months)

#the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_loss_column)
date_increase = data[profit_loss_column.index(greatest_increase)][0]

#the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(profit_loss_column)
date_decrease = data[profit_loss_column.index(greatest_decrease)][0]

#calculating the average change
average_loss = total_amount / total_months
#print(average_loss)
#print(date_decrease)
#print(greatest_decrease)

#print(greatest_increase)
#print(date_increase)

#create a loop that will calculate the amount of change between each month

#create a txt file with the results
#f = open("budget_results.txt", "w")
results_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "PyBank", "Analysis")
f = open("budget_results.txt", "w")

f.write(f"Financial Analysis\n----------------------------------\n")
f.write(f"Your profit is: ${total_amount}\n")
f.write(f"Total Months {total_months}\n")
#f.write(f"Average  Change: ${}\n")
f.write(f"Greatest Increase in Profits: (${date_increase})\n")
f.write(f"Greatest Decrease in Profits: (${date_decrease})\n")

print(f"\nFinancial Analysis\n----------------------------------\n")
print(f"Your profit is: ${total_amount}\n")
print(f"Total Months: 86 months")
#print(f"Average  Change: ${}")
print(f"Greatest Increase in Profits was in {date_increase} for (${greatest_increase}.)")
print(f"Greatest Decrease in Profits was in {date_decrease} for (${greatest_decrease}.)")

f.close