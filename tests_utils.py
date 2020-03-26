# tests_utils.py

import unittest
from utils import (
	team_players,
	validate_players,
	validate_teams
)

# team_players

class TestTeamPlayers(unittest.TestCase):
	def test_team_players_splits_string_as_expected(self):
		test_string = 'pesho, gosho'

		self.assertEqual(team_players(test_string), ['pesho', 'gosho'])

# validate_players

class TestValidatePlayers(unittest.TestCase):
	def test_validate_players_raises_exception_if_len_of_list_not_two(self):
		test_list = ['pesho', 'gosho', 'tosho']
		exc = None

		try:
			validate_players(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Only 2 players per team.')

	def test_validate_players_passes_with_correct_input(self):
		test_list = ['pesho','gosho']

		validate_players(test_list)

# validate_teams

class TestValidateTeams(unittest.TestCase):
	def test_validate_teams_raises_exception_if_teams_have_same_name(self):
		team1 = 'Mechetata'
		team2 = 'Mechetata'
		exc = None

		try:
			validate_teams(team1, team2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot have teams with same name.')

	def test_validate_teams_passes_with_correct_input(self):
		team1 = 'Mechetata'
		team2 = 'Kotencata'

		validate_teams(team1, team2)

if __name__ == '__main__':
	unittest.main()