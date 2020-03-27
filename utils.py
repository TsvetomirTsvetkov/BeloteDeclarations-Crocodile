# utils.py

def team_players(players):
	return  players.split(', ')

def validate_teams(team1, team2):
	if team1 == team2:
		raise Exception('Cannot have teams with the same name.')

def validate_player_names(list_players_team1, list_players_team2):
	if len(list_players_team1) != 2 or len(list_players_team2) != 2:
		raise Exception('Only 2 players per team.')
	elif list_players_team1[0] in list_players_team2 or list_players_team1[1] in list_players_team2:
		raise Exception('Cannot have players with the same name.')