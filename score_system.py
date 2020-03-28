# score_system.py

from player import Player
from declarations import Declarations

class ScoreSystem:
	# Constructor

	def __init__(self, player_order, game_type):
		self.__team1_declarations = [player_order[0].get_declarations(), player_order[2].get_declarations()]
		self.__team2_declarations = [player_order[1].get_declarations(), player_order[3].get_declarations()]
		self.__game_type = game_type
	
	# Private

	def __remove_unecessary_belotes(self):
		# Махаме белотите, които не са от game_type
		pass

	def __remove_weaker_declarations(self):
		# Махаме терци, кварти, квинти, които са по-слаби
		# от тези на др. отбор
		pass

	# Public

	def get_team1_score(self):
		pass

	def get_team2_score(self):
		pass



