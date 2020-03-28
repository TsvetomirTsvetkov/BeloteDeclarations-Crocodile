# game.py

from player import Player
from deck import Deck
from random import randint
from team import Team

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
		with open("results.txt", 'w') as f:
			f.write(f'	{self.__team1.get_name()}	|	{self.__team2.get_name()	}\n')
			f.write('=================================\n')
			
			# TODO: while points < 150
			
			round_points_team1 = 0					# Used for representation in results.txt
			round_points_team2 = 0
			current_round = 1						# Used for representation in json

			self.__deck.shuffle_deck()				# Shuffle Deck

			game_type = self.__contract()			# Type of Game

			self.__give_cards()						# Players get their hands
			
			for elem in self.__player_order:		# Every player calls what he / she has
				# TODO:
				# Declarations
				# Points
				pass
			
			self.__rotate_players()					# Rotation for next round

			# Това може би трябва да се форматира по някакъв начин (същото важи и за горните write-ове)
			if current_round == 1:
				f.write(f'{self.__team1_score}				|	{self.__team2_score}')
			else:
				f.write(f'{self.__team1_score} + {round_points_team1}			|	{self.__team2_score} + {round_points_team2}')

			if self.__team1_score > 150:
				return self.__p1_team1.get_team()
			elif self.__team2_score > 150:
				return self.__p3_team2.get_team()

			current_round += 1