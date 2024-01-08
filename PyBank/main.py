import os
import csv

# Path to collect data from the csv file in the Resources folder
pybank_csv = os.path.join("PyBank","resources", "budget_data.csv")

# total months
m = 0
with open(pybank_csv, 'r') as csv1:       
   csvreader1 = csv.reader(csv1, delimiter=',')
   next(csv1, None)
   for row in csvreader1:
      m += 1

# total profits/losses 
with open(pybank_csv, 'r') as csv2:       
   csvreader2 = csv.reader(csv2, delimiter=',')
   next(csv2, None)
   t = sum(int(row[1]) for row in csvreader2)

#print the results
print(f"Total Months: {m}")
print(f"Total: ${t}")
print(f"Average Change: ${t}")
print(f"Greatest Increase in Profits: ${t}")
print(f"Greatest Decrease in Profits: ${t}")
