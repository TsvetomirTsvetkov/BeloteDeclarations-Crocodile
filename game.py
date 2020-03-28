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

		self.__player_order = [self.__team1[0], self.__team2[0], self.__team1[1], self.__team2[1]]

		self.__deck = Deck()

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

		return contracts[randint(0, 5)]

	def __get_team_declarations(self):
		pass 

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
					team1_final_score = 1
					team2_final_score = 0
				else:
					team1_final_score = 0
					team2_final_score = 1
				
				full_length = self.__calculate_text_length()
				
				for number in range(0, full_length):
					f.write('=')
				f.write('\n')

				for number in range(0, full_length // 4 - 1):
						f.write(' ')

				f.write(f'({team1_final_score})')

				for number in range(0, full_length // 4 - 2):
						f.write(' ')
				f.write('|')

				for number in range(0, full_length // 4 - 2):
						f.write(' ')

				f.write(f'({team2_final_score})\n')

				for number in range(0, full_length):
					f.write('=')
				f.write('\n\n\n\n')

	# Getters

	def get_p1_team1(self):
		return self.__team1[0]
	
	def get_p2_team1(self):
		return self.__team1[1]
	
	def get_p1_team2(self):
		return self.__team2[0]
	
	def get_p2_team2(self):
		return self.__team2[1]

	def get_team1_score(self):
		return self.__team1_score
	
	def get_team2_score(self):
		return self.__team2_score

	def get_player_order(self):
		return self.__player_order

	# Public

	def play(self):
		self.__write_team_names()

		self.__team1_score = 0
		self.__team2_score = 0

		switch = True
		current_round = 1																		# Used for representation in json
		
		while self.__team1_score <= 150 and self.__team2_score <= 150:
			self.__deck.shuffle_deck()															# Shuffle Deck

			self.__give_cards()																	# Players get their hands

			game_type = self.__contract()														# Type of Game
			
			points = ScoreSystem(self.__player_order, game_type)
			
			if switch == True:
				round_points_team1 = points.get_team1_score()									# Used for representation in results.txt
				round_points_team2 = points.get_team2_score()
				switch = False
			else:
				round_points_team1 = points.get_team2_score()									# Used for representation in results.txt
				round_points_team2 = points.get_team1_score()
				switch = True

			self.__write_team_scores(current_round, round_points_team1, round_points_team2)

			# TODO: Json

			self.__team1_score += round_points_team1
			self.__team2_score += round_points_team2

			self.__rotate_players()																# Rotation for next round

			current_round += 1																	# Handling rounds

		return self.__team1 if self.__team1_score > self.__team2_score  else self.__team2 