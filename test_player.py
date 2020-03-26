import unittest
from card import Card
from player import Player

class TestPlayer(unittest.TestCase):
	# TODO: Hand class
	'''
	def test_when_add_8_cards(self):
		cards = [Card('7', 'heart'), Card('8', 'spades'), Card('J', 'heart'), Card('Q', 'heart'), \
		Card('A', 'heart'), Card('K', 'heart'), Card('J', 'spades'), Card('10', 'spades')]
		player = Player('Pesho', '1')

		player.add_cards(cards)

		# assertEqual

	def test_when_add_less_than_cards(self):
		cards = [Card('7', 'heart'), Card('8', 'spades'), Card('J', 'heart'), Card('Q', 'heart'), \
		Card('A', 'heart'), Card('K', 'heart'), Card('J', 'spades')]
		player = Player('Pesho', '1')
		my_exc = None

		try:
			player.add_cards(cards)
		except ValueError, 'You should add 8 cards.' as err:
			my_exc = err

		self.assertTrue(my_exc)	
	'''	

	def test_str_representation(self):
		player = Player('Pesho', '1')
		expected_result = 'Pesho is from team: 1'
			
		result = str(player)

		self.assertEqual(result, expected_result)

	# TODO Declaration class
	def test_declaration(self):
		pass	


if __name__ == '__main__':
	unittest.main()
