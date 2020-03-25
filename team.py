class Team:
	def __init__(self, name):
		self.__name = name
		self.__players = []

	def get_name(self):
		return self.__name

	def get_players(self):
		return self.__players		

	def add_players(self, players):
		assert len(players) == 2, 'A team has 2 players.'
		assert players[0].get_team() == players[1].get_team(), 'Players are from different teams.'
		# TODO - or to not have this and allow players with equal names? (but should have different cards(__eq__))
		assert players[0].get_name() != players[1].get_name(), 'Players should have different names.'

		self.__players = players
