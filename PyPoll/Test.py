import os 
import csv
with open('c:\\Users\\Needra Pc\\python-challenge\\PyPoll\\Resources\\election_data.csv',mode='r') as file:
    csvReader = csv.reader(file)
    next(csvReader)
    Total_Votes = 0
    votes = 0
    vote_percentage = 0
    winning_count = 0
    Candidates_List = []
    Candidates_Votes = {}
    Candidates_Percentages = {}
    Winning_Candidate = []
    for row in csvReader:
        Total_Votes  = Total_Votes + 1
        Candidates=(row[2])
        if Candidates not in Candidates_List:
            Candidates_List.append(Candidates)
            Candidates_Votes[Candidates] = 0
        Candidates_Votes[Candidates] = Candidates_Votes[Candidates] + 1
 # Retrieve vote count and percentage
    for candidate in Candidates_Votes:
        votes = Candidates_Votes.get(candidate)
        vote_percentage = float(votes) / float(Total_Votes) * 100
    
        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            Winning_Candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        Candidates_Percentages = {key:round(val / Total_Votes*100,2) for key,val in Candidates_Votes.items()}
##
with open("c:\\Users\\Needra Pc\\python-challenge\\PyPoll\\Resources\\analysis.txt","w") as file_output:
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    file_output.write("Candidate Name: %s    " % voter_output)
    file_output.write ("\n")
    file_output.write("Total Votes: %s" % Total_Votes)
    file_output.write ("\n")
    file_output.write("Winning Candidate: %s" % Winning_Candidate)
    file_output.write ("\n")
    file_output.write("Candidates Votes: %s" % Candidates_Votes)
    file_output.write ("\n")
    file_output.write("Candidates Percentages : %s" % Candidates_Percentages)
##
    print("Candidate Name: %s    " % voter_output)
    print ("\n")
    print("Total Votes: %s" % Total_Votes)
    print ("\n")
    print("Winning Candidate: %s" % Winning_Candidate)
    print ("\n")
    print("Candidates Votes: %s" % Candidates_Votes)
    print ("\n")
    print("Candidates Percentages : %s" % Candidates_Percentages)    
 