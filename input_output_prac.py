# Import the csv module in order to read in the txt file
import csv
# Make a blank list called environment - think of this as the "wrapping paper"
environment = []
# Create a new label called "f" and open the txt file containing the data
f = open('in.txt', newline='') 
# Use the csv reader function within the csv module to open the file
# Non-numeric converts the integers into floats
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# Set a loop - for every row in the file
for row in reader:
# Create a blank list called rowlist within this first loop - think of this as the
# "photo book"			
    rowlist = []
# Create a new loop within the first that appends every value within the row to the 
# rowlist - think of the values as the "Pictures" 
    for value in row:				
        rowlist.append(value)
# Once each value has been appended to a row within the rowlist, append each rowlist to
# the environment
# Note - this is indented one BEFORE the second loop and is therefore in-line with the
# original loop - this is because we want each rowlist to be added to the environment
# only once the rowlist has been processed
    environment.append(rowlist)
f.close()
print(environment)

# Note - the order in which this is done can be compared to giving a photobook to your Mum.
# The empty wrapping paper is purchased (the empty environment list)
# The blank photobook is purchased (the empty rowlist)
# Photos are added into the each page of the photobook (every value in the row is added
# to a new rowlist)
# Only once the photobook is completed, (the rows have all been processed with its values)
# do we wrap it (add it to the environment)