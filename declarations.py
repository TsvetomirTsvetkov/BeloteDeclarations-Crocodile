declarations = {'belote': 20, 'tierce': 20, 'quarte': 50, \
'quinte': 100, 'carre': 100, 'carre9': 150, 'carreJ': 200 }

class Declaration:
	# public func
	# returns list of all declarations 
	def get_valid_declarations(current_bid, cards):
		my_declarations = {}

		if current_bid == 'No trumps':
			return []
		if current_bid == 'Heart': # boq
			pass
			# if card(King,Heart) in cards and card(Queen, Heart) in cards:
			# my_declarations.append('belote': 20)	
			

	def get_highest_declaration(declaration_type):
		pass

