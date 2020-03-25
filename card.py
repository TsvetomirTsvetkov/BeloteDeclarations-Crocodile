# card.py

class Card:
	# Constructor

	def __init__(self, number, suit):
		self.validate_card(number, suit)

		self.number = number
		self.suit = suit

	# Dunders

	def __str__(self):
		return self.number + self.suit
	
	def __repr__(self):
		return self.number + self.suit

	# Static

	@staticmethod
	def validate_card(number, suit):
		allowed_numbers = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		allowed_suits = ['h', 's', 'c', 'd']

		if type(number) is not str:
			raise Exception('Number must be of "str" type.')
		elif type(suit) is not str:
			raise Exception('Suit must be of "str" type.')
		elif number not in allowed_numbers:
			raise Exception('Unrecognized number.')
		elif suit not in allowed_suits:
			raise Exception('Unrecognized suit.')