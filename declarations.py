declarations = {'belote': 20, 'tierce': 20, 'quarte': 50, \
'quinte': 100, 'carre': 100, 'carre9': 150, 'carreJ': 200 }

import copy 
from card import Card
from hand import Hand 

class Declarations: # declaration: cards, forming it
	def __init__(self, hand):
		self.__hand = copy.copy(hand) # TODO копие ли да е?
		self.__declarations = {'belote': [], 'carreJ': [], 'carre9': [], 'carre': [], \
								 'quinte': [], 'quarte': [], 'tierce': []}
		self.__add_declarations()

	def get_hand(self):
		return self.__hand	

	def get_declarations(self):
		return self.__declarations

	def __add_declarations(self):
		self.__add_belote()
		self.__add_carre()
		#self.__add_quinte()
		#self.__add_quarte()
		#self.__add_tierce()

	def __add_belote(self):
		for suit in Card.suits:
			queen = Card('Q', suit)
			king = Card('K', suit)

			if queen in self.__hand.get_cards() and king in self.__hand.get_cards():
				self.__declarations['belote'].append((queen, king))

	def __add_carre(self):
		self.__declarations['carreJ'] = []
		self.__declarations['carre9'] = []
		self.__declarations['carre'] = []

		for rank in Card.ranks:
			if self.__hand.get_number_of_cards_with_rank(rank) == 4:
				cards = [Card(rank, suit) for suit in Card.suits]

				self.__hand.remove_cards(cards)

				if rank == 'J':
					self.__declarations['carreJ'] = [tuple(cards)]
				elif rank == '9':
					self.__declarations['carre9'] = [tuple(cards)]
				else:
					self.__declarations['carre'].append(tuple(cards)) #TODO test 2x carre

	def __add_quinte(self):
		self.__declarations['quinte'] = []
		cards = []

		try:
			self.__declarations['quinte'] = [tuple(card for card in self.__get_consecutive_cards(5))]
		except:
			pass	

	def __get_consecutive_cards(self, times):
		cards = self.__hand.get_cards_by_suit(suit)
		
		assert len(cards) < times
		
	def __str__(self):
		pass	
				


		