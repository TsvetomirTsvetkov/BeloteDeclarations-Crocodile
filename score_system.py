# score_system.py

from player import Player
from declarations import Declarations

class ScoreSystem:
	# Constructor

	def __init__(self, players, game_type):
		self.__team1_declarations = {}
		self.__team2_declarations = {}

		if game_type != 'no trumps':
			self.__team1_declarations = self.get_team_declarations([players[0], players[2]])
			self.__team2_declarations = self.get_team_declarations([players[1], players[3]])

			if game_type in ['clubs', 'diamonds', 'hearts', 'spades']:
				self.__remove_unecessary_belotes(game_type)

			self.__remove_weaker_declarations()		

	# Public

	def get_team1_score(self):
		return self.__get_score(self.__team1_declarations)

	def get_team2_score(self):
		return self.__get_score(self.__team2_declarations)

	def get_team1_declarations(self): # TODO make into 1 function
		result = []

		for key in self.__team1_declarations.keys():
			if self.__team1_declarations[key] != []:
				result.append(str(key))
		
		return result

	def get_team2_declarations(self):
		result = []

		for key in self.__team2_declarations.keys():
			if self.__team2_declarations[key] != []:
				result.append(str(key))
		
		return result	

	# Private

	def __get_score(self, team_declarations):
		declarations_points = {'belote': 20, 'carreJ': 200, 'carre9': 150, 'carre': 100, \
								 'quinte': 100, 'quarte': 50, 'tierce': 20}
		score = 0

		for declaration_type in team_declarations.keys(): # belote, carre, tierce ..
			for declaration in team_declarations[declaration_type]:
				if declaration:
					score += declarations_points[declaration_type]

		return score			

	def __remove_unecessary_belotes(self, game_type):
		for team_declarations in [self.__team1_declarations, self.__team2_declarations]:
			valid_belotes = self.__remove_belote(team_declarations['belote'], game_type)
			team_declarations['belote'] = valid_belotes

	def __remove_weaker_declarations(self):
		team1_highest_sequence_of_cards = self.__get_higher_declaration(self.__team1_declarations)
		team2_highest_sequence_of_cards = self.__get_higher_declaration(self.__team2_declarations) 
		
		if team1_highest_sequence_of_cards and team2_highest_sequence_of_cards:
			if len(team1_highest_sequence_of_cards) > len(team2_highest_sequence_of_cards):
				self.__remove_sequence_declarations('team2')
			elif len(team1_highest_sequence_of_cards) < len(team2_highest_sequence_of_cards):
				self.__remove_sequence_declarations('team1')
			else:
				if team1_highest_sequence_of_cards[0] >	team2_highest_sequence_of_cards[0]:
					self.__remove_sequence_declarations('team2')
				elif team1_highest_sequence_of_cards[0] < team2_highest_sequence_of_cards[0]:
					self.__remove_sequence_declarations('team1')
				else:
					self.__remove_sequence_declarations('team1')
					self.__remove_sequence_declarations('team2')

	def __remove_sequence_declarations(self, team):
		for declaration_type in ['quinte', 'quarte', 'tierce']:
			if team == 'team1':
				self.__team1_declarations[declaration_type] = []
			else:
				self.__team2_declarations[declaration_type] = []
		
	# Static methods
	
	@staticmethod
	def get_team_declarations(players):
		team_declarations = {'belote': [], 'carreJ': [], 'carre9': [], 'carre': [], \
								 'quinte': [], 'quarte': [], 'tierce': []}

		for declaration in team_declarations:	
			for player in players:
				new_declaration = player.get_declarations()[declaration]
				
				if new_declaration:
					team_declarations[declaration] += (new_declaration)

		return team_declarations	

	@staticmethod
	def __remove_belote(all_belotes, game_type):
		for belote in all_belotes:
				belote_suit = belote[0].get_suit()	
				if belote_suit != game_type:
					all_belotes.remove(belote)
		return all_belotes						

	@staticmethod
	def __get_higher_declaration(team_declarations):
		for declaration_type in ['quinte', 'quarte', 'tierce']:
			if team_declarations[declaration_type]:
				highest_declaration_cards = team_declarations[declaration_type][0]

				for cards in team_declarations[declaration_type]:
					if int(cards[0]) > int(highest_declaration_cards[0]):
						highest_declaration_cards = cards

				return highest_declaration_cards

		return {}	