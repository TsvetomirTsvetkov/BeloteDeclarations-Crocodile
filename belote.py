# belote.py

from game import Game
from utils import team_players, validate_teams, validate_player_names

def main():
	team1_name = input('Team 1 name: ')
	team2_name = input('Team 2 name: ')

	validate_teams(team1, team2)									# Checks if teams have the same name

	input_players_team1 = input(f'"{team1}" players: ')		
	input_players_team2 = input(f'"{team2}" players: ')

	list_players_team1 = team_players(input_players_team1)			# Converts input to list of strings with names
	list_players_team2 = team_players(input_players_team2)			# Converts input to list of strings with names

	validate_player_names(list_players_team1, list_players_team2)	# Checks if names from the first list appear in the second
																	# and checks if len(lists) == 2

	team1_player1 = Player(list_players_team1[0])					# Creating players with the names
	team1_player2 = Player(list_players_team1[1])
	team2_player1 = Player(list_players_team2[0])
	team2_player2 = Player(list_players_team2[1])

	team1 = Team(team1_name, [team1_player1, team1_player2])		# Creating the teams
	team2 = Team(team2_name, [team2_player1, team2_player2])

	game = Game(team1, team2)

	# TODO:
	# until a team has 2 wins
	game.play()

if __name__ == '__main__':
	main()