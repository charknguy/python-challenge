import os
import csv



csvpath = os.path.join('election_data_2.csv')



with open(csvpath, newline = '') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ',')

	
	headerline = next(csvreader)
	

	for row in csvreader:
		
		num_Votes = list(csvreader)
		total_Votes = len(num_Votes)
		

	
	print("Election Results")
	print("------------------")
	print("Total Votes: " + str(total_Votes))
	

	




