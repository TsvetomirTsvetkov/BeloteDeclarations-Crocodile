import unittest
from card import Card
from hand import Hand
from declarations import Declarations

class TestBeloteDeclarations(unittest.TestCase):
	def setUp(self):
		self.expected_declarations = {'belote': [], 'carreJ': [], 'carre9': [], 'carre': [], \
								 'quinte': [], 'quarte': [], 'tierce': []}

	# Belote: 
								 
	def test_when_hand_has_no_belote(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = []

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_one_belote(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = [(Card('Q', 'hearts'), Card('K', 'hearts'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_more_than_one_belote(self):
		cards = [Card('A', 'hearts'), Card('Q', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('K', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = [(Card('Q', 'hearts'), Card('K', 'hearts')), \
												(Card('Q', 'spades'), Card('K', 'spades'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	

	# Carre:	

	def test_when_hand_has_no_carre(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['carre'] = []

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_carre_of_nines(self):
		cards = [Card('9', 'hearts'), Card('9', 'spades'), Card('J', 'hearts'), Card('9', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('9', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['carre9'] = [(Card('9', 'hearts'), Card('9', 'spades'), \
												Card('9', 'clubs'), Card('9', 'diamonds'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	

	def test_when_hand_has_carre_of_nines_then_remove_the_cards_from_the_hand(self):
		cards = [Card('9', 'hearts'), Card('9', 'spades'), Card('J', 'hearts'), Card('9', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('9', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		expected_hand = Hand([Card('J', 'hearts'), Card('7', 'hearts'), \
						     Card('K', 'hearts'), Card('J', 'spades')])

		self.assertEqual(declarations.get_hand(), expected_hand)	

	def test_when_hand_has_one_carre_of_non_nines_or_jacks(self):
		cards = [Card('10', 'hearts'), Card('10', 'spades'), Card('J', 'hearts'), Card('10', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('10', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['carre'] = [(Card('10', 'hearts'), Card('10', 'spades'), \
												Card('10', 'clubs'), Card('10', 'diamonds'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	

	def test_when_hand_has_two_carres_of_non_nines_or_jacks(self):
		cards = [Card('10', 'hearts'), Card('10', 'spades'), Card('Q', 'hearts'), Card('10', 'clubs'), \
				 Card('Q', 'clubs'), Card('Q', 'diamonds'), Card('Q', 'spades'), Card('10', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['carre'] = [
				(Card('10', 'hearts'), Card('10', 'spades'), Card('10', 'clubs'), Card('10', 'diamonds')), \
				(Card('Q', 'hearts'), Card('Q', 'spades'), Card('Q', 'clubs'), Card('Q', 'diamonds'))
		]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	

	# Quinte	


if __name__ == '__main__':
	unittest.main()	