import csv
exp_players = []
first_timers = []
assigned_players = []

# Reading file as a dictionary.
def read_file():
    with open('soccer_players.csv', newline='') as csv_file:
        player_reader = csv.DictReader(csv_file)
        rows = list(player_reader)
        # Gathering the needed player data and dividing players with experience from no experience.  
        for row in rows:
            if row["Soccer Experience"] == "YES":
                exp_players.append([row["Name"], row["Soccer Experience"], row["Guardian Name(s)"]])
            else:
                first_timers.append([row["Name"], row["Soccer Experience"], row["Guardian Name(s)"]])

# Assigning each third player a team depending on the starting index of a slice.
def assign_players():
    for player in exp_players[2::3]:
        assigned_players.append({'Sharks': player})
    for player in first_timers[2::3]:
        assigned_players.append({'Sharks': player})
    for player in exp_players[1::3]:
        assigned_players.append({'Dragons': player})
    for player in first_timers[1::3]:
        assigned_players.append({'Dragons': player})
    for player in exp_players[0::3]:
        assigned_players.append({'Raptors': player})
    for player in first_timers[0::3]:
        assigned_players.append({'Raptors': player})


def write_file():
    # Create a new text file.
    with open('teams.txt', 'w') as text_file:
        # Listing the teams and player's depending on the players assigned team.
        text_file.write("Sharks\n")
        text_file.write("=" * 8 + "\n")
        for player in assigned_players:
            if 'Sharks' in player.keys():
                text_file.write(', '.join(player['Sharks']))
                text_file.write("\n")
        text_file.write("\n" * 2)
        text_file.write("Dragons\n")
        text_file.write("=" * 8 + "\n")
        for player in assigned_players:
            if "Dragons" in player.keys():
                text_file.write(', '.join(player['Dragons']))
                text_file.write("\n")
        text_file.write("\n" * 2)
        text_file.write("Raptors\n")
        text_file.write("=" * 8 + "\n")
        for player in assigned_players:
            if "Raptors" in player.keys():
                text_file.write(', '.join(player['Raptors']))
                text_file.write("\n")

# Creating a welcome letter for each player.
def welcome_letter(player):
    team_meet = ["October 23 at 4", "October 23 at 5", "October 23 at 6"]
    for key in player.keys():
        # Creating a file name from the player's first and last name.
        file_name = player[key][0].split()
        with open('{}_{}.txt'.format(file_name[0].lower(), file_name[1].lower()), 'w') as text_file:
            # Writing the letter using the player's data
            text_file.write("Dear {},\n".format(player[key][2]))
            text_file.write(player[key][0])
            text_file.write(" was assigned to team {}. ".format(key))
            # Assigning a date and time for first practice.
            if key == "Sharks":
                text_file.write("First practice is on {}.".format(team_meet[0]))
            if key == "Dragons":
                text_file.write("First practice is on {}.".format(team_meet[1]))
            if key == "Raptors":
                text_file.write("First practice is on {}.".format(team_meet[2]))

# Keeping the script from running if imported.
if __name__ == "__main__":
    read_file()
    assign_players()
    write_file()
    for player in assigned_players:
        welcome_letter(player)
