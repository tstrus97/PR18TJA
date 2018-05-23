#--------------------------------------------------------- REQUEST FROM API -----------------------------------------------------

def request_all_from_api(num = 100):
    api_fill_player_ids(num)
    api_fill_player_summaries()
    api_fill_player_friends()
    api_fill_player_games()
    api_fill_player_achivements()
    api_fill_player_bans()

    
def api_fill_player_ids(num = 100):
    global global_player_ids
    global_player_ids = set()
    fill_player_ids_rec(my_id, num)

def api_fill_player_summaries():
    global players_summaries
    players_summaries = dict()
    fill_player_summaries()
    
def api_fill_player_friends():
    global player_friends
    player_friends = dict()
    fill_player_friends()

def api_fill_player_games():
    global player_games
    player_games = dict()
    fill_player_games()

def api_fill_player_achievements():
    global player_achievements
    player_achievements = dict()
    fill_player_achievements()
    
def api_fill_player_bans():
    global player_bans
    player_bans = dict()
    fill_player_bans()

#--------------------------------------------------------- REQUEST FROM FILE -----------------------------------------------------

def request_all_from_file():
    file_fill_player_ids()
    file_fill_player_summaries()
    file_fill_player_friends()
    file_fill_player_games()
    file_fill_player_achivements()
    file_fill_player_bans()

def file_fill_player_ids():
    with open("pid_set.json", "r") as fp:
        global global_player_ids
        global_player_ids = set(json.load(fp))
    
def file_fill_player_summaries():
    with open("player_summaries.json", "r") as fp:
        global players_summaries
        players_summaries = json.load(fp)
    
def file_fill_player_friends():
    with open("player_friends.json", "r") as fp:
        global player_friends
        player_friends = json.load(fp)

def file_fill_player_games():
    with open("player_games.json", "r") as fp:
        global player_games
        player_games = json.load(fp)
    
def file_fill_player_achievements():
    with open("player_achievements.json", "r") as fp:
        global player_achievements
        player_achievements = json.load(fp)
        
def file_fill_player_bans():
    with open("player_bans.json", "r") as fp:
        global player_bans
        player_bans = json.load(fp)

#--------------------------------------------------------- WRITE TO FILES -----------------------------------------------------
 
def request_all_from_file():
    write_player_ids()
    write_player_summaries()
    write_player_friends()
    write_player_games()
    write_player_achivements()
    write_player_bans()
    
    
def write_player_ids():
    with open("pid_set.json", "w") as fp:
        global global_player_ids
        json.dump(list(global_player_ids), fp)
    
def write_player_summaries():
    with open("player_summaries.json", "w") as fp:
        global players_summaries
        json.dump(players_summaries, fp)

def write_player_friends():
    with open("player_friends.json", "w") as fp:
        global player_friends
        json.dump(player_friends, fp)
    
def write_player_games():
    with open("player_games.json", "w") as fp:
        global player_games
        json.dump(player_games, fp)

def write_player_ids():
    with open("player_achievements.json", "w") as fp:
        global player_achievements
        json.dump(player_achievements, fp)
        
def write_player_bans():
    with open("player_bans.json", "w") as fp:
        global player_bans
        json.dump(player_bans, fp)