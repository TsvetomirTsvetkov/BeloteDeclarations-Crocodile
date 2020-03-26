# card.py

class Card:
	# Constructor

	def __init__(self, number, suit):
		self.validate_card(number, suit)

		self.__number = number
		self.__suit = suit

	# Getters

	def get_number(self):
		return self.__number

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
		
		return self.__number + dictionary[self.__suit]

	def __eq__(self, other):
		return self.__number == other.__number and self.__suit == other.__suit

	def __int__(self):
		int_value_of_cards = {'7' : 7, '8': 8, '9': 9, '10': 10,'J': 11, 'Q': 12, 'K': 13, 'A':14}

		return int(int_value_of_cards[self.__number])

	def __lt__(self, other):
		return int(self) < int(other)


	# Static

	@staticmethod
	def validate_card(number, suit):
		allowed_numbers = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		allowed_suits = ['hearts', 'spades', 'clubs', 'diamonds']

		if type(number) is not str:
			raise TypeError('Number must be of "str" type.')
		elif type(suit) is not str:
			raise TypeError('Suit must be of "str" type.')
		elif number not in allowed_numbers:
			raise Exception('Unrecognized number.')
		elif suit not in allowed_suits:
			raise Exception('Unrecognized suit.')