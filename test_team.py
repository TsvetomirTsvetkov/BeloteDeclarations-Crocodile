# test_team.py

import unittest
from player import Player
from team import Team

class TestTeamValidatePlayers(unittest.TestCase):
	def test_team_validate_players_raises_exception_when_argument_not_list(self):
		p1 = Player('Pesho')
		p2 = Player('Gosho')
		test_players = (p1, p2)
		exc = None

		try:
			Team.validate_players(test_players)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Players must be of "list" type.')

	def test_team_validate_players_raises_exception_when_not_two_players(self):
		p1 = Player('Pesho')
		p2 = Player('Gosho')
		p3 = Player('Tosho')
		test_players = [p1, p2, p3]
		exc = None

		try:
			Team.validate_players(test_players)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Only 2 players per team.')

	def test_team_validate_players_raises_exception_when_elem_of_list_not_player_type(self):
		p1 = Player('Pesho')
		p2 = 'Gosho'
		test_players = [p1, p2]
		exc = None

		try:
			Team.validate_players(test_players)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Elements of list must be of "Player" type.')

	def test_team_validate_players_raises_exception_when_players_have_the_same_name(self):
		p1 = Player('Pesho')
		p2 = Player('Pesho')
		test_players = [p1, p2]
		exc = None

		try:
			Team.validate_players(test_players)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot have players with the same name.')

	def test_team_validate_players_passes_with_correct_input(self):
		p1 = Player('Pesho')
		p2 = Player('Gosho')
		test_players = [p1, p2]

		Team.validate_players(test_players)

class TestTeamGetitemDunder(unittest.TestCase):
	def test_team_getitem_works_as_expected(self):
		p1 = Player('Pesho')
		p2 = Player('Gesho')
		
		team = Team('Team1',[p1, p2])

		self.assertEqual(team[0], p1)
		self.assertEqual(team[1], p2)

class TestTeamStrDunder(unittest.TestCase):
	def test_team_str_representation_is_as_expected(self):
		p1 = Player('Pesho')
		p2 = Player('Gesho')
		
		test_team = Team('Team1',[p1, p2])

		self.assertEqual(str(team), 'Team1')

class TestTeamInit(unittest.TestCase):
	def test_team_init_initialization_is_as_expected(self):
		p1 = Player('Pesho')
		p2 = Player('Gesho')
		
		team = Team('Team1',[p1, p2])
		
		expected_result = [p1, p2]

		self.assertEqual(team.get_players(), expected_result)

if __name__ == '__main__':
	unittest.main()