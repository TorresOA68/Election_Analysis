# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)


# Assign a variable for the file to load and the path.
file_to_load = '/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv'


# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()


# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

    # Write three counties to the file.
     txt_file.write("Arapahoe")
     txt_file.write("Denver")
     txt_file.write("Jefferson")
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources" , "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
   # Print each row in the CSV file.
    for row in file_reader:
        print(row)

       # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        
# -*- coding: utf-8 -*-
import csv
import os
file_to_load = os.path.join("Resources", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/Resources/election_results.csv")

file_to_save = os.path.join("analysis", "/Users/johanaherrera/Desktop/Analysis_Data/Election_Analysis/analysis/election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {} # key: name of the candidate => value : total votes for that candidate
with open(file_to_load) as election_data:
	file_reader = csv.reader(election_data)	
	headers = next(file_reader)
	for row in file_reader:
		total_votes += 1
		candidate_name = row[2]
		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name] = 0
		candidate_votes[candidate_name] += 1

print("Total Votes: " + str(total_votes))
for c in candidate_options:
	print("Votes for " + c + ": " + str(candidate_votes[c]))

