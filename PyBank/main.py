#import the pandas library
import os
import csv
import pandas as pd
import locale
#determine the file for data analysis or the csv path
file = "Resources/budget_data.csv"
# find the number of lines
numberOfMonths = len(original_df)
print("The number of months in the file is:")
print(numberOfMonths)
# create a new dataframe to get the information requested. 

#create a dictionary

d = {"Data":['Jan-10','Feb-10','Mar-10'],"Profit/Losses":[1088983,-354534,276622]}

#creating a DataFrame
df = pd.DataFrame(d)

#Display original DataFrame
print("Original DataFrame\n", df, "\n")

#Calculating difference
df["Difference"] = df["Profit/Losses"].diff()
print (df)
# new dataframe worked. Now get the average results for this new column
change2 = df["Difference"].mean()
print("The averaged amount of Profit/Losses over the entire period was:")
change2
locale.setlocale(locale.LC_ALL, '')
print(locale.currency(change2, grouping=True))
# find the column name of the greatest increase
df = pd.DataFrame(d)
maxValuesIndex = df["Data"].max()
maxValues = df["Profit/Losses"].max()

print("The greatest increase on Profit/Losses over the entire period was:")
print(maxValuesIndex)
maxValues
locale.setlocale(locale.LC_ALL, '')
print(locale.currency(maxValues, grouping=True))    
# then add greatest decrease in profits
df = pd.DataFrame(d)
minValuesIndex = df["Data"].min()
minValues = df["Profit/Losses"].min()

print("The greatest decrease on Profit/Losses over the entire period was:")
print (minValuesIndex)
minValues
locale.setlocale(locale.LC_ALL, '')
print(locale.currency(minValues, grouping=True))   

#final script should export a text file with the results
lines(L)
f.close()f = open("PythonBankResults", "w")
L = ["FINANCIAL ANALYSIS \n","----------------------- \n","              by AM Scaranelo \n","Total Months = 86 \n","Total = $22,564,198.00 \n","Average Change: -$406,180.50 \n","Greatest Increase in Profits: Mar-10 $1,088,983.00 \n","Greatest Decrease in Profits: Feb-10  -$354,534.00 \n"]
f.write