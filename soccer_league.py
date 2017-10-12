import csv
exp_players = []
first_timers = []
assigned_players = []


def read_file():
    with open('soccer_players.csv', newline='') as csv_file:
        player_reader = csv.DictReader(csv_file)
        rows = list(player_reader)
        for row in rows:
            if row["Soccer Experience"] == "YES":
                exp_players.append([row["Name"], row["Soccer Experience"], row["Guardian Name(s)"]])
            else:
                first_timers.append([row["Name"], row["Soccer Experience"], row["Guardian Name(s)"]])


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
    with open('teams.txt', 'w') as text_file:
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


def welcome_letter(player):
    team_meet = ["October 23 at 4", "October 23 at 5", "October 23 at 6"]
    for key in player.keys():
        file_name = player[key][0].split()
        with open('{}_{}.txt'.format(file_name[0].lower(), file_name[1].lower()), 'w') as text_file:
            text_file.write("Dear {},\n".format(player[key][2]))
            text_file.write(player[key][0])
            text_file.write(" was assigned to team {}. ".format(key))
            if key == "Sharks":
                text_file.write("First practice is on {}.".format(team_meet[0]))
            if key == "Dragons":
                text_file.write("First practice is on {}.".format(team_meet[1]))
            if key == "Raptors":
                text_file.write("First practice is on {}.".format(team_meet[2]))


if __name__ == "__main__":
    read_file()
    assign_players()
    write_file()
    for player in assigned_players:
        welcome_letter(player)
