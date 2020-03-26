# belote.py

from game import Game
from utils import team_players, validate_teams

def main():
	team1 = input('Team 1 name: ')
	team2 = input('Team 2 name: ')

	validate_teams(team1, team2)

	players1 = input(f'"{team1}" players: ') 
	players2 = input(f'"{team2}" players: ')

	game = Game(team1, team2, team_players(players1), team_players(players2))

	# TODO:
	# until a team has 2 wins
	game.play()

if __name__ == '__main__':
	main()