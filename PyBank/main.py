import os
import csv     
import numpy as np

months=[]
sum_total=0
budget_numbers = []

##PyBank\Resources\budget_data.csv
bank_csv= os.path.join('PyBank\\Resources\\budget_data.csv')
#print(bank_csv)

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
    for date, number in csvreader:
        months.append(date)
        budget_numbers.append(int(number))
    
        sum_total += int(number)


    difference = np.diff(budget_numbers)
    average= np.average(difference)
    greatest_inc=np.max(difference)
    greatest_decr=np.min(difference)

    index_greatest_inc = list(difference).index(greatest_inc) + 1
    index_greatest_decr = list(difference).index(greatest_decr) + 1

    print("Total months: " + str(len(months)))
    print(f"Total: ${sum_total}")    
    print(f"Average Change:$ {average:.2f}")
    print(f"Greatest Increase in Profits: {months[index_greatest_inc]} (${greatest_inc})")
    print(f"Greatest Increase in Profits: {months[index_greatest_decr]} (${greatest_decr})")


    output_CSV = [["Financial Analysis"],
                  ["--------------------------------"],
                  ["Total months: " + str(len(months))],[f"Total: ${sum_total}"],
                  [f"Average Change:$ {average:.2f}"],
                  [f"Greatest Increase in Profits: {months[index_greatest_inc]} (${greatest_inc})"],
                  [f"Greatest Increase in Profits: {months[index_greatest_decr]} (${greatest_decr})"]]

    output_file= os.path.join("PyBank\analysis")
    
    with open('PyBank\\analysis','w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerows(output_CSV)
    
     
          





