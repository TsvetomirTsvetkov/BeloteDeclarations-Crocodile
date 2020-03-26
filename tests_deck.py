# tests_deck.py

import unittest
from card import Card
from deck import Deck

class TestDeckInit(unittest.TestCase):
	def test_deck_init_initializes_object_as_expected(self):
		expected_result = 	[Card('7', 'hearts'), Card('7', 'diamonds'), Card('7', 'clubs'), Card('7', 'spades'),
							Card('8', 'hearts'), Card('8', 'diamonds'), Card('8', 'clubs'), Card('8', 'spades'),\
							Card('9', 'hearts'), Card('9', 'diamonds'), Card('9', 'clubs'), Card('9', 'spades'),\
							Card('10', 'hearts'), Card('10', 'diamonds'), Card('10', 'clubs'), Card('10', 'spades'),\
							Card('J', 'hearts'), Card('J', 'diamonds'), Card('J', 'clubs'), Card('J', 'spades'),\
							Card('Q', 'hearts'), Card('Q', 'diamonds'), Card('Q', 'clubs'), Card('Q', 'spades'),\
							Card('K', 'hearts'), Card('K', 'diamonds'), Card('K', 'clubs'), Card('K', 'spades'),\
							Card('A', 'hearts'), Card('A', 'diamonds'), Card('A', 'clubs'), Card('A', 'spades')]
			
		test_obj = Deck()

		self.assertEqual(getattr(test_obj,'cards'), expected_result)

class TestDeckStrDunder(unittest.TestCase):
	def test_deck_str_representation_is_as_expected(self):
		expected_result = 	'7'+u'\u2665 '+'7'+ u'\u2666 '+'7'+ u'\u2663 '+'7'+ u'\u2660 '+\
							'8'+ u'\u2665 '+'8'+ u'\u2666 '+'8'+ u'\u2663 '+'8'+ u'\u2660 '+\
							'9'+ u'\u2665 '+'9'+ u'\u2666 '+'9'+ u'\u2663 '+'9'+ u'\u2660 '+\
							'10'+ u'\u2665 '+'10'+ u'\u2666 '+'10'+ u'\u2663 '+'10'+ u'\u2660 '+\
							'J'+ u'\u2665 '+'J'+ u'\u2666 '+'J'+ u'\u2663 '+'J'+ u'\u2660 '+\
							'Q'+ u'\u2665 '+'Q'+ u'\u2666 '+'Q'+ u'\u2663 '+'Q'+ u'\u2660 '+\
							'K'+ u'\u2665 '+'K'+ u'\u2666 '+'K'+ u'\u2663 '+'K'+ u'\u2660 '+\
							'A'+ u'\u2665 '+'A'+ u'\u2666 '+'A'+ u'\u2663 '+'A'+ u'\u2660'
		
		test_obj = Deck()

		self.assertEqual(str(test_obj), expected_result)

class TestDeckReprDunder(unittest.TestCase):
	def test_deck_repr_representation_is_as_expected(self):
		expected_result = 	'7'+u'\u2665 '+'7'+ u'\u2666 '+'7'+ u'\u2663 '+'7'+ u'\u2660 '+\
							'8'+ u'\u2665 '+'8'+ u'\u2666 '+'8'+ u'\u2663 '+'8'+ u'\u2660 '+\
							'9'+ u'\u2665 '+'9'+ u'\u2666 '+'9'+ u'\u2663 '+'9'+ u'\u2660 '+\
							'10'+ u'\u2665 '+'10'+ u'\u2666 '+'10'+ u'\u2663 '+'10'+ u'\u2660 '+\
							'J'+ u'\u2665 '+'J'+ u'\u2666 '+'J'+ u'\u2663 '+'J'+ u'\u2660 '+\
							'Q'+ u'\u2665 '+'Q'+ u'\u2666 '+'Q'+ u'\u2663 '+'Q'+ u'\u2660 '+\
							'K'+ u'\u2665 '+'K'+ u'\u2666 '+'K'+ u'\u2663 '+'K'+ u'\u2660 '+\
							'A'+ u'\u2665 '+'A'+ u'\u2666 '+'A'+ u'\u2663 '+'A'+ u'\u2660'
		
		test_obj = Deck()

		self.assertEqual(repr(test_obj), expected_result)

class TestDeckHandOut(unittest.TestCase):
	def test_deck_hand_out_returns_first_8_cards_from_top_of_deck_and_puts_them_in_the_back(self):
		test_obj = Deck()
		expected_result = getattr(test_obj, 'cards')[0:8]

		handed_cards = test_obj.hand_out()

		self.assertEqual(handed_cards, expected_result)
		self.assertEqual(handed_cards, getattr(test_obj, 'cards')[24:32])

if __name__ == '__main__':
	unittest.main()