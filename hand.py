from card import Card

class Hand:
	def __init__(self, cards):
		self.__cards = cards
		cards.sort()