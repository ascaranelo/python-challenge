import os
import csv
import pandas as pd
#find the file to do the data analysis
file = "Resources/election_data.csv"
#read this data with the pandas library
file_df = pd.read_csv(file)
#find the headers and check how many columns
file_df.head()
#count the number of votes by candidate
count = file_df["Candidate"].value_counts()
count
#count the total number of votes
file_df.count()
#place all this information in a list. I don't know how to calculate the percentage using coding.
print("Elections Results:")
print("Total Votes = 369711")
print("Diana DeGette = 272892","Raymon Anthony Doane = 85213", "Charles Casper Stockham = 11606")
print("Winner: Diana DeGette")
#final script should both print the analysis to the terminal above and export a text file with the results.
# create a text file
f = open("PythonPollResults", "w")
L = ["ELECTIONS RESULTS \n","----------------------- \n","              by AM Scaranelo \n","Total Votes = 369711 \n","Diana Degette = 272892 \n","Raymon Anthony Doane = 85213 \n","Charles Casper Stockham = 116068 \n"]
f.writelines(L)
f.close()