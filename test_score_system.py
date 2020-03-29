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

		self.nothing = [Card('9', 'hearts'), Card('7', 'spades'), Card('8', 'hearts'), Card('Q', 'clubs'), \
						Card('K', 'hearts'), Card('7', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')]
		self.belote_C = [Card('9', 'hearts'), Card('7', 'spades'), Card('8', 'clubs'), Card('Q', 'clubs'), \
						 Card('K', 'clubs'), Card('7', 'diamonds'), Card('J', 'spades'), Card('A', 'diamonds')]			
		self.belote_DH = [Card('8', 'hearts'), Card('8', 'spades'), Card('Q', 'hearts'), Card('Q', 'diamonds'), \
						  Card('7', 'hearts'), Card('K', 'diamonds'), Card('K', 'hearts'), Card('7', 'diamonds')]
		self.tierce987_H = [Card('9', 'hearts'), Card('8', 'hearts'), Card('7', 'hearts'), Card('A', 'hearts'), \
							 Card('K', 'clubs'), Card('A', 'clubs'), Card('J', 'spades'), Card('7', 'spades')]
		self.tierceQJ10_H = [Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts'), Card('A', 'hearts'), \
							 Card('K', 'clubs'), Card('A', 'clubs'), Card('J', 'spades'), Card('7', 'spades')]	
		self.quarteJ1098_H = [Card('J', 'hearts'), Card('10', 'hearts'), Card('9', 'hearts'), Card('8', 'hearts'), \
							  Card('10', 'clubs'), Card('A', 'spades'), Card('J', 'spades'), Card('7', 'spades')]
		self.quarteQJ109_H = [Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts'), Card('9', 'hearts'), \
							  Card('10', 'clubs'), Card('A', 'spades'), Card('J', 'spades'), Card('7', 'spades')] 
		self.quinteAKQJ10_H_belote_H = [Card('A', 'hearts'), Card('K', 'hearts'), Card('Q', 'hearts'), Card('J', 'hearts'), \
										Card('10', 'hearts'), Card('A', 'spades'), Card('J', 'spades'), Card('7', 'spades')]
		self.carre9 = [Card('9', 'hearts'), Card('9', 'clubs'), Card('9', 'spades'), Card('9', 'diamonds'), \
							  Card('10', 'clubs'), Card('A', 'spades'), Card('J', 'spades'), Card('7', 'spades')]  

	def test_when_all_trumps_then_all_belotes_are_valid(self):
		# # # # #
		self.p1.add_cards(self.belote_DH)
		self.p3.add_cards(self.nothing)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.nothing)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['belote'])
		self.assertEqual(ss.get_team2_declarations(), [])
		self.assertEqual(ss.get_team1_score(), 40)
		self.assertEqual(ss.get_team2_score(), 0)
		 
	def test_when_hearts_and_have_unecessary_belote_then_remove_it_from_points(self):
		# # # # #
		self.p1.add_cards(self.belote_DH)
		self.p3.add_cards(self.nothing)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.nothing)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'hearts')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['belote'])
		self.assertEqual(ss.get_team2_declarations(), [])
		self.assertEqual(ss.get_team1_score(), 20)
		self.assertEqual(ss.get_team2_score(), 0)	 
		
	def test_when_team1_has_lower_declaration_then_remove_points_from_team1(self):
		# # # # #
		self.p1.add_cards(self.quarteQJ109_H)
		self.p3.add_cards(self.tierceQJ10_H)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.quinteAKQJ10_H_belote_H)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), [])
		self.assertEqual(ss.get_team2_declarations(), ['belote','quinte'])
		self.assertEqual(ss.get_team1_score(), 0)
		self.assertEqual(ss.get_team2_score(), 120)	

	def test_when_team2_has_lower_declaration_then_remove_points_from_team2(self):
		# # # # #
		self.p1.add_cards(self.quinteAKQJ10_H_belote_H)
		self.p3.add_cards(self.nothing)

		self.p2.add_cards(self.tierceQJ10_H)
		self.p4.add_cards(self.belote_C)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['belote', 'quinte'])
		self.assertEqual(ss.get_team2_declarations(), ['belote'])
		self.assertEqual(ss.get_team1_score(), 120)
		self.assertEqual(ss.get_team2_score(), 20)	

	def test_when_team1_has_same_declaration_as_team_2_then_remove_points_from_both_teams(self):
		# # # # #
		self.p1.add_cards(self.quarteQJ109_H)
		self.p3.add_cards(self.quinteAKQJ10_H_belote_H)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.quinteAKQJ10_H_belote_H)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 
		
		self.assertEqual(ss.get_team1_declarations(), ['belote'])
		self.assertEqual(ss.get_team2_declarations(), ['belote'])
		self.assertEqual(ss.get_team1_score(), 20)
		self.assertEqual(ss.get_team2_score(), 20)			
	
	def test_when_team1_has_lower_rank_declaration_then_remove_points_from_team1(self):
		# # # # #
		self.p1.add_cards(self.quarteJ1098_H)
		self.p3.add_cards(self.carre9)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.quarteQJ109_H)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['carre9'])
		self.assertEqual(ss.get_team2_declarations(), ['quarte'])
		self.assertEqual(ss.get_team1_score(), 150)
		self.assertEqual(ss.get_team2_score(), 50)	

	def test_when_team2_has_lower_rank_declaration_then_remove_points_from_team2(self):
		# # # # #
		self.p1.add_cards(self.tierceQJ10_H)
		self.p3.add_cards(self.nothing)

		self.p2.add_cards(self.nothing)
		self.p4.add_cards(self.tierce987_H)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['tierce'])
		self.assertEqual(ss.get_team2_declarations(), [])
		self.assertEqual(ss.get_team1_score(), 20)
		self.assertEqual(ss.get_team2_score(), 0)	

	def test_when_both_teams_has_same_declarations_then_remove_points_from_both_teams(self):
		# # # # #
		self.p1.add_cards(self.quinteAKQJ10_H_belote_H)
		self.p3.add_cards(self.quinteAKQJ10_H_belote_H)

		self.p2.add_cards(self.quinteAKQJ10_H_belote_H)
		self.p4.add_cards(self.quinteAKQJ10_H_belote_H)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'all trumps')
		# # # # # 

		self.assertEqual(ss.get_team1_declarations(), ['belote'])
		self.assertEqual(ss.get_team2_declarations(), ['belote'])
		self.assertEqual(ss.get_team1_score(), 40)
		self.assertEqual(ss.get_team2_score(), 40)

	def test_random_cards(self):
		p1_c = [Card('8', 'diamonds'), Card('8', 'clubs'), Card('9', 'diamonds'), Card('9', 'spades'), \
				Card('9', 'clubs'), Card('J', 'spades'), Card('Q', 'clubs'), Card('A', 'clubs')]
		p3_c = [Card('7', 'clubs'), Card('8', 'spades'), Card('8', 'hearts'), Card('9', 'hearts'), \
				Card('J', 'clubs'), Card('Q', 'hearts'), Card('K', 'hearts'), Card('A', 'spades')]

		p2_c = [Card('7', 'hearts'), Card('7', 'spades'), Card('10', 'diamonds'), Card('10', 'clubs'), \
				Card('10', 'hearts'), Card('J', 'diamonds'), Card('J', 'hearts'), Card('K', 'clubs')]
		p4_c = [Card('7', 'diamonds'), Card('10', 'spades'), Card('Q', 'diamonds'), Card('Q', 'spades'), \
				Card('K', 'diamonds'), Card('K', 'spades'), Card('A', 'hearts'), Card('A', 'diamonds')]

		# # # # #
		self.p1.add_cards(p1_c)
		self.p3.add_cards(p3_c)

		self.p2.add_cards(p2_c)
		self.p4.add_cards(p4_c)

		ss = ScoreSystem([self.p1, self.p2, self.p3, self.p4], 'diamonds')
		# # # # #

		self.assertEqual(ss.get_team1_declarations(), [])
		self.assertEqual(ss.get_team2_declarations(), ['belote', 'tierce'])
		self.assertEqual(ss.get_team1_score(), 0)
		self.assertEqual(ss.get_team2_score(), 40)		

if __name__ == '__main__':
	unittest.main()