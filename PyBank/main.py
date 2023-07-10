import csv
import os

# Create and load budget data csv file and file output "analysis"
file_input = os.path.join("PyBank","Resources", "budget_data.csv")
file_output = os.path.join("PyBank","Resources","analysis")
# Create financial parameters
total_months = 0
total_net= 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
# Read the csv then convert into list of dictionaries
with open(file_input) as financial_data:
    reader = csv.reader(financial_data)
    # Read the header row     Header row contains Date,Profit/Losses
    header = next(reader)
    # Extract first row to avoid appending to net_change_list  first row of data contains Jan-10,1088983
    first_row = next(reader)
    #init total_months + 1 to account for month of first row of data
    total_months = total_months + 1
    # add the first row to total net  = 1088983 from the Jan-10 ,1088983
    total_net = total_net + int(first_row[1])
    #Previous net is the first row 1088983 from the Jan-10 ,1088983
    prev_net = int(first_row[1])
    # use for loop to read through the rest of the data starting from row 
    # interate through row
    for row in reader:
        # Total Months
        total_months = total_months + 1
        # Total Net
        total_net = total_net + int(row[1])
        # Change in at the start of data, prev_net contained 108893 now compare prev_net to current int(row[1]) to get new value
        net_change = int(row[1]) - prev_net
        # set prev_net to  current row value for next comparison in the loop (Line 36) 
        prev_net = int(row[1])
        # set net change list  = net_change_list + [net-change]
        net_change_list = net_change_list + [net_change]
        # set month of change, month is the first position in row = [0], dictionar
        month_of_change = month_of_change + [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)