# deck.py

from card import Card
import random

class Deck:
	# Constructor

	def __init__(self):
		self.cards = []

		numbers = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

		for elem in numbers:
			self.cards.append(Card(elem, 'hearts'))
			self.cards.append(Card(elem, 'diamonds'))
			self.cards.append(Card(elem, 'clubs'))
			self.cards.append(Card(elem, 'spades'))

	# Dunders

	def __str__(self):
		result = ''

		for elem in self.cards:
			result += str(elem) + ' '

		return result[:-1]

	def __repr__(self):
		result = ''

		for elem in self.cards:
			result += str(elem) + ' '

		return result[:-1]

	# Public

	def shuffle_deck(self):
		random.shuffle(self.cards)

	def hand_out(self):
		hand = self.cards[0:8]
		self.cards = self.cards[8:32] + hand
		
		return hand