# importing csv module
import csv

# Initializing Variables
Total_Number_Of_Votes = 0
candidates = []

# creating a csv object to work on
with open("election_data.csv", newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ',')

    # skipping header 
    next(election_data)
        
    for row in election_data:

        Total_Number_Of_Votes += 1

        # creating a list of the candidates who received a vote
        if row[2] not in candidates:
            candidates.append(str(row[2]))
    print("----------------")
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {Total_Number_Of_Votes:,.0f}")
    print("----------------")

most_votes = 0
for candidate in candidates:
    with open("election_data.csv", newline="") as csvfile:
        election_data = csv.reader(csvfile, delimiter = ',') 

        next(election_data)
        Number_Votes_Per_Candidate = 0    
        for row in election_data:       
            if candidate == row[2]:
                Number_Votes_Per_Candidate += 1
        print(f"{candidate} : {(Number_Votes_Per_Candidate/Total_Number_Of_Votes)*100:.3f}% ({Number_Votes_Per_Candidate:,.0f})")
        

        if Number_Votes_Per_Candidate > most_votes:
            most_votes = Number_Votes_Per_Candidate
            winner = candidate 
print("----------------")
print(f"Winner: {winner}") 


    




