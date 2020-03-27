# card.py

class Card:
	# Constructor
	ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	suits = ['hearts', 'spades', 'clubs', 'diamonds']
	
	def __init__(self, rank, suit):
		self.validate_card(rank, suit)

		self.__rank = rank
		self.__suit = suit

	# Getters

	def get_rank(self):
		return self.__rank

	def get_suit(self):
		return self.__suit	

	# Dunders

	def __str__(self):
		return self.__string_repr()
	
	def __repr__(self):
		return self.__string_repr()

	# за да няма повторение на код
	def __string_repr(self):
		dictionary = {'hearts': u'\u2665', 'diamonds': u'\u2666', 'clubs': u'\u2663', 'spades': u'\u2660'}
		
		return self.__rank + dictionary[self.__suit]

	def __eq__(self, other):
		return self.__rank == other.__rank and self.__suit == other.__suit

	def __int__(self):
		int_value_of_cards = {'7' : 7, '8': 8, '9': 9, '10': 10,'J': 11, 'Q': 12, 'K': 13, 'A':14}

		return int(int_value_of_cards[self.__rank])

	def __lt__(self, other):
		return int(self) < int(other)


	# Class Method
	@classmethod
	def validate_card(cls, rank, suit):
		if type(rank) is not str:
			raise TypeError('Rank must be of "str" type.')
		elif type(suit) is not str:
			raise TypeError('Suit must be of "str" type.')
		elif rank not in cls.ranks:
			raise Exception('Unrecognized rank.')
		elif suit not in cls.suits:
			raise Exception('Unrecognized suit.')