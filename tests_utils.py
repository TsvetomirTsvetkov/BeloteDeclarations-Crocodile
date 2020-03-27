# tests_utils.py

import unittest
from utils import (
	team_players,
	validate_teams,
	validate_player_names
)

# team_players

class TestTeamPlayers(unittest.TestCase):
	def test_team_players_splits_string_as_expected(self):
		test_string = 'pesho, gosho'

		self.assertEqual(team_players(test_string), ['pesho', 'gosho'])

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
		self.assertEqual(str(exc), 'Cannot have teams with the same name.')

	def test_validate_teams_passes_with_correct_input(self):
		team1 = 'Mechetata'
		team2 = 'Kotencata'

		validate_teams(team1, team2)

# validate_player_names

class TestValidatePlayerNames(unittest.TestCase):
	def test_validate_player_names_raises_exception_if_player_with_same_name_in_both_teams(self):
		test_names1 = ['Pesho','Gosho']
		test_names2 = ['Pesho','Tosho']
		exc = None

		try:
			validate_player_names(test_names1, test_names2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot have players with the same name.')

	def test_validate_player_names_raises_exception_if_len_of_list_is_not_two(self):
		test_names1 = ['Pesho','Gosho']
		test_names2 = ['Tosho']
		exc = None

		try:
			validate_player_names(test_names1, test_names2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Only 2 players per team.')

if __name__ == '__main__':
	unittest.main()