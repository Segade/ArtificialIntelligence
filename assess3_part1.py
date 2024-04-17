import numpy as np
import pandas as pd


df = pd.read_csv("laliga_player_stats_english.csv")
df1 = pd.read_csv("LaLiga_Matches.csv")
season = pd.DataFrame()
 
# I discard the players with less than 1000 minutes played 
# The person who created this dataset must be spanish because he uses the point to separate the thousands values
# So, I replace the points for a non space 
df["Minutes played"] = df["Minutes played"].astype(str)
df["Minutes played"] = df["Minutes played"].str.replace('.', '').astype(int)

criteria = df["Minutes played"] > 1000
df = df[criteria]
 

# I pick all the team names and delete the duplication to have the list of the teams 
teams = df["Team"]
teams = teams.drop_duplicates()
all_cols = []
 
h_cols = []
a_cols = []

# *********
 
 
season["team"] = teams

# I delete the columns I won't use in the project
df_copy = df
# the list of the columns I don't want to
c = ["Team", "Position", "Shirt number", "Name", "Minutes played", "Percentage of games played", "Full games played", "Percentage of full games played", "Games started", "Percentage of games started", "Games where substituted", "Percentage of games where substituted" ]
# the dataset now just has the valid columns 
df_copy = df_copy.drop(c, axis=1)

# I pick the columns I will use in the project 
cols = df_copy.columns
# I iterate the list of the columns 
for col in cols:
# I initialise  the arrays that will store the values for each defender, midfield and forward 
	defender_stats = []
	midfield_stats = []
	forward_stats = []  

# I iterate each team data 
	for t in teams: 
# I initialise the variable that will be appended to the corresponding array 
		defender = 0
		midfield = 0
		forward = 0
# for all the defenders for the current team  in the loop 
# I sum all the values and add the result to the array 
		criteria = (df["Position"] == "Defender") & (df["Team"] == t)
		df3 = df[criteria]
		defender = np.sum(df3[col])
		defender_stats.append(defender)

# The same process as below, but for the midfield  
		criteria = (df["Position"] == "Midfielder") & (df["Team"] == t)
		df3 = df[criteria]
		midfield = np.sum(df3[col])
		midfield_stats.append(midfield)

# The same process as below, but for the forward 
		criteria = (df["Position"] == "Forward") & (df["Team"] == t)
		df3 = df[criteria]
		forward = np.sum(df3[col])
		forward_stats.append(forward)

# variable with the name of the new column in the new dataset 
	defender_col = col + " defender"	
	midfield_col = col + " midfielder"
	forward_col = col + " forward"

# I add a new column to the dataset along with the name and the values 
# I add column by column 
# the new column already has all the values for each team
	season[defender_col] = defender_stats
	season[midfield_col] = midfield_stats
	season[forward_col] = forward_stats
# I initialise a variable with all the new columns 
	all_cols.append(defender_col)
	all_cols.append(midfield_col)
	all_cols.append(forward_col)



####### 

# I initialise an array  that will store the new columns for the Home team and Away team 
season_cols = [] 

# I iterate all the new columns created previously 
# The Home team and Away team will have the same fields, but to differenciate them in the dataset, the H or A is added 
# The array will store the columns adding H or A depending for the Home team and Away team 
for a in all_cols:
	season_cols.append("H " + a)
	h_cols.append("H " + a)


for a in all_cols:
	season_cols.append("A " + a)
	a_cols.append("A " + a)

# I add all the new columns for the Home team and Away team 
for c in season_cols:
	df1[c] = np.nan
 
# I filter for the 2019-20 season. The season I will work with 
criteria = df1["Season"] == "2019-20"
df3 = df1[criteria]

# I create the csv file  
df3.to_csv("new_season.csv", index=False)
 
 
#df3.iloc[rows_change, 11] = 99
 # I create the csv file with the data for each team 
season.to_csv("a.csv", index=False)