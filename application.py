import constants
import os
import sys

TEAMS = []
PLAYERS = []


def clean_teams_data():
    constants_teams_copy = constants.TEAMS.copy()
    for team in constants_teams_copy:
        new_team_dict = {
            team.lower(): []
        }
        TEAMS.append(new_team_dict)


def clean_players_data():
    constants_players_copy = constants.PLAYERS.copy()
    for player in constants_players_copy:
        if 'and' in player['guardians']:
            player['guardians'] = player['guardians'].split(' and ')
        elif 'and' not in player['guardians']:
            player['guardians'] = [player['guardians']]
        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False
        new_player_dict = {
            'name': player['name'],
            'guardians': player['guardians'],
            'experience': player['experience'],
            'height': int(player['height'][:2]),
        }
        PLAYERS.append(new_player_dict)


def balance_and_add_players_to_teams():
    experienced_players = []
    inexperienced_players = []
    for player in PLAYERS:
        if player['experience']:
            experienced_players.append(player)
        elif not player['experience']:
            inexperienced_players.append(player)
    a_third = (len(PLAYERS) // 3) // 2
    two_thirds = a_third + a_third
    addition_loop = 1
    for team in TEAMS:
        for _, value in team.items():
            if addition_loop == 3:
                value += experienced_players[two_thirds:]
                value += inexperienced_players[two_thirds:]
            elif addition_loop == 2:
                value += experienced_players[a_third:two_thirds]
                value += inexperienced_players[a_third:two_thirds]
                addition_loop += 1
            elif addition_loop == 1:
                value += experienced_players[:a_third]
                value += inexperienced_players[:a_third]
                addition_loop += 1


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu_banners():
    banner1 = "BASKETBALL TEAM STATS"
    banner2 = "MENU"
    print(banner1 + '\n')
    print("—" * len(banner2), banner2, "—" * len(banner2) + "\n")


def display_initial_menu_choices():
    print(
        "Enter 'Teams' to View the Teams Menu\n"
        "Enter 'Quit' to Exit\n"
    )


def display_teams_menu():
    print(
        "Enter a Team's Name to View Stats\n"
        "Enter 'Quit' to Exit\n"
    )
    display_team_loop = 1
    for team in TEAMS:
        for key in team.keys():
            print(f"{display_team_loop}) {key.title()}")
            display_team_loop += 1
    print()


def display_team_name(team_name):
    for team in TEAMS:
        for key in team.keys():
            if key == team_name:
                print(f"\n{key.upper()} STATS:\n")


def display_total_players_and_names(team_name):
    value_list = []
    for team in TEAMS: 
        for key in team.keys():
            if key == team_name:
                for value in team.values():
                    for player in value:
                        value_list.append(player['name'])
    print(f"Total Players: {len(value_list)}\n")
    print(f"Players on Team:\n{', '.join(value_list)}\n")


def display_experienced_inexperienced_players(team_name):
    experienced_players = []
    inexperienced_players = []
    for team in TEAMS: 
        for key in team.keys():
            if key == team_name:
                for value in team.values():
                    for player in value:
                        if player['experience']:
                            experienced_players.append(player)
                        elif not player['experience']:
                            inexperienced_players.append(player)
    print(f"Inexperienced Players on Team: {len(inexperienced_players)}")
    print(f"Experienced Players on Team: {len(experienced_players)}\n")


def display_team_average_height(team_name):
    players_heights = []
    total_players = []
    for team in TEAMS:
        for key in team.keys():
                if key == team_name:
                    for value in team.values():
                        for player in value:
                            players_heights.append(player['height'])
                            total_players.append(player)
    print(f"Team Average Height: {sum(players_heights) // len(total_players)} inches\n")


def display_team_guardians(team_name):
    team_guardians = []
    for team in TEAMS:
        for key in team.keys():
                if key == team_name:
                    for value in team.values():
                        for player in value:
                            team_guardians.extend(player['guardians'])
    print(f"Team Guardians:\n{', '.join(team_guardians)}\n")


if __name__ == '__main__':
    clean_teams_data()
    clean_players_data()
    balance_and_add_players_to_teams()
    clear_screen()
    display_menu_banners()
    while True:
        display_initial_menu_choices()
        try:
            initial_menu_choice = input('> ').lower()
            imc_valid_choices = ['quit', 'teams']
            if initial_menu_choice not in imc_valid_choices:
                imc_attempts = 1
                while initial_menu_choice not in imc_valid_choices:
                    if imc_attempts == 3:
                        sys.exit("\nToo many invalid entries.")
                    initial_menu_choice = input("\n Please enter a valid choice:\n")
                    imc_attempts += 1
        except ValueError:
            print("\nThere's been an issue. Try again.")
        else:
            if initial_menu_choice == 'quit':
                clear_screen()
                break
            elif initial_menu_choice == 'teams':
                clear_screen()
                display_teams_menu()
                try:
                    teams_menu_choice = input('> ').lower()
                    tmc_valid_choices = []
                    tmc_valid_choices.append('quit')
                    for team in TEAMS:
                        for key in team.keys():
                            tmc_valid_choices.append(key)
                    if teams_menu_choice not in tmc_valid_choices:
                        tmc_attempts = 1
                        while teams_menu_choice not in tmc_valid_choices:
                            if tmc_attempts == 3:
                                sys.exit("\nToo many invalid entries.")
                            teams_menu_choice = input("\n Please enter a valid choice:\n")
                            tmc_attempts += 1
                except ValueError:
                    print("\nThere's been an issue. Try again.")
                else:
                    if teams_menu_choice == 'quit':
                        clear_screen()
                        break
                    else:
                        clear_screen()
                        display_team_name(teams_menu_choice)
                        display_total_players_and_names(teams_menu_choice)
                        display_experienced_inexperienced_players(teams_menu_choice)
                        display_team_average_height(teams_menu_choice)
                        display_team_guardians(teams_menu_choice)
                        continue
