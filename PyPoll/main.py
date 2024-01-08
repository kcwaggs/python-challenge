import os
import csv

pypoll_csv = os.path.join('resources','election_data.csv')
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)