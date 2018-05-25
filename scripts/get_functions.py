import requests

def get_player_summary (id, api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    try:
        data = requests.get( "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="+api_key+"&steamids="+id).json()
    except:
        return None
    return data["response"]["players"][0] 


def get_multiple_player_summary (ids, api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    request_str = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="+api_key+"&steamids="
    request_str += ",".join(ids)
    try:
        data = requests.get(request_str).json()
    except:
        return None
    return data["response"]["players"]


def get_multiple_player_bans (ids, api_key = "651624DDEE8476FED7FCA5264702440A"):
    request_str = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key="+api_key+"&steamids="
    request_str += ",".join(ids)
    #print(request_str)
    data = dict()
    try:
        data = requests.get(request_str).json()
        #print(data)
    except:
        #print(data)
        return None
    return data


def get_player_friends(pid, api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    try:
        data = requests.get( "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + api_key + "&steamid=" + str(pid) + "&relationship=friend").json()["friendslist"]["friends"]
    except KeyError:
        return []
    return data


def get_owned_games(pid,  api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    try:
        data = requests.get( "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&steamid=" + str(pid)).json()["response"]
    except KeyError:
        return []
    return data


def get_achievements_for_player_game(pid, appid,  api_key = "5F5DD2FA8A6C8646FCFE265C07BB90E5"):
    data = requests.get( "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=" + str(appid) + "&key=" + api_key + "&steamid=" + str(pid)).json()
    return data


def get_game_list(player_games):
    game_id_list = set()
    for player, data in player_games.items():
        try:
            for game in data["games"]:
                game_id_list.add(game["appid"])
        except:
            pass
    return sorted(list(game_id_list))



