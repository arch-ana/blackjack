from Card import Card, suits, ranks
import random

class Deck():
	def __init__(self):

		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				new_card = Card(suit, rank)
				self.all_cards.append(new_card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal(self):
		return self.all_cards.pop()

	