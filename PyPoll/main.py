import os
import csv
import pathlib

#define file path
election_data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "PyPoll", "Resources", "election_data.csv")

#open the csv file
with open(election_data_path, "r") as election_data_csv:
    csv_reader = csv.reader(election_data_csv)

    
    for line in csv_reader:

        print(line)
#the total number of votes cast

#a complete list of candidates who received votes

#the percentage of votes each candidate won

#the total number of votes each candidate won

#the winner of the election based on popular vote.
