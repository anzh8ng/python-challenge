#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import csv


# In[30]:


# Path to collect data from the Resources folder
wwe_csv = os.path.join("..","Resources","WWE-Data-2016.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter

def print_percentages(wrestlerData):

# Find the total number of matches wrestled
    TotalMatches = int(wrestlerData[1])+int(wrestlerData[2])+int(wrestlerData[3]))
# Find the percentage of matches won
    MatchesWon = ((int(wrestlerData[1])/TotalMatches)*100)
# Find the percentage of matches lost
    MatchesLost = ((int(wrestlerData[2])/TotalMatches)*100)
# Find the percentage of matches drawn
    MatchesDraw = ((int(wrestlerData[3])/TotalMatches)*100)
# Print out the wrestler's name and their percentage stats
    print(f'Name: {wrestlerData[0]}')
    print(f'Matches Won: {MatchesWon}')
    print(f'Matches Lost: {MatchesLost}')
    print(f'Matches Drawn: {MatchesDraw}')
    
    if MatchesLost > 50:
        print(f"{wrestlerData[0]} is a Superstar.")
    elif MatchesLost <= 50:
            print(f"{wrestlerData[0]} is a Jobber.")
    


# In[31]:


# Read in the CSV file
with open(wwe_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)


# In[ ]:




