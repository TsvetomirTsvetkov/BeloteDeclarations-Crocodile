# tests_card.py

import unittest
from card import Card

# Card

class TestCardValidateCard(unittest.TestCase):
	def test_card_validate_card_raises_exception_if_number_type_is_not_str(self):
		test_number = 5
		test_suit = 'diamonds'
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Number must be of "str" type.')

	def test_card_validate_card_raises_exception_if_suit_type_is_not_str(self):
		test_number = '9'
		test_suit = 3
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Suit must be of "str" type.')

	def test_card_validate_card_raises_exception_if_suit_is_not_allowed(self):
		test_number = '8'
		test_suit = 'p'
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Unrecognized suit.')

	def test_card_validate_card_raises_exception_if_number_is_not_allowed(self):
		test_number = '12'
		test_suit = 'diamonds'
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Unrecognized number.')

	def test_card_validate_card_passes_with_correct_input(self):
		test_number = 'A'
		test_suit = 'diamonds'

		test_obj = Card(test_number, test_suit)

class TestCardInit(unittest.TestCase):
	def test_card_init_initializes_object_as_expected(self):
		test_number = '8'
		test_suit = 'hearts'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(test_obj.get_number(), '8')
		self.assertEqual(test_obj.get_suit(), 'hearts')

class TestCardStrDunder(unittest.TestCase):
	def test_card_str_representation_is_as_expected(self):
		test_number = '8'
		test_suit = 'hearts'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(str(test_obj), '8' + u'\u2665')
		

class TestCardReprDunder(unittest.TestCase):
	def test_card_repr_representation_is_as_expected(self):
		test_number = '8'
		test_suit = 'hearts'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(repr(test_obj), '8'+ u'\u2665')

class TestCardEqDunder(unittest.TestCase):
	def test_card_eq_compares_cards_as_expected(self):
		test_number1 = '8'
		test_suit1 = 'hearts'

		test_obj1 = Card(test_number1, test_suit1)
		test_obj2 = Card(test_number1, test_suit1)

		self.assertEqual(test_obj1, test_obj2)

		test_number2 = '7'
		test_suit2 = 'diamonds'

		test_obj3 = Card(test_number2, test_suit2)

		self.assertNotEqual(test_obj1, test_obj3)

class TestCardLtDunder(unittest.TestCase):
	def test_card_lt_compares_cards_as_expected_when_different_suits(self):
		test_number1 = '7'
		test_suit1 = 'hearts'
		test_number2 = '8'
		test_suit2 = 'diamonds'

		test_obj1 = Card(test_number1, test_suit1)
		test_obj2 = Card(test_number2, test_suit2)

		self.assertLess(test_obj1, test_obj2)

	def test_card_lt_compares_cards_as_expected_same_different_suit(self):
		test_number1 = '7'
		test_suit1 = 'hearts'
		test_number2 = '8'
		test_suit2 = 'hearts'

		test_obj1 = Card(test_number1, test_suit1)
		test_obj2 = Card(test_number2, test_suit2)

		self.assertLess(test_obj1, test_obj2)

if __name__ == '__main__':
	unittest.main()