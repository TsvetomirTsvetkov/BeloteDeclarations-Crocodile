from hand import Hand

class Player:
	def __init__(self, player_name, team_name):
		self.__name = player_name
		# self.__hand = Hand([]) # инициализирам го като му се подадат карти?
		self.__team = team_name # TODO // string? 

	def get_name(self):
		return self.__name

	def get_team(self):
		return self.__team	

	def get_cards(self):
		return self.__hand.get_cards()		

	def add_cards(self, cards):
		if len(cards) == 8:
			self.__hand = Hand(cards)
		else:
			raise ValueError('You should add 8 cards.')

	def get_declarations(self, current_bid):
		return Declaration(current_bid, self.__hand)

	def __string_repr(self):
		return self.__name + ' is from team: ' + self.__team

	def __str__(self):
		return self.__string_repr()

	def __repr__(self):
		return self.__string_repr()

	def __eq__(self, other):
		return self.__name == other.__name and self.__team == other.__team