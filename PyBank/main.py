import os
import csv



csvpath = os.path.join('budget_data_1.csv')



with open(csvpath, newline = '') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ',')

	
	headerline = next(csvreader)
	total_Revenue = 0

	for row in csvreader:
		
		total_Revenue += int(row[1])
		numMonths = list(csvreader)
		row_count = len(numMonths)

		average_Change = (total_Revenue/row_count)
	
	print("Finacial Analysis")
	print("------------------")
	print("Total Months: " + str(row_count))
	print("Total Revenue: " + str(total_Revenue)) 
	print("Average Revenue Change: " + str(average_Change))

	




