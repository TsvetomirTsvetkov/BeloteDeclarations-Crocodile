# card.py

class Card:
	# Constructor

	def __init__(self, number, suit):
		self.validate_card(number, suit)

		self.number = number
		self.suit = suit

	# Dunders

	def __str__(self):
		dictionary = {'hearts': u'\u2665', 'diamonds': u'\u2666', 'clubs': u'\u2663', 'spades': u'\u2660'}
		
		return self.number + dictionary[self.suit]
	
	def __repr__(self):
		dictionary = {'hearts': u'\u2665', 'diamonds': u'\u2666', 'clubs': u'\u2663', 'spades': u'\u2660'}
		
		return self.number + dictionary[self.suit]

	def __eq__(self, other):
		return self.number == other.number and self.suit == other.suit

	def __lt__(self, other):
		dictionary = {'7' : 7, '8': 8, '9': 9, '10': 10,'J': 11, 'Q': 12, 'K': 13, 'A':14}
		
		return dictionary[self.number] < dictionary[other.number]

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