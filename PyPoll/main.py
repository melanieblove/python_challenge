import os
import csv
import numpy as np

from collections import Counter

total_votes=[]
candidates=[]
candidate_votes={}

#path\PyPoll\Resources\election_data.csv
poll_csv=os.path.join("PyPoll\Resources\election_data.csv")

print("Election Results")
print("-----------------------")

column_index= 2
unique_candidates=set()
# Read in the CSV file
with open(poll_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   


    ## Loop through the data
    for row in csvreader:
        #total number votes cast
        total_votes.append(row[0])

        #count each vote for each candidate 
        value= row[column_index]
        if value in candidate_votes:
            candidate_votes[value] +=1
        else:
            candidate_votes[value]=1

        #list of candidates
        unique_candidates.add(row[column_index])
    
    #unique values o names of the candidates
    unique_candidates_list= list(unique_candidates)
    unique_candidates_list.sort()

    #total of votes cast
    total_votes_sum= len(total_votes)

    #from the dictionary access to the values 
    candidate_list_values= list(candidate_votes.values())
    
    ##get the key and the value from a dictionary using the max funciton
    winner=  max(candidate_votes.items(), key=lambda item: item[1])

    
    #percentages of the votes
    candidate1= candidate_list_values[0]*100/total_votes_sum
    candidate2=candidate_list_values[1]*100/total_votes_sum
    candidate3=candidate_list_values[2]*100/total_votes_sum

        
    ##print total votes cast
    print("Total votes: "+ str(total_votes_sum))
    print('-----------------------')

    ###list of candidates with percentages and number of votes
    
    print(f"{unique_candidates_list[0]}: {candidate1:.3f}% ({candidate_votes['Charles Casper Stockham']})")
    print(f"{unique_candidates_list[1]}: {candidate2:.3f}% ({candidate_votes['Diana DeGette']})")
    print(f"{unique_candidates_list[2]}: {candidate3:.3f}% ({candidate_votes['Raymon Anthony Doane']})")

    print("------------------------")
    print(f"Winner:{winner}")
    print("------------------------")



    ## writing the result using write csv
    output_CSV_poll = [["Election Results"],
                  ["--------------------------------"],
                  ["Total votes: "+ str(total_votes_sum)],
                  [f"{unique_candidates_list[0]}: {candidate1:.3f}% ({candidate_votes['Charles Casper Stockham']})"],
                  [f"{unique_candidates_list[1]}: {candidate2:.3f}% ({candidate_votes['Diana DeGette']})"],
                  [f"{unique_candidates_list[2]}: {candidate3:.3f}% ({candidate_votes['Raymon Anthony Doane']})"],
                  ["--------------------------------"],
                  [f"Winner:{winner}"],
                  ["--------------------------------"]]

    #path to the text file\analysis
    output_file= os.path.join("PyPoll\analysis")

    ## writing the result using write csv
    with open('PyPoll\\analysis.txt','w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerows(output_CSV_poll)
    

