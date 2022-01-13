import os
import csv
import pathlib

#define file path
budget_data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "PyBank", "Resources", "budget_data.csv")

#open the csv file
with open(budget_data_path, "r") as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter=',')

    header = next(csv_reader)

    for row in csv_reader:
        print(row)
    #the total number of months included in the dataset

    #the net total amount of "Profit/Losses" over the entire period

    #Calculate the changes in "Profit/Losses" 
    #over the entire period, then find the average of those changes


    #the greatest increase in profits (date and amount) over the entire period


    #the greatest decrease in profits (date and amount) over the entire period