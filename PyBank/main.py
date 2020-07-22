import os
import csv

budget_csv = os.path.join("", "Resources", "budget_data.csv")
write_file = open(os.path.join("", "analysis", 'budgetOutput.txt'), 'w+')

# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    monthCount = 0
    netTotal = 0
    monthlyChange = []
    prevAmt = 0
    currAmt = 0
    changeAmt = 0
    greatestIncrease = 0
    greatestDecrease = 100000000
    greatestMonth = ""
    worstMonth = ""


    for row in csvreader:
        # Count months
        monthCount = monthCount + 1
    
        currAmt = int(row[1])
        netTotal = netTotal + int(row[1])
        if monthCount > 1:
            changeAmt = currAmt - prevAmt
            monthlyChange.append(changeAmt)
            if changeAmt > greatestIncrease :
                greatestIncrease = changeAmt
                greatestMonth = row[0]
            if changeAmt < greatestDecrease :
                greatestDecrease = changeAmt
                worstMonth = row[0]
        prevAmt = int(row[1])

    print ("```text")
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {monthCount}")
    print (f"Total: ${netTotal}")
    print (f"Average Change: ${round(sum(monthlyChange)/len(monthlyChange), 2)}")
    print (f"Greatest Increase in Profits: {greatestMonth} (${greatestIncrease})")
    print (f"Greatest Decrease in Profits: {worstMonth} (${greatestDecrease})")
    print ("```")

    write_file.write("```text\n")
    write_file.write("Financial Analysis\n")
    write_file.write("----------------------------\n")
    write_file.write(f"Total Months: {monthCount}\n")
    write_file.write(f"Total: ${netTotal}\n")
    write_file.write(f"Average Change: ${round(sum(monthlyChange)/len(monthlyChange), 2)}\n")
    write_file.write(f"Greatest Increase in Profits: {greatestMonth} (${greatestIncrease})\n")
    write_file.write(f"Greatest Decrease in Profits: {worstMonth} (${greatestDecrease})\n")
    write_file.write("```")

write_file.close() 

    