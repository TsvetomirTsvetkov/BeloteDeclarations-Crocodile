# tests_score_system.py

import unittest
from card import Card
from player import Player
from score_system import ScoreSystem

class TestScoreSystem(unittest.TestCase):
	def setUp(self):
		self.p1 = Player('Pesho')
		self.p2 = Player('Gosho')
		self.p3 = Player('Losho')
		self.p4 = Player('Tosho')

		self.p1.add_cards([Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'diamonds'), \
						   Card('7', 'hearts'), Card('K', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')])
		self.p3.add_cards([Card('9', 'hearts'), Card('8', 'spades'), Card('8', 'hearts'), Card('Q', 'clubs'), \
						   Card('7', 'hearts'), Card('K', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')])

		self.p2.add_cards([Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'diamonds'), \
						   Card('7', 'hearts'), Card('K', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')])
		self.p4.add_cards([Card('A', 'hearts'), Card('8', 'spades'), Card('J', 'hearts'), Card('Q', 'clubs'), \
						   Card('7', 'hearts'), Card('K', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')])

		self.ss = ScoreSystem([self.p1,self.p2,self.p3,self.p4], 'all trumps')

	def test_init_score_system(self):
		expected_team1_declarations = {'belote': [(Card('Q', 'diamonds'), Card('K', 'diamonds'))], 'carreJ': [], 'carre9': [], \
		'carre': [], 'quinte': [], 'quarte': [], 'tierce': [(Card('A', 'diamonds'), Card('K', 'diamonds'), Card('Q', 'diamonds')), \
		(Card('9', 'hearts'), Card('8', 'hearts'), Card('7', 'hearts'))]}

		print(self.ss.get_team1_score())

		self.assertEqual(self.ss.get_team_declarations([self.p1, self.p3]), expected_team1_declarations)
		 

	def test_when_unecessary_belote_then_remove_from_points(self):
		self.ss = ScoreSystem([self.p1,self.p2,self.p3,self.p4], 'spades')
	
		self.assertEqual(self.ss.get_team1_score(), 0)		 





if __name__ == '__main__':
	unittest.main()