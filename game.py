# game.py

from player import Player
from deck import Deck
from random import randint

class Game:
	# Constructor

	def __init__(self, team1, team2, players_team1, players_team2):
		p1_team1 = Player(players_team1[0], team1)
		p2_team1 = Player(players_team1[1], team1)
		p3_team2 = Player(players_team2[0], team2)
		p4_team2 = Player(players_team2[1], team2)

		self.__p1_team1 = p1_team1
		self.__p2_team1 = p2_team1
		self.__p3_team2 = p3_team2
		self.__p4_team2 = p4_team2

		self.__order = [p1_team1, p3_team2, p2_team1, p4_team2]
		
		self.__deck = Deck()

		self.__team1_score = 0
		self.__team2_score = 0

	# Private

	def __rotation(self):								# Handle rotation
		first = self.__order[0]							
		self.__order.pop(0)
		self.__order.append(first)

	def __give_cards(self):								# Handing Out Cards To Players
		for elem in self.__order:						
			elem.add_cards(self.__deck.hand_out())

	def __contract(self):
		contracts = ['clubs', 'diamonds','hearts','spades','no trumps','all trumps']

		return contracts[randint(0, 5)]

	# Public

	def get_p1_team1(self):
		return self.__p1_team1
	
	def get_p2_team1(self):
		return self.__p2_team1
	
	def get_p3_team2(self):
		return self.__p3_team2
	
	def get_p4_team2(self):
		return self.__p4_team2

	def get_team1_score(self):
		return self.__team1_score
	
	def get_team2_score(self):
		return self.__team2_score

	def get_order(self):
		return self.__order

	def get_deck(self):
		return self.__deck

	def play(self):
		with open("results.txt", 'w') as f:
			f.write(f'	{self.__p1_team1.get_team()}	|	{self.__p3_team2.get_team()	}\n')
			f.write('=================================\n')
			
			# TODO: while points < 150
			
			round_points_team1 = 0			# Used for representation in results.txt
			round_points_team2 = 0
			current_round = 1				# Used for representation in json

			self.__deck.shuffle_deck()		# Shuffle Deck

			game_type = self.__contract()	# Type of Game

			self.__give_cards()				# Players get their hands
			
			for elem in self.__order:		# Every player calls what he / she has
				# TODO:
				# Declarations
				# Points
				pass
			
			self.__rotation()				# Rotation for next round

			# Това може би трябва да се форматира по някакъв начин (същото важи и за горните write-ове)
			if current_round == 1:
				f.write(f'{self.__team1_score}				|	{self.__team2_score}')
			else:
				f.write(f'{self.__team1_score} + {round_points_team1}			|	{self.__team2_score} + {round_points_team2}')
			# TODO: 
			# Fix class Team to have obj of
			# type "Player"

			if self.__team1_score > 150:
				return self.__p1_team1.get_team()
			elif self.__team2_score > 150:
				return self.__p3_team2.get_team()

			current_round += 1