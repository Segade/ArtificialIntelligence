import pandas as pd 
import numpy as np 

# From the part 1 I fetch the dataset 
# There are two problems with the a.csv file. 
# the team names do not match with the season dataset. So, I copied the names from the season dataset and replace them 
# The author of the data of teams is wrong. He says that uses the 2019-20 season. However, there are three team names that don't match
# I don't know which season he is working with, as the team names are not relevant for the project at all, only the stats, I just replace the wrong team names for the correct ones.
# Mallorca for girona, Real Vallecano for Granada and Huesca for Osasuna
# I create the teams.csv file with the correct team names 
# the a.csv file must be modified with the valid team names manually 
df = pd.read_csv("new_season.csv")
df1 = pd.read_csv("a.csv")
all_teams = pd.read_csv("teams.csv")
# I fetch the column witht he correct team names 
teams = all_teams["0"]

# I iterate each team 
# when the team is the Home team, I change the columns corresponding to the Home team. the fields with the "H" in front 
# When the team is the Away team, I do the same for the corresponding columns with the "A" in front 
# I get the index where the team is located 
# I know that there are 150 columns for the Home team, and obviously for the Away team as well.
# for the Home team, I added from the column 10 up to 160 
# for the Away team, from the 161 up to the 310
# df1b contains the data for the team 
for t in teams:
# Home teams 
	criteria = df["HomeTeam"] == t
	myRows = df[criteria].index

	criteria = df1["team"] == t
	df1b = df1[criteria]
 
	for x in range (1, 151):
 		df.iloc[myRows, 9+x] = df1b.iloc[0,x]
 
# Away teams
	criteria = df["AwayTeam"] == t
	myRows = df[criteria].index
	criteria = df1["team"] == t
	df1b = df1[criteria]
 
	for x in range (1, 151):
 		df.iloc[myRows, 159+x] = df1b.iloc[0,x]



# As the result of the match is a letter, I change it for a number 
# Draw = 0, Home = 1, Away = 2
criteria = df["FTR"] =="H"
myRows = df[criteria].index
df.iloc[myRows, 6] = "1"

criteria = df["FTR"] =="D"
myRows = df[criteria].index
df.iloc[myRows, 6] = "0"

criteria = df["FTR"] =="A"
myRows = df[criteria].index
df.iloc[myRows, 6] = "2"



# I create the final dataset, which I will work with with the algorithms 
print(df.iloc[:,6])
df.to_csv("result.csv", index=False)

