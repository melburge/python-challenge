import os
import csv


# Path where the file is located
election_data_csv = os.path.join("../PyPoll/Resources/election_data.csv")

# Create Variables and lists

total_votes_cast = []
candidates = []
candidate_votes = []
candidate_list = {}
total_votes = 0
winner_count = 0


# Open the file in read only mode'
with open (election_data_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    csv_header = next(csvreader)

 # Loop through the columns to get votes cast per candidate and totals
    for row in csvreader:
            
       total_votes = total_votes + 1
       candidate = row[2]
       if candidate not in candidate_list:
           candidate_list[candidate] = 1
       else:
           candidate_list[candidate] = candidate_list[candidate] + 1



    # print(total_votes, candidate_list)
    print(" ")
    print("Elction Results")
    print(" ")
    print("------------------")
    print(" ")
    print(f"Total Votes:  {total_votes}")
    print(" ")
    print("------------------")
    print(" ")

    for c, v in candidate_list.items():
        print(f"{c}: {round(v/total_votes*100, 3)}%  ({v})")
print("")
print("------------------")
print("")
print(f"Winner: {max(candidate_list, key=candidate_list.get)}")
print("")
print("------------------")

# Print to text file
text = (" ", "Election Results",
" ", 
"------------------", 
" ",
f"Total Votes:  {total_votes}",
" ", 
"-------------------",
f"{c}: {round(v/total_votes*100, 3)}%  ({v})",
"",
f"{c}: {round(v/total_votes*100, 3)}%  ({v})",
"", 
f"{c}: {round(v/total_votes*100, 3)}%  ({v})",
"",
"------------------",
"", 
f"Winner: {max(candidate_list, key=candidate_list.get)}",
"",
"------------------")



with open('../PyPoll/analysis/textfile.txt', 'w') as f:
    for line in text:
        f.write(line)
        f.write('\n')


   