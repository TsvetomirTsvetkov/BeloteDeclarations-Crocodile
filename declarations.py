import copy 
from card import Card

class Declarations: # declaration: cards that form it
	def __init__(self, hand):
		self.__hand = copy.copy(hand) # TODO копие ли да е?
		self.__declarations = {'belote': [], 'carreJ': [], 'carre9': [], 'carre': [], \
								 'quinte': [], 'quarte': [], 'tierce': []}
		self.__add_declarations()

	def get_hand(self):
		return self.__hand	

	def get_declarations(self):
		return self.__declarations

	def __add_declarations(self):
		self.__add_belote()
		self.__add_carre()
		self.__add_consecutive_cards()

	def __add_belote(self):
		for suit in Card.suits:
			queen = Card('Q', suit)
			king = Card('K', suit)

			if queen in self.__hand.get_cards() and king in self.__hand.get_cards():
				self.__declarations['belote'].append((queen, king))

	def __add_carre(self):
		for rank in Card.ranks:
			if self.__hand.get_number_of_cards_with_rank(rank) == 4:
				carre_cards = [Card(rank, suit) for suit in Card.suits]

				self.__hand.remove_cards(carre_cards)

				if rank == 'J':
					self.__declarations['carreJ'] = [tuple(carre_cards)]
				elif rank == '9':
					self.__declarations['carre9'] = [tuple(carre_cards)]
				else:
					self.__declarations['carre'].append(tuple(carre_cards)) #TODO test 2x carre

	def __add_consecutive_cards(self):
		declaration_types = {'quinte': 5, 'quarte': 4, 'tierce': 3}

		for decl_type in declaration_types:
			for suit in Card.suits:
				try:
					new_declaration_cards = self.get_consecutive_cards(self.__hand, suit, declaration_types[decl_type])

					if new_declaration_cards:
						self.__declarations[decl_type].append(tuple(new_declaration_cards))
						self.__hand.remove_cards(new_declaration_cards)

				except AssertionError:
					pass

	@staticmethod
	def get_consecutive_cards(hand, suit, times):
		my_cards = sorted(hand.get_cards_by_suit(suit), reverse=True)
		assert len(my_cards) >= times

		all_cards = sorted([Card(rank, suit) for rank in Card.ranks], reverse=True)

		for i in range(0, len(all_cards) - times + 1):
			possible_sequence = [card for card in all_cards[i : i + times]]

			for j in range(0, len(my_cards) - times + 1):
				my_sequence = my_cards[j : j + times]

				if possible_sequence == my_sequence:
					return my_sequence
		return None						
		
	def __str__(self):
		return self.__str_representation()
	
	def __repr__(self):
		return self.__str_representation()

	def __str_representation(self):
		str_result = ''

		for declaration in self.__declarations.keys():
			if self.__declarations[declaration] != []:
				str_result += declaration + ': ' + str(self.__declarations[declaration]) + ', '
		
		return str_result