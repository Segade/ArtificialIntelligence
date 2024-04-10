import numpy as np
import pandas as pd


df = pd.read_csv("laliga_player_stats_english.csv")
df1 = pd.read_csv("LaLiga_Matches.csv")
season = pd.DataFrame()
 
 
df["Minutes played"] = df["Minutes played"].astype(str)
df["Minutes played"] = df["Minutes played"].str.replace('.', '').astype(int)

criteria = df["Minutes played"] > 1000
df = df[criteria]
#df = df[[ "Team", "Position", "Red Cards", "Goals scored", "Penalties scored", "Successful tackles", "Successful duels", "Successful aerial challenges", "Fouls committed", "Goals scored per attempt"]]


teams = df["Team"]
 
teams = teams.drop_duplicates()

# *********
#	col = df.columns get all column names
# use df.drop to remove columns I wont; use 
# new stat defense colum = []
# new stat field column ]]
# new  attack stat = [] 
 # for each team 
# for each player  teams players = df["team nname = 
# ndefense stats = 0 mildfilestats= 0 attackstats= 0
# for each   column name for all comumns
# defensestats = np.sum(teamsplayers[columanname] where teamsplayers["position"] = defense 
# new stat defense column .append(defense stats)


season["team"] = teams

#for t in teams:
#criteria = df["Team"] == t
#df2 = df[criteria]

df_copy = df
c = ["Team", "Position", "Shirt number", "Name", "Minutes played", "Percentage of games played", "Full games played", "Percentage of full games played", "Games started", "Percentage of games started", "Games where substituted", "Percentage of games where substituted" ]
df_copy = df_copy.drop(c, axis=1)
cols = df_copy.columns
 
for col in cols:
	defender_stats = []
	midfield_stats = []
	forward_stats = []  


	for t in teams: 
 
		defender = 0
		midfield = 0
		forward = 0

		criteria = (df["Position"] == "Defender") & (df["Team"] == t)
		df3 = df[criteria]
		defender = np.sum(df3[col])
		defender_stats.append(defender)
 
		criteria = (df["Position"] == "Midfielder") & (df["Team"] == t)
		df3 = df[criteria]
		midfield = np.sum(df3[col])
		midfield_stats.append(midfield)

		criteria = (df["Position"] == "Forward") & (df["Team"] == t)
		df3 = df[criteria]
		forward = np.sum(df3[col])
		forward_stats.append(forward)
	defender_col = col + " defender"	
	midfield_col = col + " midfielder"
	forward_col = col + " forward"
	season[defender_col] = defender_stats
	season[midfield_col] = midfield_stats
	season[forward_col] = forward_stats
 


#print("defender " , defender_stats)

season.to_csv("a.csv", index=False)