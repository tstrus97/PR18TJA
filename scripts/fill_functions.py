from scripts.get_functions import *
from scripts.async_req import *
import json


def fill_player_ids_rec(pid, player_ids, num = 1000, already_called = set()):
    already_called.add(pid)
    #print("recursive call of id: " + str(pid) + "  len: " + str(len(player_ids)))
    try:
        if get_player_summary(pid)["profilestate"] != 1:
            #print("not public")
            return None
    except KeyError:
        #print("not public key error")
        return None
    data = get_player_friends(pid)
    tmp_id = set()
    for friend in data:
        if len(player_ids) >= num:
            #print("enough friends")
            break
        tmp_id.add(friend["steamid"])
        player_ids.add(friend["steamid"])
        #print("len: "+ str(len(player_ids)))
        
    #print("added my friends" + "  len: " + str(len(player_ids)))
    
    for playerid in tmp_id:
        if len(player_ids) >= num:
            break
        data = get_player_friends(playerid)
        for fof in data:
            if len(player_ids) >= num:
                #print("enough friends")
                break
            player_ids.add(fof["steamid"])
        #print("added friends of friend")
            
    #print("added friends of friends" + "  len: " + str(len(player_ids)))
    
    for playerid in tmp_id:
        if len(player_ids) >= num:
            print("enough friends")
            break
        if playerid not in already_called:
            fill_player_ids_rec(playerid, player_ids, num, already_called)
    return player_ids
    

def fill_player_summaries(player_ids, player_summaries = dict()):
    player_ids = list(player_ids)
    for i in range(100, len(player_ids)+1, 100):
        tmp_summaries = get_multiple_player_summary(player_ids[i-100:i])
        for summary in tmp_summaries:
            #summary["friends"] = get_player_friends(summary["steamid"])
            player_summaries[summary["steamid"]] = summary
    return player_summaries


def fill_player_bans(player_ids, player_bans = dict()):
    player_ids = list(player_ids)
    for i in range(100, len(player_ids)+1, 100):
        tmp_bans = get_multiple_player_bans(player_ids[i-100:i])
        #print("bans: ")
        #print(tmp_bans)
        try:
            for summary in tmp_bans["players"]:
                player_bans[summary["SteamId"]] = summary
        except:
            pass
    return player_bans
                        


def fill_player_friends(player_ids, player_friends = dict(), api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    urls = []
    odered_ids = sorted(player_ids)
    for i in range(len(odered_ids)):
        urls += ["http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + api_key + "&steamid=" + str(odered_ids[i]) + "&relationship=friend"]
    responses = async_request(urls)
    for i in range(len(odered_ids)):
        try:
            player_friends[odered_ids[i]] =  json.loads(str(responses[i]).strip("b").strip("'"))["friendslist"]["friends"]
        except:
            player_friends[odered_ids[i]] = []
    return player_friends
    
    
def fill_player_games(player_ids, player_games = dict(), api_key = "EEA36ABA0BB06BBFC90ECF96B503007E"):
    urls = []
    odered_ids = sorted(player_ids)
    for i in range(len(odered_ids)):
        urls += ["http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&steamid=" + str(odered_ids[i])]
    responses = async_request(urls)
    #print(urls[0])
    #print(responses[0])
    for i in range(len(odered_ids)):
        try:
            player_games[odered_ids[i]] =  json.loads(str(responses[i]).strip("b").strip("'"))["response"]
        except:
            player_games[odered_ids[i]] = []
    return player_games
        

def fill_player_achievements(player_ids, player_games, player_achievements = dict(), api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    urls = []
    sorted_ids = sorted(player_ids)
    for player_id in sorted_ids:
        if len(player_games[player_id]) == 0:
            player_achievements[player_id] = dict()
        else:
            for game in player_games[player_id]['games']:
                gameid = game["appid"]
                urls+=["http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=" + str(gameid) + "&key=" + api_key + "&steamid=" + str(player_id)]
    #print("urls created")
    responses = async_request(urls)
    i = 0;
    for player_id in sorted_ids:
        if len(player_games[player_id]) == 0:
            player_achievements[player_id] = dict()
        else:
            player_achievements[player_id] = dict()
            for game in player_games[player_id]['games']:
                gameid = game["appid"]
                player_achievements[player_id][gameid] = responses[i]
                i+=1
                
    return player_achievements

def fill_global_game_stats(game_ids, global_game_stats = dict()):
    urls = []
    for appid in game_ids:
        urls+= ["http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid="+str(appid)]
    responses = async_request(urls)
    for i in range(len(responses)):
        try:
            global_game_stats[game_ids[i]] = json.loads(str(responses[i]).strip("b").strip("'").replace("\\","\\\\"))["achievementpercentages"]["achievements"]
        except:
            pass
    return global_game_stats

def fill_game_names(game_names = dict()):
    data = get_game_names()
    for info in data["applist"]["apps"]["app"]:
        id, name = info.values()
        game_names[id] = name
    return game_names