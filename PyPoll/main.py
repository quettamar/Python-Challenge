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

#loop through to complete a list of candidates who received votes
for line in data:
    if line[2] not in candidates:
        candidates[line[2]] = 1
    else:
        candidates[line[2]] += 1

#the percentage of votes each candidate won
khan = ((candidates["Khan"])/total_votes)
correy = ((candidates["Correy"])/total_votes)
li = ((candidates["Li"])/total_votes)
tooley = ((candidates["O'Tooley"])/total_votes)

#changing into a percentage format
khan_percentage = "{:.3%}".format(khan)
correy_percentage = "{:.3%}".format(correy)
li_percentage = "{:.3%}".format(li)
tooley_percentage = "{:.3%}".format(tooley)

#the total number of votes each candidate won
khan_votes = (candidates["Khan"])
correy_votes = (candidates["Correy"])
li_votes = (candidates["Li"])
tooley_votes = (candidates["O'Tooley"])

print(f"Election Result")
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25)
print(f"Khan: {khan_percentage}% ({khan_votes})")
print(f"Correy: {correy_percentage}% ({correy_votes})")
print(f"Li: {li_percentage}% ({li_votes})")
print(f"O' Tooley: {tooley_percentage}% ({tooley_votes})")
print(f"    ")
print(f"Winner = Khan")
print("-"*25)

#create a txt file with the election results
#come back later to figure out how to change directories
f = open(r"C:\\Users\marqu\OneDrive\Desktop\Repositories\Python-Challenge\PyPoll\Analysis\election_results.txt","w")
f.write(f"Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("-------------------------\n")
f.write(f"Khan: {khan_percentage}% ({khan_votes})\n")
f.write(f"Correy: {correy_percentage}% ({correy_votes})\n")
f.write(f"Li: {li_percentage}% ({li_votes})\n")
f.write(f"O' Tooley: {tooley_percentage}% ({tooley_votes})\n")
f.write("-------------------------\n")
f.write("Winner: Khan\n")

f.close