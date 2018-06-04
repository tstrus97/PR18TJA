def player_was_banned(ban_data):
    if ban_data["cb"] == True:
        return True
    if ban_data["vacb"] == True:
        return True
    if ban_data["novacb"] > 0:
        return True
    if ban_data["nogb"] > 0:
        return True
    if ban_data["eb"] != "none":
        return True

def get_community_ban_visibility_data(player_summaries, player_bans):
    bans_and_profiles = [0]*4 #p!b, pb, !p!b, !pb
    for playerid, data in player_summaries.items():
        try: 
            if data["cvs"] == 3:
                if player_bans[playerid]["cb"] == True:
                    bans_and_profiles[1]+=1
                else:
                    bans_and_profiles[0]+=1
            else:
                if player_bans[playerid]["cb"] == True:
                    bans_and_profiles[3]+=1
                else:
                    bans_and_profiles[2]+=1
        except:
            pass
    return ((bans_and_profiles[0], bans_and_profiles[2]),(bans_and_profiles[1], bans_and_profiles[3]))
    
def get_vac_ban_visibility_data(player_summaries, player_bans):
    bans_and_profiles = [0]*4 #p!b, pb, !p!b, !pb
    for playerid, data in player_summaries.items():
        try: 
            if data["cvs"] == 3:
                if player_bans[playerid]["vacb"] == True:
                    bans_and_profiles[1]+=1
                else:
                    bans_and_profiles[0]+=1
            else:
                if player_bans[playerid]["vacb"] == True:
                    bans_and_profiles[3]+=1
                else:
                    bans_and_profiles[2]+=1
        except:
            pass
    return ((bans_and_profiles[0], bans_and_profiles[2]),(bans_and_profiles[1], bans_and_profiles[3]))

def get_economy_ban_visibility_data(player_summaries, player_bans):
    bans_and_profiles = [0]*4 #p!b, pb, !p!b, !pb
    for playerid, data in player_summaries.items():
        try: 
            if data["cvs"] == 3:
                if player_bans[playerid]["eb"] != "none":
                    bans_and_profiles[1]+=1
                else:
                    bans_and_profiles[0]+=1
            else:
                if player_bans[playerid]["eb"] != "none":
                    bans_and_profiles[3]+=1
                else:
                    bans_and_profiles[2]+=1
        except:
            pass
    return ((bans_and_profiles[0], bans_and_profiles[2]),(bans_and_profiles[1], bans_and_profiles[3]))

def ban_visibility_plot(good_in, bad_in):
    import numpy as np
    import matplotlib.pyplot as plt
    
    good = [0]*2
    bad = [0]*2
    good[0]= good_in[0]/sum([good_in[0], bad_in[0]])
    good[1]= good_in[1]/sum([good_in[1], bad_in[1]])
    bad[0]= bad_in[0]/sum([good_in[0], bad_in[0]])
    bad[1]= bad_in[1]/sum([good_in[1], bad_in[1]])
    
    fig, ax = plt.subplots()

    ind = np.arange(2)    # the x locations for the groups
    width = 0.35         # the width of the bars
    p1 = ax.bar(ind, good, width, color='y', bottom=0)


    p2 = ax.bar(ind + width, bad, width, color='r', bottom=0)

    ax.set_title('bans')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('Public', 'Private'))

    ax.legend((p1[0], p2[0]), ('Never Banned', 'Banned'))
    ax.autoscale_view()

    plt.show()