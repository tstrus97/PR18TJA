def fill_player_ids_rec(id, num = 1000, already_called = set()):
    global global_player_ids
    already_called.add(id)
    print("recursive call of id: " + id + "  len: " + str(len(global_player_ids)))
    try:
        if get_player_summary(id)["profilestate"] != 1:
            #print("not public")
            return None
    except KeyError:
        #print("not public key error")
        return None
    data = get_player_friends(id)
    tmp_id = set()
    for friend in data:
        if len(global_player_ids) >= num:
            print("enough friends")
            break
        tmp_id.add(friend["steamid"])
        global_player_ids.add(friend["steamid"])
        #print("len: "+ str(len(global_player_ids)))
        
    print("added my friends" + "  len: " + str(len(global_player_ids)))
    
    for playerid in tmp_id:
        if len(global_player_ids) >= num:
            break
        data = get_player_friends(playerid)
        for fof in data:
            if len(global_player_ids) >= num:
                print("enough friends")
                break
            global_player_ids.add(fof["steamid"])
        #print("added friends of friend")
            
    print("added friends of friends" + "  len: " + str(len(global_player_ids)))
    
    for playerid in tmp_id:
        if len(global_player_ids) >= num:
            print("enough friends")
            break
        if playerid not in already_called:
            fill_player_ids_rec(playerid, num, already_called)
    

def fill_player_summaries():
    global global_player_ids
    global players_summaries
    
    player_ids = list(global_player_ids)
    for i in range(0, len(player_ids)+1, 100):
        tmp_summaries = get_multiple_player_summary(player_ids[i-100:i])
        for summary in tmp_summaries:
            #summary["friends"] = get_player_friends(summary["steamid"])
            players_summaries[summary["steamid"]] = summary


def fill_player_bans():
    global global_player_ids
    global players_bans
    
    player_ids = list(global_player_ids)
    for i in range(0, len(player_ids)+1, 100):
        tmp_bans = get_multiple_player_summary(player_ids[i-100:i])
        for summary in tmp_bans:
            players_bans[summary["steamid"]] = summary
            
            

def fill_player_friends():
    global player_friends
    global global_player_ids
    global players_summaries
    for player in global_player_ids.keys():
        player_friends[player] = get_player_friends(player)
        print(len(player_friends))
    print("done")
    
    
def fill_player_games():
    global player_games
    for player_id in global_player_ids:
        player_games[player_id] = get_owned_games(player_id)
        
        
def fill_player_achievements():
    global player_achievements
    for player_id in global_player_ids:
        if len(player_games[player_id]) == 0:
            player_achievements[player_id] = dict()
        else:
            for game in player_games[player_id]['games']:
                gameid = game["appid"]
                gamedata = get_achievements_for_player_game(player_id, gameid)
                if player_id in player_achievements:
                    player_achievements[player_id]
                else:
                    player_achievements[player_id] = dict()
                    player_achievements[player_id][gameid] = gamedata