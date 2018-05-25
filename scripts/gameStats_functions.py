import matplotlib.pyplot as plt
import numpy as np

def getMostCommonGamesAndHighestPlaytimeSorted( player_games):
	globalGamePlayTime=dict()
	numberOfPlayersForGame=dict()
	for user in player_games:
	    if(player_games[user]!={} and player_games[user]['game_count']!=0):
	        for game_info in player_games[user]["games"]:
	            if( game_info['appid'] not in globalGamePlayTime):
	                globalGamePlayTime[game_info['appid']]=game_info['playtime_forever']
	                numberOfPlayersForGame[game_info['appid']]=1
	            else:
	                globalGamePlayTime[game_info['appid']]+=game_info['playtime_forever']
	                numberOfPlayersForGame[game_info['appid']]+=1
	TopTotalPlaytime= sorted(globalGamePlayTime.items(), key=lambda x: x[1], reverse=True)
	TopBoughtGames= sorted(numberOfPlayersForGame.items(), key=lambda x: x[1], reverse=True)
	return (TopBoughtGames,TopTotalPlaytime)

def plotTopBoughtGames( sortedGames):
	games=[]
	playtimes=[]
	for game,playtime in sortedGames:
	    games.append(str(game))
	    playtimes.append(playtime/60)
	y_pos = np.arange(len(games))
	plt.figure(figsize=(15,25))
	plt.barh(games,playtimes, align='center', alpha=0.5)
	#plt.yticks(y_pos, games)
	plt.xlabel("Playtime in hours")
	plt.title('Št. ur za posamezno igro')
	plt.show()
	return None
