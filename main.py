from Deck import Deck
from Player import Player
from time import sleep

#Game Begins
print('Welcome to Blackjack!')

replay = True

player = Player(100)
dealer = Player(100)

def bet(player):
	while True:
		bet_amount = input('Enter your bet: ')
		if bet_amount.isnumeric() and int(bet_amount) <= player.chips and int(bet_amount) <= dealer.chips and int(bet_amount) > 0:
			player.bet(int(bet_amount))
			dealer.bet(int(bet_amount))
			break
		else:
			print('Invalid Input!')

def print_hand(player_instance, player_name):
	print(f'{player_name} has the following cards with the value of {player_instance.hand.value()}:')
	print(player_instance.hand)

def player_action():

	while True:
		if player.hand.value() > 21:
			break
		
		elif player.hand.value() == 21:
			print("Player has a perfect hand. Dealer's turn")
			print("")
			break
		
		action = input('Would you like to hit or stand? (H/S): ')
		print("")
		
		if action.upper() == 'H':
			player.hit(deck.deal(), 'Player')
			print("")
			sleep(1.5)
		elif action.upper() == 'S':
			print_hand(player, 'Player')
			print("")
			break
		else:
			print('Invalid action')

def dealer_action():

	while dealer.hand.value() <= 17:
		dealer.hit(deck.deal(), 'Dealer')
		print("")
		sleep(1.5)

	if dealer.hand.value() > 21:
		pass

	print_hand(dealer, 'Dealer')

def ask_replay():
	
	while True:
		game_play = input("Would you like to replay? (Y/N): ")

		global replay
		if game_play.upper() == 'Y':
			replay = True
			player.hand.clear()
			dealer.hand.clear()
			print("")
			break
		elif game_play.upper() == 'N':
			replay = False
			print("")
			break
		else:
			print("Invalid input")

while replay == True:

	print(f"Player's current balance is: {player.chips}")
	print(f"Dealer's current balance is: {dealer.chips}")

	deck = Deck()
	deck.shuffle()

	#Ask player for their bet
	print("")
	bet(player)

	#Deal two cards
	for x in range(2):
		player.hand.add_card(deck.deal())
		dealer.hand.add_card(deck.deal())

	print("")
	#Print both of players cards
	print_hand(player, 'Player')

	#Print one of dealer's cards
	print(f"Dealer has the following cards with the value of {dealer.hand.get_card_value(0)}:")
	print(dealer.hand.cards[0])

	#Ask player if they want to hit or stand
	#until they go bust or stand

	print("")
	player_action()

	if player.hand.value() > 21:
		print('Player busts. Dealer wins!')
		dealer.win_bet()
		print("")
		ask_replay() 		

	else:
		dealer_action()

		#Deciding winner
		if dealer.hand.value() > 21:
			print('Dealer busts. Player wins!')
			player.win_bet()
		elif player.hand.value() > dealer.hand.value():
			print('Player wins')
			player.win_bet()
		elif player.hand.value() == dealer.hand.value():
			print('Draw!')
			player.draw_bet()
			dealer.draw_bet()
		else:
			print('Dealer wins')
			dealer.win_bet()

		#Would they like to replay?
		print("")
		ask_replay()