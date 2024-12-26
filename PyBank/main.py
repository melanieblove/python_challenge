import os
import csv     
import numpy as np
months=[]
sum_total=0
budget_numbers = []
##PyBank\Resources\budget_data.csv
bank_csv= os.path.join('PyBank\\Resources\\budget_data.csv')
#print(bank_csv)

#     ##The total number of months included in the dataset
# def print_headers(bank_data):
#      total_months = len(csvreader['Date'])
#      print("Total months:" + total_months)

print("Financial Analysis")

print("--------------------------------") 


with open(bank_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        budget_numbers.append(int(row[1]))
        sum_total += int(row[1])
    print(np.average(budget_numbers))
    print(np.max(budget_numbers))
    print(np.min(budget_numbers))
    print("Total months:" + str(len(months)))
    print(f"Total: ${sum_total}")    
    

    

     
    
     
          





