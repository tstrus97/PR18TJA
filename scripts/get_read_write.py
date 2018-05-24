from scripts.fill_functions import *
import json

#--------------------------------------------------------- REQUEST FROM API -----------------------------------------------------

def request_all_from_api(num = 100):
    api_fill_player_ids(num)
    api_fill_player_summaries()
    api_fill_player_friends()
    api_fill_player_games()
    api_fill_player_achivements()
    api_fill_player_bans()

    
def api_fill_player_ids(my_id = "76561198101569818",num = 100, player_ids = set()):
    return fill_player_ids_rec(my_id, player_ids, num)

def api_fill_player_summaries(player_summaries = dict()):
    return fill_player_summaries(player_summaries)
    
def api_fill_player_friends(player_friends = dict()):
    return fill_player_friends()

def api_fill_player_games(player_games = dict()):
    return fill_player_games()

def api_fill_player_achievements(player_achievements = dict()):
    return fill_player_achievements()
    
def api_fill_player_bans(player_bans = dict()):
    return fill_player_bans()

#--------------------------------------------------------- REQUEST FROM FILE -----------------------------------------------------

def request_all_from_file():
    file_fill_player_ids()
    file_fill_player_summaries()
    file_fill_player_friends()
    file_fill_player_games()
    file_fill_player_achievements()
    file_fill_player_bans()

def file_fill_player_ids():
    with open("data/pid_set.json", "r") as fp:
        return (json.load(fp))
    
def file_fill_player_summaries():
    with open("data/player_summaries.json", "r") as fp:
        return json.load(fp)
    
def file_fill_player_friends():
    with open("data/player_friends.json", "r") as fp:
        return json.load(fp)

def file_fill_player_games():
    with open("data/player_games.json", "r") as fp:
        return json.load(fp)
    
def file_fill_player_achievements():
    with open("data/player_achievements.json", "r") as fp:
        return json.load(fp)
        
def file_fill_player_bans():
    with open("data/player_bans.json", "r") as fp:
        return json.load(fp)

#--------------------------------------------------------- WRITE TO FILES -----------------------------------------------------
 
def write_all_to_file():
    write_player_ids()
    write_player_summaries()
    write_player_friends()
    write_player_games()
    write_player_achivements()
    write_player_bans()
    
    
def write_player_ids(player_ids):
    with open("data/pid_set.json", "w") as fp:
        json.dump(list(player_ids), fp)
    
def write_player_summaries(player_summaries):
    with open("data/player_summaries.json", "w") as fp:
        json.dump(players_summaries, fp)

def write_player_friends(player_friends):
    with open("data/player_friends.json", "w") as fp:
        json.dump(player_friends, fp)
    
def write_player_games(player_games):
    with open("data/player_games.json", "w") as fp:
        json.dump(player_games, fp)

def write_player_ids(player_achievements):
    with open("data/player_achievements.json", "w") as fp:
        json.dump(player_achievements, fp)
        
def write_player_bans(player_bans):
    with open("data/player_bans.json", "w") as fp:
        json.dump(player_bans, fp)