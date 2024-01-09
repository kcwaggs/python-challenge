# import CSV 
import os

f = open("analysis/analysis.txt",'w')
f.write('')
f.close()

# variables
t = 0
total_counter = 0
candidate_1 = "Charles Casper Stockham"
candidate_1_counter = 0
candidate_2 = "Diana DeGette"
candidate_2_counter = 0
candidate_3 = "Raymon Anthony Doane"
candidate_3_counter = 0

# pathing and read CSV file
pypoll_csv = os.path.join('resources','election_data.csv')
with open(pypoll_csv) as csvfile:
    import csv
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        total_counter += 1
        if row[2] == candidate_1:
            candidate_1_counter += 1
        elif row[2] == candidate_2:
            candidate_2_counter += 1
        elif row[2] == candidate_3:
            candidate_3_counter += 1

# percent of votes per candidate
candidate_1_percent = ((candidate_1_counter / total_counter)*100).__round__(3)
candidate_2_percent = ((candidate_2_counter / total_counter)*100).__round__(3)
candidate_3_percent = ((candidate_3_counter / total_counter)*100).__round__(3)

# determine the winner 
if candidate_1_counter > candidate_2_counter and candidate_3_counter:
    winner = candidate_1
elif candidate_2_counter > candidate_1_counter and candidate_3_counter:
    winner = candidate_2
elif candidate_3_counter > candidate_1_counter and candidate_2_counter:
    winner = candidate_3

#print the results
def results():
    print('---------------------')
    print('Election Results')
    print('---------------------')
    print(f"Total Votes: {total_counter}")
    print('---------------------')
    print(f"{candidate_1}: {candidate_1_percent}% ({candidate_1_counter})")
    print(f"{candidate_2}: {candidate_2_percent}% ({candidate_2_counter})")
    print(f"{candidate_3}: {candidate_3_percent}% ({candidate_3_counter})")
    print('---------------------')
    print(f"Winner: {winner}")
    print('---------------------')
    return()
results()


with open("analysis/analysis.txt",'w') as f:
    print('---------------------',file = f)
    print('Election Results',file = f)
    print('---------------------',file = f)
    print(f"Total Votes: {total_counter}",file = f)
    print('---------------------',file = f)
    print(f"{candidate_1}: {candidate_1_percent}% ({candidate_1_counter})",file = f)
    print(f"{candidate_2}: {candidate_2_percent}% ({candidate_2_counter})",file = f)
    print(f"{candidate_3}: {candidate_3_percent}% ({candidate_3_counter})",file = f)
    print('---------------------',file = f)
    print(f"Winner: {winner}",file = f)
    print('---------------------',file = f)
    f.close()