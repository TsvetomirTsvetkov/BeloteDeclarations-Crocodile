import unittest
from card import Card
from player import Player

class TestPlayer(unittest.TestCase):
	def test_when_add_less_than_8_cards(self):
		cards = [Card('7', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
		Card('A', 'hearts'), Card('K', 'hearts'), Card('J', 'spades')]
		player = Player('Pesho', '1')

		with self.assertRaisesRegex(ValueError, 'You should add 8 cards.'):
			player.add_cards(cards)
		
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
