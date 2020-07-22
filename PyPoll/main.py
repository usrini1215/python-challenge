#PyPoll analysis for election candidates
import os
import csv

#Voter ID,County,Candidate
#12864552,Marsh,Khan


voters_csv = os.path.join("", "Resources", "election_data.csv")
write_file = open(os.path.join("", "analysis", 'electionOutput.txt'), 'w+')

# Open and read csv
with open(voters_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    voteCount = 0

    # Read through each row of data after the header
    for row in csvreader:
        # Count votes
        voteCount = voteCount + 1


    
    print ("```text")
    print ("Election Results")
    print ("----------------------------")
    print (f"Total Votes: {voteCount}")
    print ("----------------------------")
    print ("```")

    write_file.write("```text\n")
    write_file.write("Election Results\n")
    write_file.write("----------------------------\n")
    write_file.write(f"Total Votes: {voteCount}\n")
    write_file.write ("----------------------------\n")
    write_file.write ("```")