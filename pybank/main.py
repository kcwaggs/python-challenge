# Dependencies
import os
import csv

# Variables
total_months = 0
total_profit_loss = 0
maximum_profit = 0
minimum_profit = 0
change = []
min_profit_date = []
max_profit_date = []

# Path to collect data from the csv file in the Resources folder
csv_path = os.path.join("resources", "budget_data.csv")

# Run through the CSV file
with open(csv_path, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvfile)
   next_row = next(csvreader)
   total_months = total_months + 1
   total_profit_loss += int(float(next_row[1]))
   previous = int(float(next_row[1]))

   for row in csvreader:
      total_months = total_months + 1
      total_profit_loss += int(float(row[1]))
      change_profit_loss = int(float(row[1])) - previous
      change.append(change_profit_loss)
      previous = int(row[1])

      if change_profit_loss > maximum_profit:
         maximum_profit = change_profit_loss
         max_profit_date = row[0]
      if change_profit_loss < minimum_profit:
         minimum_profit = change_profit_loss
         min_profit_date = row[0]

average = sum(change) / len(change)
average = average.__round__(2)
total_profit_loss = total_profit_loss

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

print(results)
with open("analysis/analysis.txt",'w') as txtfile:
   txtfile.write(results)