from card import Card

class Hand:
	def __init__(self, cards): # cards from type Card 
		self.__cards = sorted(cards)
		self.init_dictionaries()
		self.update_dictionaries()

	def get_cards(self):
		return self.__cards	

	def get_cards_by_suit(self, suit):
		return self.__suits[suit]

	def get_number_of_cards_with_rank(self, rank):
		return self.__ranks[rank]

	def init_dictionaries(self):
		self.__ranks = {'7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0} # how many times we have the card
		self.__suits = {'hearts': [], 'diamonds': [], 'clubs': [], 'spades': []} # hearts: list of card numbers of that suit

	def update_dictionaries(self):
		for card in self.__cards:
			self.__ranks[card.get_number()] += 1
			self.__suits[card.get_suit()].append(card.get_number())

	def remove_cards(self, cards_to_remove):
		new_cards = []

		for card in self.__cards:
			if card not in cards_to_remove:
				new_cards.append(card)

		self.__cards = new_cards		
		self.init_dictionaries()
		self.update_dictionaries()
		
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