# player.py

from hand import Hand

class Player:
	# Constructor

	def __init__(self, player_name):
		self.__name = player_name
		self.__hand = []

	# Private:

	def __string_repr(self): 
		return self.__name

	# Dunders

	def __str__(self):
		return self.__string_repr()

	def __repr__(self):
		return self.__string_repr()

	def __eq__(self, other):
		return self.__name == other.__name

	# Getters

	def get_name(self):
		return self.__name

	# Public

	def add_cards(self, cards):
		self.__hand = Hand(cards)

	def get_declarations(self):
		return Declaration(self.__hand).get_declarations()
