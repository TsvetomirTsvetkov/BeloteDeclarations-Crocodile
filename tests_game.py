# tests_game.py

import unittest
from game import Game
from hand import Hand
from player import Player
from deck import Deck
from team import Team

# Game

class TestGameInit(unittest.TestCase):
	def test_game_init_initializes_object_as_expected(self):
		team1 = Team('Kotenca', [Player('Pesho'), Player('Gosho')])
		team2 = Team('Mechenca', [Player('Tosho'), Player('Losho')])

		game = Game(team1, team2)

		self.assertEqual(game.get_p1_team1(), Player('Pesho'))
		self.assertEqual(game.get_p2_team1(), Player('Gosho'))
		self.assertEqual(game.get_p1_team2(), Player('Tosho'))
		self.assertEqual(game.get_p2_team2(), Player('Losho'))
		self.assertEqual(game.get_team1_score(), 0)
		self.assertEqual(game.get_team2_score(), 0)
		self.assertEqual(game.get_player_order(), 
						[Player('Pesho'), Player('Tosho'),
						Player('Gosho'), Player('Losho')])

# TODO:
# Tests for Play
# Според интернет, за private методи не се пишат тестове, а направо за 
# метода, който ги ползва. За гетърите - също не се.

if __name__ == '__main__':
	unittest.main()