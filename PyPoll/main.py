#PyPoll analysis for election candidates
import os
import csv

#Voter ID,County,Candidate
#12864552,Marsh,Khan

def distinctValues(mylist2): 
        distinct_list = [] 
        for i in mylist2:  
            if i not in distinct_list: 
                distinct_list.append(i) 
        return distinct_list

def listCount(mylist, myStr): 
        list_count = 0
        #print(mylist)
        
        for i in mylist:  

            if i == myStr :
                #print(f"{myStr} and {list_count}")
                list_count = list_count + 1

        return list_count


voters_csv = os.path.join("", "Resources", "election_data.csv")
write_file = open(os.path.join("", "analysis", 'electionOutput.txt'), 'w+')

# Open and read csv
with open(voters_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    voteCount = 0
    candidates = []
    mydistinctcandidates = []
    candidateCount = []


    # Read through each row of data after the header
    for row in csvreader:
        # Count votes
        voteCount = voteCount + 1
        candidates.append(row[2])

    print ("```text")
    print ("Election Results")
    print ("----------------------------")
    print (f"Total Votes: {voteCount}")
    print ("----------------------------")

    write_file.write("```text\n")
    write_file.write("Election Results\n")
    write_file.write("----------------------------\n")
    write_file.write(f"Total Votes: {voteCount}\n")
    write_file.write ("----------------------------\n")

    countValue = 0
    mydistinctcandidates = distinctValues(candidates)
    loopcount = 0
    candidatePercent = 0
    winnerCount = 0
    winner = ""
    for j in mydistinctcandidates:
        countValue = listCount(candidates,mydistinctcandidates[loopcount])
        
        candidateCount.append(countValue)
        if winnerCount < candidateCount[loopcount] :
            winner = mydistinctcandidates[loopcount]
            winnerCount = candidateCount[loopcount] 

        candidatePercent = round((candidateCount[loopcount]/voteCount)*100, 3)

        print (f"{mydistinctcandidates[loopcount]}: {candidatePercent}%  ({candidateCount[loopcount]})")
        write_file.write (f"{mydistinctcandidates[loopcount]}: {candidatePercent}%  ({candidateCount[loopcount]})\n")

        loopcount = loopcount + 1
    
    
    #print(mydistinctcandidates)
    #print(candidateCount)
    print ("----------------------------")
    print (f"Winner: {winner}")
    print ("----------------------------")
    
    write_file.write  ("----------------------------\n")
    write_file.write  (f"Winner: {winner}\n")
    write_file.write  ("----------------------------\n")
    print  ("```")
    write_file.write ("```\n")
