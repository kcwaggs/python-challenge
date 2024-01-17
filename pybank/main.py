# Dependencies of analysis:
import os
import csv

# Variables to use:
total_months = 0
total_profit_loss = 0
maximum_profit = 0
minimum_profit = 0
change = []
min_profit_date = []
max_profit_date = []

# Path to collect data from the csv file in the Resources folder
# you need to be in the PyBank folder to collect the correct results for this path. 
csv_path = os.path.join("resources", "budget_data.csv")

# Run through the CSV file - collect information from first row:
with open(csv_path, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvfile)
   next_row = next(csvreader)
   total_months = total_months + 1
   total_profit_loss += int(float(next_row[1]))
   previous = int(float(next_row[1]))

   # For loop to get the profit total, change, and months:
   for row in csvreader:
      total_months = total_months + 1
      total_profit_loss += int(float(row[1]))
      change_profit_loss = int(float(row[1])) - previous
      change.append(change_profit_loss)
      previous = int(row[1])

      # if statement to determine the maximum and minimum profit changes:
      if change_profit_loss > maximum_profit:
         maximum_profit = change_profit_loss
         max_profit_date = row[0]
      if change_profit_loss < minimum_profit:
         minimum_profit = change_profit_loss
         min_profit_date = row[0]

# calculate the average:
average = sum(change) / len(change)

# identify the results - format them as necessary:
results = (
   f"---------------------------------------\n"
   f"Financial Analysis\n"
   f"---------------------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_profit_loss:,.0f}\n"
   f"Average Change: ${average:,.2f}\n"
   f"---------------------------------------\n"
   f"Greatest Increase in Profits: {max_profit_date} (${maximum_profit:,.0f})\n"
   f"Greatest Decrease in Profits: {min_profit_date} (${minimum_profit:,.0f})\n"
   f"---------------------------------------\n"
)

# ptint the results and add to text file - this will create a file if none exists:
print(results)
with open("analysis/analysis.txt",'w') as txtfile:
   txtfile.write(results)