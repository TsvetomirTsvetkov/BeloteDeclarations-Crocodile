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
				 Card('7', 'hearts'), Card('K', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = []

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_one_belote(self):
		cards = [Card('A', 'spades'), Card('8', 'spades'), Card('10', 'spades'), Card('Q', 'hearts'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = [(Card('Q', 'hearts'), Card('K', 'hearts'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_more_than_one_belote(self):
		cards = [Card('A', 'diamonds'), Card('Q', 'spades'), Card('10', 'spades'), Card('Q', 'hearts'), \
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

	# Consecutive cards:
	
	def test_consecutive_cards(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('10', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		expected_result = [Card('A', 'hearts'), Card('K', 'hearts'), 
						   Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts')]

		result = declarations.get_consecutive_cards(hand, 'hearts', 5)

		self.assertEqual(result, expected_result)
	
	# Quinte:	

	def test_when_hand_has_no_quinte(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quinte'] = []

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)
	
	def test_when_hand_has_quinte_from_ace(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('10', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)
		self.expected_declarations['belote'] = [(Card('Q', 'hearts'), Card('K', 'hearts'))]

		self.expected_declarations['quinte'] = [(Card('A', 'hearts'), Card('K', 'hearts'), 
												 Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)
	
	def test_when_hand_has_quinte_from_jack(self):
		cards = [Card('9', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('7', 'hearts'), \
				 Card('10', 'hearts'), Card('8', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quinte'] = [(Card('J', 'hearts'), Card('10', 'hearts'), Card('9', 'hearts'), \
												 Card('8', 'hearts'), Card('7', 'hearts'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_quinte_then_remove_the_cards_from_the_hand(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'hearts'), \
				 Card('10', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		expected_hand = Hand([Card('8', 'spades'), Card('J', 'spades'), Card('A', 'diamonds')])

		self.assertEqual(declarations.get_hand(), expected_hand)	

	# Quarte:

	def test_when_hand_has_no_quarte(self):
		cards = [Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'clubs'), \
				 Card('7', 'hearts'), Card('K', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quarte'] = []

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_quarte(self):
		cards = [Card('9', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('7', 'diamonds'), \
				 Card('10', 'hearts'), Card('8', 'hearts'), Card('J', 'spades'), Card('A', 'diamonds')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quarte'] = [(Card('J', 'hearts'), Card('10', 'hearts'), Card('9', 'hearts'), \
												 Card('8', 'hearts'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)

	def test_when_hand_has_two_quartes(self):
		cards = [Card('9', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('7', 'spades'), \
				 Card('10', 'hearts'), Card('8', 'hearts'), Card('9', 'spades'), Card('10', 'spades')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quarte'] = [(Card('J', 'hearts'), Card('10', 'hearts'), 
												 Card('9', 'hearts'), Card('8', 'hearts')), \
												(Card('10', 'spades'), Card('9', 'spades'), \
												 Card('8', 'spades'), Card('7', 'spades'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	

	# Tierce:
	def test_when_hand_has_quarte_and_tierce(self):
		cards = [Card('9', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('7', 'diamonds'), \
				 Card('10', 'hearts'), Card('8', 'hearts'), Card('9', 'spades'), Card('10', 'spades')]
		hand = Hand(cards)
		declarations = Declarations(hand)

		self.expected_declarations['quarte'] = [(Card('J', 'hearts'), Card('10', 'hearts'), 
												 Card('9', 'hearts'), Card('8', 'hearts'))]
		self.expected_declarations['tierce'] = [(Card('10', 'spades'), Card('9', 'spades'), \
												 Card('8', 'spades'))]

		self.assertEqual(declarations.get_declarations(), self.expected_declarations)	


class TestOtherTests(unittest.TestCase):
	def setUp(self):
		self.expected_declarations = {'belote': [], 'carreJ': [], 'carre9': [], 'carre': [], \
								 'quinte': [], 'quarte': [], 'tierce': []}

		self.expected_declarations['belote'] = [(Card('Q', 'hearts'), Card('K', 'hearts'))]
		self.expected_declarations['quinte'] = [(Card('A', 'hearts'), Card('K', 'hearts'), 
												 Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts'))]
		self.expected_declarations['tierce'] = [(Card('9', 'hearts'), Card('8', 'hearts'), Card('7', 'hearts'))]

		cards = [Card('K', 'hearts'), Card('8', 'hearts'), Card('J', 'hearts'), Card('7', 'hearts'), \
				 Card('10', 'hearts'), Card('Q', 'hearts'), Card('9', 'hearts'), Card('A', 'hearts')]
		hand = Hand(cards)
		self.declarations = Declarations(hand)

	def test_when_hand_has_8_consecutive_cards_then_return_quinte_tierce_and_belote(self):
		self.assertEqual(self.declarations.get_declarations(), self.expected_declarations)	

	def test_string_repr_when_hand_has_quinte_tierce_and_belote(self):
		str_belote = str([(Card('Q', 'hearts'), Card('K', 'hearts'))])
		str_quinte = str([(Card('A', 'hearts'), Card('K', 'hearts'), 
					   Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts'))])
		str_tierce = str([(Card('9', 'hearts'), Card('8', 'hearts'), Card('7', 'hearts'))])

		expected_string = 'belote: ' + str_belote + ', ' + 'quinte: ' + str_quinte + ', ' + 'tierce: ' + str_tierce + ', '
		
		self.assertEqual(str(self.declarations), expected_string)


if __name__ == '__main__':
	unittest.main()	