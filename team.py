# team.py

from player import Player

class Team:
	# Constructor

	def __init__(self, name, players):
		self.validate_players(players)
		self.__name = name
		self.__players = players

	# Dunders

	def __getitem__(self, key):
		return self.__players[key]

	def __str__(self):
		return self.__name

	# Getters
		
	def get_name(self):
		return self.__name

	def get_players(self):
		return self.__players		

	# Static

	@staticmethod
	def validate_players(players):
		if type(players) is not list:
			raise TypeError('Players must be of "list" type.')
		elif len(players) != 2:
			raise Exception('Only 2 players per team.')
		elif type(players[0]) is not Player or type(players[1]) is not Player:
			raise TypeError('Elements of list must be of "Player" type.')
		elif players[0].get_name() == players[1].get_name():
			raise Exception('Cannot have players with the same name.')