import os
import csv
import pathlib

#define file path
election_data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "PyPoll", "Resources", "election_data.csv")

#open the csv file
with open(election_data_path, "r") as election_data_csv:
    csv_reader = list(csv.reader(election_data_csv))

data = csv_reader[1:]

total_votes = len(data)
candidates = {}
max_value = 0
winner = ''

#loop through to complete a list of candidates who received votes
for line in data:
    if line[2] not in candidates:
        candidates[line[2]] = 1
    else:
        candidates[line[2]] += 1

#the percentage of votes each candidate won

#the total number of votes each candidate won

#the winner of the election based on popular vote.
