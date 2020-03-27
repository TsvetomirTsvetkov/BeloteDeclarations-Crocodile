import unittest
from card import Card
from hand import Hand

class TestHand(unittest.TestCase):
	def setUp(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]

		self.hand = Hand(cards)

	def test_get_number_of_cards_with_specific_rank(self):
		self.assertEqual(self.hand.get_number_of_cards_with_rank('7'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('8'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('9'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('10'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('J'), 2)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('Q'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('K'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('A'), 2)
	
	def test_get_cards_with_specific_suit(self):
		self.assertEqual(self.hand.get_cards_by_suit('hearts'), ['7', 'J', 'Q', 'K', 'A'])
		self.assertEqual(self.hand.get_cards_by_suit('spades'), ['8', 'J'])
		self.assertEqual(self.hand.get_cards_by_suit('diamonds'), ['A'])
		self.assertEqual(self.hand.get_cards_by_suit('clubs'), [])

	def test_init(self):
		expected_result = [Card('7', 'hearts'),  Card('8', 'spades'), Card('J', 'hearts'), Card('J', 'spades'), \
						   Card('Q', 'hearts'), Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]
		
		self.assertEqual(self.hand.get_cards(), expected_result)	

	def test_get_str_representation_of_the_hand(self):
		sorted_cards = [Card('7', 'hearts'),  Card('8', 'spades'), Card('J', 'hearts'), Card('J', 'spades'), \
						Card('Q', 'hearts'), Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]

		expected = ''.join(str(card) + ' ' for card in sorted_cards)

		self.assertEqual(str(self.hand), expected)

	def test_when_remove_cards_then_update_cards(self):
		cards_to_remove = [Card('J', 'hearts'), Card('8', 'spades')]
		expected_result = [Card('7', 'hearts'), Card('J', 'spades'), Card('Q', 'hearts'), \
						   Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]

		self.hand.remove_cards(cards_to_remove)

		self.assertEqual(self.hand.get_cards(), expected_result)

	def test_when_remove_cards_then_update_rank_dictionary(self):
		cards_to_remove = [Card('J', 'hearts'), Card('8', 'spades')]
		expected_result = [Card('7', 'hearts'), Card('J', 'spades'), Card('Q', 'hearts'), \
						   Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]

		self.hand.remove_cards(cards_to_remove)

		self.assertEqual(self.hand.get_number_of_cards_with_rank('7'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('8'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('9'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('10'), 0)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('J'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('Q'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('K'), 1)
		self.assertEqual(self.hand.get_number_of_cards_with_rank('A'), 2)

	def test_when_remove_cards_then_update_suit_dictionary(self):
		cards_to_remove = [Card('J', 'hearts'), Card('8', 'spades')]
		expected_result = [Card('7', 'hearts'), Card('J', 'spades'), Card('Q', 'hearts'), \
						   Card('K', 'hearts'),  Card('A', 'hearts'), Card('A', 'diamonds')]

		self.hand.remove_cards(cards_to_remove)

		self.assertEqual(self.hand.get_cards_by_suit('hearts'), ['7', 'Q', 'K', 'A'])
		self.assertEqual(self.hand.get_cards_by_suit('spades'), ['J'])
		self.assertEqual(self.hand.get_cards_by_suit('diamonds'), ['A'])
		self.assertEqual(self.hand.get_cards_by_suit('clubs'), [])	


if __name__ == '__main__':
	unittest.main()	