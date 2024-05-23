values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

class Hand():
	def __init__(self):
		self.cards = []
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		if card.rank == 'Ace':
			self.aces += 1

	def get_card_value(self, card_index): 
		return values[self.cards[card_index].rank]

	def value(self):
		hand_value = 0
		number_of_aces = self.aces

		for card in self.cards:
			hand_value += values[card.rank]

		while hand_value > 21 and number_of_aces > 0:
			hand_value -= 10
			number_of_aces -= 1

		return hand_value

	def clear(self):
		self.cards = []

	def __str__(self):
		
		result = ''

		for card in self.cards:
			result += str(card) + '\n'

		return result

