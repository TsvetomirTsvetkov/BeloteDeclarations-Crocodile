import unittest
from player import Player
from team import Team

class TestTeam(unittest.TestCase):
	def test_when_add_two_players_with_different_names_and_same_team_then_init_team(self):
		p1 = Player('Pesho', 'Team1')
		p2 = Player('Gesho', 'Team1')
		team = Team('Team1')
		expected_result = [p1, p2]

		team.add_players(expected_result)

		self.assertEqual(team.get_players(), expected_result)

	def test_when_add_one_player_then_raise_error(self):
		p1 = Player('Pesho', 'Team1')
		team = Team('Team1')

		with self.assertRaisesRegex(AssertionError, 'A team has 2 players.'):
			team.add_players([p1])
	
	def test_when_add_two_players_with_different_names_and_teams_then_raise_error(self):
		p1 = Player('Pesho', 'Team1')
		p2 = Player('Gesho', 'Team2')
		team = Team('Team1')

		with self.assertRaisesRegex(AssertionError, 'Players are from different teams.'):
			team.add_players([p1, p2])
	
	def test_when_add_two_players_with_equal_names_and_teams_then_raise_error(self):
		p1 = Player('Pesho', 'Team1')
		p2 = Player('Pesho', 'Team1')
		team = Team('Team1')

		with self.assertRaisesRegex(AssertionError, 'Players should have different names.'):
			team.add_players([p1, p2])

if __name__ == '__main__':
	unittest.main()