# game.py

from player import Player
from deck import Deck
from random import randint
from team import Team
from score_system import ScoreSystem
import json

class Game:
	# Constructor

	def __init__(self, team1, team2):
		self.__team1 = team1
		self.__team2 = team2

		self.__team1_score = 0
		self.__team2_score = 0

		self.__team1_wins = 0
		self.__team2_wins = 0

		self.__player_order = [self.__team1[0], self.__team2[0], self.__team1[1], self.__team2[1]]

		self.__deck = Deck()

		self.__games_played = 0

	# Private

	def __rotate_players(self):																# Handle rotation
		first = self.__player_order[0]							
		self.__player_order.pop(0)
		self.__player_order.append(first)

	def __give_cards(self):																	# Handing Out Cards To Players
		for player in self.__player_order:
			player.add_cards(self.__deck.hand_out())

	def __contract(self):
		contracts = ['clubs', 'diamonds', 'hearts', 'spades', 'no trumps', 'all trumps']	# Random contract

		return contracts[randint(0, len(contracts) - 1)]

	# Helpers for writing in results.txt

	def __calculate_text_length(self):														# Helps with formatting text in results.txt
		return 2 * max(len(self.__team1.get_name()), len(self.__team2.get_name())) + 12
	
	def __write_team_names(self):																
		gap = '   '
		team1_name = self.__team1.get_name()
		team2_name = self.__team2.get_name()

		shift = (max(len(team1_name), len(team2_name)) - min(len(team1_name), len(team2_name))) // 2
		helper = gap
		
		for index in range(0, shift):
			helper += ' '

		if len(team1_name) > len(team2_name):
			line = gap + team1_name + gap + '|' + helper + team2_name + helper + '\n'
		elif len(team1_name) < len(team2_name):
			line = helper + team1_name + helper + '|' + gap + team2_name + gap + '\n'
		else:	
			line = gap + team1_name + gap + '|' + gap + team2_name + gap + '\n'
		
		length_of_frame = self.__calculate_text_length()
		
		with open("results.txt", 'a+') as f:
			f.write(line)

			for index in range(0, length_of_frame):
				f.write('=')
			
			f.write('\n')

	def __write_team_scores(self, current_round, round_points_team1, round_points_team2):
		with open("results.txt", 'a+') as f:
			if current_round == 1:
				f.write(str(self.__team1_score + round_points_team1))
				text_length_until_score2 = (self.__calculate_text_length() // 2 ) - len(str(self.__team1_score + round_points_team1))
				
				for number in range(0, text_length_until_score2):
					f.write(' ')
				f.write('| ')
				f.write(str(self.__team2_score + round_points_team2) + '\n')
			else:
				score1 = str(self.__team1_score) + ' + ' + str(round_points_team1)
				f.write(score1)
				text_length_until_score2 = (self.__calculate_text_length() // 2 ) - len(score1)

				for number in range(0, text_length_until_score2):
					f.write(' ')
				f.write('| ')
				f.write(str(self.__team2_score) + ' + ' + str(round_points_team2) + '\n')

			if self.__team1_score + round_points_team1 > 150 or self.__team2_score + round_points_team2 > 150:
				f.write(str(self.__team1_score + round_points_team1))
				text_length_until_score2 = (self.__calculate_text_length() // 2 ) - len(str(self.__team1_score + round_points_team1))
				
				for number in range(0, text_length_until_score2):
					f.write(' ')
				f.write('| ')
				f.write(str(self.__team2_score + round_points_team2) + '\n')

				if self.__team1_score + round_points_team1 > 150:
					self.__team1_wins += 1
				else:
					self.__team2_wins += 1
				
				full_length = self.__calculate_text_length()
				
				for number in range(0, full_length):
					f.write('=')
				f.write('\n')

				for number in range(0, full_length // 4 - 1):
						f.write(' ')

				f.write(f'({self.__team1_wins})')

				for number in range(0, full_length // 4 - 2):
						f.write(' ')
				f.write('|')

				for number in range(0, full_length // 4 - 2):
						f.write(' ')

				f.write(f'({self.__team2_wins})\n')

				for number in range(0, full_length):
					f.write('=')
				f.write('\n\n\n\n')

	# Helpers for writing in data.json
	
	def __round_to_json(self, curr_round, round_points_team1, round_points_team2, declarations_team1, declarations_team2, game_type):
		round_dict = {f'Round {curr_round}':
							{
								"Game type": game_type,
								str(self.__team1):
									{self.__team1.get_players()[0].get_name(): 
										{"Cards": str(self.__team1.get_players()[0].get_hand())},
									self.__team1.get_players()[1].get_name(): 
										{"Cards": str(self.__team1.get_players()[1].get_hand())},
									"Declarations": declarations_team1, 
									"Points": round_points_team1},
								str(self.__team2):
									{self.__team2.get_players()[0].get_name(): 
										{"Cards": str(self.__team2.get_players()[0].get_hand())},
									self.__team2.get_players()[1].get_name(): 
										{"Cards": str(self.__team2.get_players()[1].get_hand())},
									"Declarations": declarations_team2, 
									"Points": round_points_team2}
							}
					}

		return round_dict

	def __save_to_json(self, games_played, round_dictionaries):
		with open('data.json', 'a+') as f:														# Handling .json
			json_data = json.dumps({f"Game{self.__games_played}":round_dictionaries}, indent=4)
			f.write(json_data)			

	# Public

	def play(self):
		self.__write_team_names()

		self.__team1_score = 0
		self.__team2_score = 0

		is_first_player_from_team1 = True # is the first player in player_order from Team1
		current_round = 1																				# Used for representation in json
		round_dictionaries = []
		
		while self.__team1_score <= 150 and self.__team2_score <= 150:
			self.__deck.shuffle_deck()																	# Shuffle Deck

			self.__give_cards()																			# Players get their hands

			game_type = self.__contract()																# Type of Game
			
			score_system = ScoreSystem(self.__player_order, game_type)
			
			if is_first_player_from_team1 == True:
				round_points_team1 = score_system.get_team1_score()										# Used for representation in results.txt
				round_points_team2 = score_system.get_team2_score()
				declarations_team1 = score_system.get_team1_declarations()
				declarations_team2 = score_system.get_team2_declarations()
				is_first_player_from_team1 = False
			else:
				round_points_team1 = score_system.get_team2_score()										# Used for representation in results.txt
				round_points_team2 = score_system.get_team1_score()
				declarations_team1 = score_system.get_team2_declarations()
				declarations_team2 = score_system.get_team1_declarations()
				is_first_player_from_team1 = True

			self.__write_team_scores(current_round, round_points_team1, round_points_team2)

			round_dictionaries.append(self.__round_to_json(	current_round, round_points_team1,\
															round_points_team2, declarations_team1,\
															declarations_team2, game_type))									# Saving to .json

			self.__team1_score += round_points_team1
			self.__team2_score += round_points_team2

			self.__rotate_players()																		# Rotation for next round

			current_round += 1																			# Handling rounds

		self.__games_played += 1

		self.__save_to_json(self.__games_played, round_dictionaries)

		return self.__team1 if self.__team1_score > self.__team2_score  else self.__team2