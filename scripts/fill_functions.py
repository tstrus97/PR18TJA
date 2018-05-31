from scripts.get_functions import *
from scripts.async_req import *
import json


def fill_player_ids_rec(pid, player_ids, num = 1000, already_called = set()):
    already_called.add(pid)
    print("recursive call of id: " + str(pid) + "  len: " + str(len(player_ids)))
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
            compressed = dict()
            try:
                compressed["cvs"]= summary["communityvisibilitystate"]
            except:
                pass
            try:
                compressed["cntry"]= summary["loccountrycode"]
            except:
                pass
            try:
                compressed["name"]= summary["personaname"]
            except:
                pass
            try:
                compressed["pcid"]= summary["primaryclanid"]
            except:
                pass
            try:
                compressed["ps"]= summary["profilestate"]
            except:
                pass
            try:
                compressed["rn"]= summary["realname"]
            except:
                pass
            try:
                compressed["tc"]= summary["timecreated"]
            except:
                pass
            try:
                player_summaries[summary["steamid"]] = compressed
            except:
                pass
    return player_summaries


def fill_player_bans(player_ids, player_bans = dict()):
    player_ids = list(player_ids)
    for i in range(100, len(player_ids)+1, 100):
        tmp_bans = get_multiple_player_bans(player_ids[i-100:i])
        #print("bans: ")
        #print(tmp_bans)
        try:
            for ban in tmp_bans:
                compressed  = dict()
                compressed["id"] = ban["SteamId"]
                compressed["cb"] = ban["CommunityBanned"]
                compressed["vacb"] = ban["VACBanned"]
                compressed["novacb"] = ban["NumberOfVACBans"]
                compressed["dslb"] = ban["DaysSinceLastBan"]
                compressed["nogb"] = ban["NumberOfGameBans"]
                compressed["eb"] = ban["EconomyBan"]
                player_bans[ban["SteamId"]] = compressed
        except:
            pass
    return player_bans
                        


def fill_player_friends(player_ids, player_friends = dict(), api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    urls = []
    ordered_ids = sorted(player_ids)
    for i in range(len(ordered_ids)):
        urls += ["http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + api_key + "&steamid=" + str(ordered_ids[i]) + "&relationship=friend"]
    responses = async_request(urls)
    for i in range(len(ordered_ids)):
        try:
            compressed = dict()
            data  =  json.loads(str(responses[i]).strip("b").strip("'"))["friendslist"]["friends"]
            frnds = []
            for frnd in data:
                compressed = dict()
                try:
                    compressed["fs"] = frnd["friend_since"]
                except:
                    pass
                try:
                    compressed["id"] = frnd["steamid"]
                except:
                    pass
                frnds += [compressed]
            player_friends[ordered_ids[i]] = compressed
        except Exception as e:
            #print("{} {}".format(type(e).__name__, e))
            player_friends[ordered_ids[i]] = dict()
    return player_friends
    
    
def fill_player_games(player_ids, player_games = dict(), api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    urls = []
    ordered_ids = sorted(player_ids)
    for i in range(len(ordered_ids)):
        urls += ["http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&steamid=" + str(ordered_ids[i])]
    responses = async_request(urls)
    #print(urls[0])
    #print(responses[0])
    for i in range(len(ordered_ids)):
        try:
            data = json.loads(str(responses[i]).strip("b").strip("'"))["response"]
            if ordered_ids[i] not in player_games or len(data) > len(player_games[ordered_ids[i]]):
                player_games[ordered_ids[i]] = data
        except:
            player_games[odrered_ids[i]] = []
    return player_games
        

def fill_player_achievements(player_ids, player_games, player_achievements = dict(), api_key = "EEA36ABA0BB06BBFC90ECF96B503007E"):
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
                try:
                    gameid = game["appid"]
                    data =  json.loads(str(responses[i]).strip("b").strip("'").replace("\\","\\\\").replace("\\\\\"","\\\""))
                    if len(data) > 0:
                         player_achievements[player_id][gameid] = data
                except:
                    pass
                i+=1
                
    return player_achievements

def fill_global_game_stats(game_ids, global_game_stats = dict()):
    urls = []
    for appid in game_ids:
        urls+= ["http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid="+str(appid)]
    responses = async_request(urls)
    for i in range(len(responses)):
        try:
            global_game_stats[game_ids[i]] = json.loads(str(responses[i]).strip("b").strip("'").replace("\\","\\\\").replace("\\\\\"","\\\""))["achievementpercentages"]
        except Exception as e :
            #print(e)
            #print(str(responses[i]).strip("b").strip("'"))
            global_game_stats[game_ids[i]] = dict()
            pass
    return global_game_stats

def fill_game_names(game_names = dict()):
    data = get_game_names()
    for info in data["applist"]["apps"]["app"]:
        id, name = info.values()
        game_names[id] = name
    return game_names


def filled_p(var):
    filled = 0;
    for data in var.values():
        if len(data) != 0:
            filled += 1
    print("Currently:", filled, "out of", len(var))