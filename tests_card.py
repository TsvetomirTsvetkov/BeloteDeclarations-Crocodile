# tests_card.py

import unittest
from card import Card

# Card

class TestCardValidateCard(unittest.TestCase):
	def test_card_validate_card_raises_exception_if_number_type_is_not_str(self):
		test_number = 5
		test_suit = 'k'
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Number must be of "str" type.')

	def test_card_validate_card_raises_exception_if_suit_type_is_not_str(self):
		test_number = '5'
		test_suit = 3
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except Exception as err:
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
		test_suit = 'd'
		exc = None

		try:
			Card.validate_card(test_number, test_suit)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Unrecognized number.')

	def test_card_validate_card_passes_with_correct_input(self):
		test_number = 'A'
		test_suit = 'd'

		test_obj = Card(test_number, test_suit)

class TestCardInit(unittest.TestCase):
	def test_card_init_initializes_object_as_expected(self):
		test_number = '8'
		test_suit = 'h'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(getattr(test_obj, 'number'), '8')
		self.assertEqual(getattr(test_obj, 'suit'), 'h')

class TestCardStrDunder(unittest.TestCase):
	def test_card_str_representation_is_as_expected(self):
		test_number = '8'
		test_suit = 'h'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(str(test_obj), '8h')
		

class TestCardReprDunder(unittest.TestCase):
	def test_card_repr_representation_is_as_expected(self):
		test_number = '8'
		test_suit = 'h'
		test_obj = Card(test_number, test_suit)

		self.assertEqual(repr(test_obj), '8h')

if __name__ == '__main__':
	unittest.main()