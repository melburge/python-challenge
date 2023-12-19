import os
import csv

# Path where the file is located
budget_data_csv = os.path.join("../PyBank/Resources/budget_data.csv")
print(budget_data_csv)
# Create Variables and lists
print(budget_data_csv)
total_months = []
total_pl = []
pl_changes = []
avg_changes = []
date =[]

# Open the file in read only mode'
with open (budget_data_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

    # Loop through the columns to get months
    for row in csvreader:
        total_months.append(row[0])
        total_pl.append(int(row[1]))
        date.append(row[0])
    
    # Loop through columns to get totals
    for pl in range(1, len(total_pl)):
        pl_changes.append(int(total_pl[pl])- int(total_pl[pl-1]))

    # Average Changes    
    avg_changes = sum(pl_changes) / len(pl_changes)
    
    # Create variables to store values and format
    gtinc = max(pl_changes)
    gtdec = min(pl_changes)
    gtincdt = date[pl_changes.index(gtinc) + 1] 
    gtdecdt = date[pl_changes.index(gtdec)+ 1]

    # Print the outcomes
    print(" ")
    print("Financial Analysis")
    print(" ")
    print("------------------")
    print(" ")
    print(f"Total Months:  {len(total_months)}")
    print(" ")
    print(f"Total:  ${sum(total_pl)}")
    print(" ")
    print(f"Average Change:  ${round(avg_changes, 2)}")
    print(" ")
    print(f"Greatest Increase in Profits: {gtincdt}  (${gtinc})")
    print(" ")
    print(f"Greatest Decrease in Profits: {gtdecdt}  (${gtdec})")
    print(" ")

# Print Financial Anlysis to text file
text = (" ", "Financial Analysis",
" ",
"------------------",
" ",
f"Total Months:  {len(total_months)}",
" ",
f"Total:  ${sum(total_pl)}",
" ",
f"Average Change:  ${round(avg_changes, 2)}",
" ",
f"Greatest Increase in Profits: {gtincdt}  (${gtinc})",
" ",
f"Greatest Decrease in Profits: {gtdecdt}  (${gtdec})",
" ")

with open('../PyBank/analysis/textfile.txt', 'w') as f:
    for line in text:
        f.write(line)
        f.write('\n')








    