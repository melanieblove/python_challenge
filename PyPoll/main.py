import os
import csv
import numpy as np

from collections import Counter

total_votes=[]
winner=[]
candidates=[]
candidate_votes={}


poll_csv=os.path.join("PyPoll\Resources\election_data.csv")

print("Election Results")
print("-----------------------")

column_index= 2
unique_candidates=set()

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    # Read each row of data after the header
    for row in csvreader:
        #total number votes cast
        total_votes.append(row[0])

        value= row[column_index]
        if value in candidate_votes:
            candidate_votes[value] +=1
        else:
            candidate_votes[value]=1

        #list of candidates
        unique_candidates.add(row[column_index])
    
    unique_candidates_list= list(unique_candidates)

           #count each vote for each candidate
    #counts_votes=[row[column_index] for row in unique_candidates_list]
    #numbers_votes= Counter(counts_votes)
    
    #candidate0= str(unique_candidates_list[0].append(numbers_votes))
    #candidate1=str(unique_candidates_list[1].append(numbers_votes)) 
    #candidate2=str(unique_candidates_list[2].append(numbers_votes)) 

    ##print total votes cast
    print("Total votes: "+ str(len(total_votes)))
    print('-----------------------')

    ###list of candidates str{candidate0}
    
    print(f"{unique_candidates_list[0]}:  ")
    print(f"{unique_candidates_list[1]}:  ")
    print(f"{unique_candidates_list[2]}:  ")     

    #print votes of each candidate
    print(candidate_votes)

    # def list_candidates(candidates):
    #         counts=Counter(row[2])
    #         candidates.append(counts) 

    #         for i in candidates:
        
    #          print(f"Row{i+1} count:{dict(candidates)}")
      