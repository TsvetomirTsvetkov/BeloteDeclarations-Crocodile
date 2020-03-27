from card import Card

class Hand:
	def __init__(self, cards): # cards from type Card 
		self.__cards = sorted(cards)
		self.__init_dictionaries()
		self.__update_dictionaries()

	def get_cards(self):
		return self.__cards	

	def get_cards_by_suit(self, suit):
		return self.__suits[suit]

	def get_number_of_cards_with_rank(self, rank):
		return self.__ranks[rank]

	def __init_dictionaries(self):
		self.__init_ranks()
		self.__init_suits()

	def __init_ranks(self):
		self.__ranks = {}
		for rank in Card.ranks: # how many times we have the card
			self.__ranks[rank] = 0	

	def __init_suits(self):
		self.__suits = {}
		for suit in Card.suits:  # hearts: list of card numbers of that suit
			self.__suits[suit] = []

	def __update_dictionaries(self):
		for card in self.__cards:
			self.__ranks[card.get_rank()] += 1
			self.__suits[card.get_suit()].append(card)

	def remove_cards(self, cards_to_remove):
		new_cards = []

		for card in self.__cards:
			if card not in cards_to_remove:
				new_cards.append(card)

		self.__cards = new_cards		
		self.__init_dictionaries()
		self.__update_dictionaries()
		
	# TODO
	# Къде да е тая ф-я? Защото май в Карти не е много подходящо? 
	@staticmethod 
	def sum_value_of_cards(cards):
		value = 0

		for card in cards:
			value += int(card)

		return value							

	def __str__(self):
		return ''.join(str(card) + ' ' for card in self.__cards) 

	def __repr__(self):
		return ''.join(str(card) + ' ' for card in self.__cards) 
	
	def __getitem__(self, index):
		return self.__cards[index]	

	def __eq__(self, other):
		return self.__cards == other.__cards	