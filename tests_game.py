# tests_game.py

import unittest
from game import Game
from hand import Hand
from player import Player
from deck import Deck

# Game

class TestGameInit(unittest.TestCase):
	def test_game_init_initializes_object_as_expected(self):
		team1 = 'Kotenca'
		team2 = 'Mechenca'

		game = Game(team1, team2, ['Pesho', 'Gosho'], ['Tosho', 'Losho'])

		self.assertEqual(game.get_p1_team1(), Player('Pesho', 'Kotenca'))
		self.assertEqual(game.get_p2_team1(), Player('Gosho', 'Kotenca'))
		self.assertEqual(game.get_p3_team2(), Player('Tosho', 'Mechenca'))
		self.assertEqual(game.get_p4_team2(), Player('Losho', 'Mechenca'))
		self.assertEqual(game.get_team1_score(), 0)
		self.assertEqual(game.get_team2_score(), 0)
		self.assertEqual(game.get_order(), 
						[Player('Pesho', 'Kotenca'), Player('Tosho', 'Mechenca'),
						Player('Gosho', 'Kotenca'), Player('Losho', 'Mechenca')])

# TODO:
# Tests for Play
# Според интернет, за private методи не се пишат тестове, а направо за 
# метода, който ги ползва. За гетърите - също не се.

if __name__ == '__main__':
	unittest.main()