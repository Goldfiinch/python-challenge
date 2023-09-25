import os
import csv

cwd = os.getcwd()
csvpath = os.path.join("election_data.csv")

# Created null lists, one for all of the data and one for just the candidate names
data_list = []
name_list = []

# Reading the csv file and turning it into a list
with open(csvpath, encoding='utf') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    for row in election_data:
        data_list.append(row)
        #seperated the names from the ids in a seperate list
        name_list.append(row[2])

# Found the total number of votes minus the headers
nvotes = len(data_list)-1

# Had to remove "Candidates" header from name_list
name_list.remove("Candidate")

# Found the unique names in the list using the Set Method
list_set = set(name_list)
candidates = (list(list_set))

# Using For loops to determine vote count of each name
# Vote count for Raymon
Raymon_vote = 0
for i in name_list:
    if i == 'Raymon Anthony Doane' :
        Raymon_vote = Raymon_vote + 1

# Vote count for Charles
Charles_vote = 0
for i in name_list:
    if i == 'Charles Casper Stockham' :
        Charles_vote = Charles_vote + 1

# Vote count for Diana
Diana_vote = 0
for i in name_list:
    if i == 'Diana DeGette' :
        Diana_vote = Diana_vote + 1

# Calculate the decimal ratios of candidate votes to total votes, formatted as percentages

Raymon_Ratio = f"{Raymon_vote/nvotes: .3%}"
Charles_Ratio = f"{Charles_vote/nvotes: .3%}"
Diana_Ratio = f"{Diana_vote/nvotes: .3%}"

# Create a dictionary and assign name labels to the vote ratios. Using the max() and get() functions to find the Winner. 

votes = {'Raymon Anthony Doane': Raymon_Ratio, 'Charles Casper Stockham': Charles_Ratio, 'Diana DeGette': Diana_Ratio}

Winner = max(votes, key=votes.get)

# Printing the election results summary

election_results = (f'''
----------------------------
                    
Election Results

----------------------------
      
Total Votes: {nvotes}

----------------------------

Charles Casper STockham:{Charles_Ratio} ({Charles_vote})

Diana DeGette:{Diana_Ratio} ({Diana_vote})

Raymon Anthony Doane:{Raymon_Ratio} ({Raymon_vote})

---------------------------

Winner:{Winner}

---------------------------

''')

# Exporting results to text file
txtfile = open('election_results.txt', 'a')

txtfile.write(election_results)
txtfile.close()
    






    


        


