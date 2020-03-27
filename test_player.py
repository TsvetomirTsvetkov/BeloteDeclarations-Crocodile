import unittest
from card import Card
from player import Player
from hand import Hand

class TestPlayerInit(unittest.TestCase):
	def test_player_init_initializes_player_as_expected(self):
		test_player = Player('Pesho')

		self.assertEqual(test_player.get_name(), 'Pesho')
		self.assertEqual(test_player._Player__hand, [])

class TestPlayerStrDunder(unittest.TestCase):
	def test_player_str_representation_is_as_expected(self):
		test_player = Player('Pesho')
		expected_result = 'Pesho'
			
		result = str(test_player)

		self.assertEqual(result, expected_result)

class TestPlayerReprDunder(unittest.TestCase):
	def test_player_str_representation_is_as_expected(self):
		test_player = Player('Pesho')
		expected_result = 'Pesho'
			
		result = repr(test_player)

		self.assertEqual(result, expected_result)

class TestPlayerEqDunder(unittest.TestCase):
	def test_player_eq_comparison_is_as_expected(self):
		test_player1 = Player('Pesho')
		test_player2 = Player('Pesho')
		test_player3 = Player('Gosho')

		self.assertEqual(test_player1, test_player2)
		self.assertNotEqual(test_player2, test_player3)

class TestPlayerAddCards(unittest.TestCase):
	def test_player_add_cards_works_as_expected(self):
		test_player = Player('Pesho')
		test_hand = Hand([Card('7','hearts'), Card('7','spades'), Card('7','clubs'), Card('7','diamonds'),\
		Card('8','hearts'), Card('8','spades'), Card('8','clubs'), Card('8','diamonds')])

		test_player.add_cards(test_hand)

		self.assertEqual(test_player._Player__hand, test_hand)

if __name__ == '__main__':
	unittest.main()
