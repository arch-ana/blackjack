from Card import Card
from Deck import Deck
from Hand import Hand

class Player():
	def __init__(self, chips):
		self.chips = chips
		self.hand = Hand()
		self.bet_amount = 0

	def bet(self, bet_amount):
		self.chips -= bet_amount
		self.bet_amount = bet_amount

	def hit(self, card, player_name):
		self.hand.add_card(card)
		print(f"{player_name} hits {card}. Current hand value is {self.hand.value()}")

	def stand(self):
		print(f'Player stands with the following cards with a value of {self.hand.value}:')
		print(self.hand)

	def win_bet(self):
		self.chips += 2*self.bet_amount

	def draw_bet(self):
		self.chips += self.bet_amount
