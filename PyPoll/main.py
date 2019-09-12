# importing csv module
import csv

# Initializing Variables
Total_Number_Of_Votes = 0
candidates = []

# creating a csv object to work on
with open("Election_Results.txt", "w") as file:
    with open("election_data.csv", newline="") as csvfile:
        election_data = csv.reader(csvfile, delimiter = ',')

        # skipping header 
        next(election_data)
        
        for row in election_data:

            Total_Number_Of_Votes += 1

            # creating a list of the candidates who received a vote
            if row[2] not in candidates:
                candidates.append(str(row[2]))
        print("--------------------")
        file.write("--------------------\n")
        print("Election Results")
        file.write("Election Results\n")
        print("--------------------")
        file.write("--------------------\n")
        print(f"Total Votes: {Total_Number_Of_Votes:,.0f}")
        file.write(f"Total Votes: {Total_Number_Of_Votes:,.0f}\n")
        print("--------------------")
        file.write("--------------------\n")

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
            file.write(f"{candidate} : {(Number_Votes_Per_Candidate/Total_Number_Of_Votes)*100:.3f}% ({Number_Votes_Per_Candidate:,.0f})\n")    

            if Number_Votes_Per_Candidate > most_votes:
                most_votes = Number_Votes_Per_Candidate
                winner = candidate 
    print("--------------------")
    file.write("--------------------\n")
    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}\n") 







    




