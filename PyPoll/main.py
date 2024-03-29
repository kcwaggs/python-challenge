# import CSV 
import os

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
# you need to be in the PyPoll folder for this path to work
pypoll_csv = os.path.join('resources','election_data.csv')

# set up the CSV reading 
with open(pypoll_csv) as csvfile:
    import csv
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    
    # for loop to grab the row totals (votes)
    for row in csvreader:
        total_counter += 1
        
        # conditional statements to calculate the per candidate votes
        if row[2] == candidate_1:
            candidate_1_counter += 1
        elif row[2] == candidate_2:
            candidate_2_counter += 1
        elif row[2] == candidate_3:
            candidate_3_counter += 1

# calculate percent of votes per candidate and round the decimal place
candidate_1_percent = ((candidate_1_counter / total_counter)*100).__round__(3)
candidate_2_percent = ((candidate_2_counter / total_counter)*100).__round__(3)
candidate_3_percent = ((candidate_3_counter / total_counter)*100).__round__(3)

# calculate the winner with conditional statement
if candidate_1_counter > candidate_2_counter and candidate_3_counter:
    winner = candidate_1
elif candidate_2_counter > candidate_1_counter and candidate_3_counter:
    winner = candidate_2
elif candidate_3_counter > candidate_1_counter and candidate_2_counter:
    winner = candidate_3

# identify the results from analysis
results = (
    f"---------------------------------------\n"
    f"Elections Results\n"
    f"---------------------------------------\n"
    f"Total Votes: {total_counter:,.0f}\n"
    f"---------------------------------------\n"
    f"{candidate_1}: {candidate_1_percent:,.2f}% ({candidate_1_counter:,.0f})\n"
    f"{candidate_2}: {candidate_2_percent:,.2f}% ({candidate_2_counter:,.0f})\n"
    f"{candidate_3}: {candidate_3_percent:,.2f}% ({candidate_3_counter:,.0f})\n"
    f"---------------------------------------\n"
    f"Winner: {winner}\n"
    f"---------------------------------------\n"
)

# print the results and add to text file - this will create a file if none exists. 
print(results)
with open("analysis/analysis.txt",'w') as txtfile:
    txtfile.write(results)