# player.py

from hand import Hand
from declarations import Declarations

class Player:
	# Constructor

	def __init__(self, player_name):
		self.__name = player_name
		self.__hand = []

	# Getters

	def get_name(self):
		return self.__name

	def get_hand(self):
		return self.__hand.get_cards()
	
	# Public

	def add_cards(self, cards):
		self.__hand = Hand(cards)

	def get_declarations(self):
		return Declarations(self.__hand).get_declarations()

	# Dunders

	def __str__(self):
		return self.__string_repr()

	def __repr__(self):
		return self.__string_repr()

	def __eq__(self, other):
		return self.__name == other.__name

	# Private:

	def __string_repr(self): 
		return self.__name