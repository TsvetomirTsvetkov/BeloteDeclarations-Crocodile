# utils.py

def team_players(players):
	players = players.replace(', ', ' ')
	players = players.split()

	validate_players(players)

	return players

def validate_players(players_list):
	if len(players_list) != 2:
		raise Exception('Only 2 players per team.')

def validate_teams(team1, team2):
	if team1 == team2:
		raise Exception('Cannot have teams with same name.')