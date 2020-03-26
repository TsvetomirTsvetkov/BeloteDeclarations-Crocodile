import unittest
from card import Card
from hand import Hand

class TestHand(unittest.TestCase):
	def setUp(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
		Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]

		self.hand = Hand(cards)

	def test_get_cards_from_specific_suit(self):
		self.assertEqual(self.hand.get_cards_by_suit('hearts'), ['7', 'J', 'Q', 'K', 'A'])
		self.assertEqual(self.hand.get_cards_by_suit('spades'), ['8', 'J'])
		self.assertEqual(self.hand.get_cards_by_suit('diamonds'), ['A'])
		self.assertEqual(self.hand.get_cards_by_suit('clubs'), [])

	def test_get_number_of_cards_with_specific_card_number(self):
		self.assertEqual(self.hand.get_number_of_cards_with_number('7'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_number('8'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_number('9'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_number('10'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_number('J'), 2)
		self.assertEqual(self.hand.get_number_of_cards_with_number('Q'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_number('K'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_number('A'), 2)
		
	def test_init(self):
		expected_result = [Card('7', 'hearts'),  Card('8', 'spades'), Card('J', 'hearts'), Card('J', 'spades'), \
		Card('Q', 'hearts'), Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]
		
		self.assertEqual(self.hand.get_cards(), expected_result)	


	def test_get_str_representation_of_the_hand(self):
		sorted_cards = [Card('7', 'hearts'),  Card('8', 'spades'), Card('J', 'hearts'), Card('J', 'spades'), \
		Card('Q', 'hearts'), Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]

		expected = ''.join(str(card) + ' ' for card in sorted_cards)

		self.assertEqual(str(self.hand), expected)

if __name__ == '__main__':
	unittest.main()	