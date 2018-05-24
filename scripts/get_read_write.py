from scripts.fill_functions import *
import json
import time

#--------------------------------------------------------- REQUEST FROM API -----------------------------------------------------

def request_all_from_api(num = 100):
    api_fill_player_ids(num)
    api_fill_player_summaries()
    api_fill_player_friends()
    api_fill_player_games()
    api_fill_player_achivements()
    api_fill_player_bans()

    
def api_fill_player_ids(num = 100, my_id = "76561198101569818", player_ids = set()):
    print("INFO: requesting ids")
    start_time = time.time()
    data = fill_player_ids_rec(my_id, player_ids, num)
    print("INFO: requesting ids finished")
    print("Time needed: {} seconds ".format((time.time() - start_time)))
    return data


def api_fill_player_summaries(player_summaries = dict()):
    print("INFO: requesting summaries")
    data = fill_player_summaries(player_summaries)
    print("INFO: requesting summaries finished")
    return data
    
    
def api_fill_player_friends(player_friends = dict()):
    print("INFO: requesting friends")
    data = fill_player_friends()
    print("INFO: requesting friends finished")
    return data


def api_fill_player_games(player_games = dict()):
    print("INFO: requesting games")
    data = fill_player_games()
    print("INFO: requesting games finished")
    return data


def api_fill_player_achievements(player_achievements = dict()):
    print("INFO: requesting achievements")
    data = fill_player_achievements()
    print("INFO: requesting achievements finished")
    return data
    

def api_fill_player_bans(player_bans = dict()):
    print("INFO: requesting bans")
    data = fill_player_bans()
    print("INFO: requesting bans finished")
    return data

#--------------------------------------------------------- REQUEST FROM FILE -----------------------------------------------------

def request_all_from_file():
    file_fill_player_ids()
    file_fill_player_summaries()
    file_fill_player_friends()
    file_fill_player_games()
    file_fill_player_achievements()
    file_fill_player_bans()
    

def file_fill_player_ids():
    print("INFO: reading ids")
    with open("data/pid_set.json", "r") as fp:
        data = (json.load(fp))
    print("INFO: reading ids finished")
    return data
    
    
def file_fill_player_summaries():
    print("INFO: reading summaries")
    with open("data/player_summaries.json", "r") as fp:
        data = json.load(fp)
    print("INFO: reading summaries finished")
    return data

    
def file_fill_player_friends():
    print("INFO: reading friends")
    with open("data/player_friends.json", "r") as fp:
        data = json.load(fp)
    print("INFO: reading friends finished")
    return data
        
    
def file_fill_player_games():
    print("INFO: reading games")
    with open("data/player_games.json", "r") as fp:
        data = json.load(fp)
    print("INFO: reading games finished")
    return data

    
def file_fill_player_achievements():
    print("INFO: reading achievements")
    with open("data/player_achievements.json", "r") as fp:
        data = json.load(fp)
    print("INFO: reading achievements finished")
    return data

        
def file_fill_player_bans():
    print("INFO: reading bans")
    with open("data/player_bans.json", "r") as fp:
        data = json.load(fp)
    print("INFO: reading bans finished")
    return data


#--------------------------------------------------------- WRITE TO FILES -----------------------------------------------------
 
def write_all_to_file():
    write_player_ids()
    write_player_summaries()
    write_player_friends()
    write_player_games()
    write_player_achivements()
    write_player_bans()
    
    
def write_player_ids(player_ids):
    print("INFO: writing ids")
    with open("data/pid_set.json", "w") as fp:
        json.dump(list(player_ids), fp)
    print("INFO: finised writing ids")
    
    
def write_player_summaries(player_summaries):
    print("INFO: writing summaries")
    with open("data/player_summaries.json", "w") as fp:
        json.dump(players_summaries, fp)
    print("INFO: finised writing summaries")
    
        
def write_player_friends(player_friends):
    print("INFO: writing friends")
    with open("data/player_friends.json", "w") as fp:
        json.dump(player_friends, fp)
    print("INFO: finised writing friends")
    
    
def write_player_games(player_games):
    print("INFO: writing games")
    with open("data/player_games.json", "w") as fp:
        json.dump(player_games, fp)
    print("INFO: finised writing games")
        
def write_player_achievements(player_achievements):
    print("INFO: writing achievements")
    with open("data/player_achievements.json", "w") as fp:
        json.dump(player_achievements, fp)
    print("INFO: finised writing acievements")
        
def write_player_bans(player_bans):
    print("INFO: writing bans")
    with open("data/player_bans.json", "w") as fp:
        json.dump(player_bans, fp)
    print("INFO: finised writing bans")
    