# Created by: Matthew Lourenco
# Created on: 9 Nov 2016
# This program is a version of the game 21

from __future__ import division
from numpy import random
import ui
import time
from scene import *

DECK = ['card:ClubsA', 'card:DiamondsA', 'card:HeartsA', 'card:SpadesA', 'card:Clubs2', 'card:Diamonds2', 'card:Hearts2', 'card:Spades2', 'card:Clubs3', 'card:Diamonds3', 'card:Hearts3', 'card:Spades3', 'card:Clubs4', 'card:Diamonds4', 'card:Hearts4', 'card:Spades4', 'card:Clubs5', 'card:Diamonds5', 'card:Hearts5', 'card:Spades5', 'card:Clubs6', 'card:Diamonds6', 'card:Hearts6', 'card:Spades6', 'card:Clubs7', 'card:Diamonds7', 'card:Hearts7', 'card:Spades7', 'card:Clubs8', 'card:Diamonds8', 'card:Hearts8', 'card:Spades8', 'card:Clubs9', 'card:Diamonds9', 'card:Hearts9', 'card:Spades9', 'card:Clubs10', 'card:Diamonds10', 'card:Hearts10', 'card:Spades10', 'card:ClubsJ', 'card:DiamondsJ', 'card:HeartsJ', 'card:SpadesJ', 'card:ClubsQ', 'card:DiamondsQ', 'card:HeartsQ', 'card:SpadesQ', 'card:ClubsK', 'card:DiamondsK', 'card:HeartsK', 'card:SpadesK']

DECK_VALUE = {'card:ClubsA':1, 'card:DiamondsA':1, 'card:HeartsA':1, 'card:SpadesA':1, 'card:Clubs2':2, 'card:Diamonds2':2, 'card:Hearts2':2, 'card:Spades2':2, 'card:Clubs3':3, 'card:Diamonds3':3, 'card:Hearts3':3, 'card:Spades3':3, 'card:Clubs4':4, 'card:Diamonds4':4, 'card:Hearts4':4, 'card:Spades4':4, 'card:Clubs5':5, 'card:Diamonds5':5, 'card:Hearts5':5, 'card:Spades5':5, 'card:Clubs6':6, 'card:Diamonds6':6, 'card:Hearts6':6, 'card:Spades6':6, 'card:Clubs7':7, 'card:Diamonds7':7, 'card:Hearts7':7, 'card:Spades7':7, 'card:Clubs8':8, 'card:Diamonds8':8, 'card:Hearts8':8, 'card:Spades8':8, 'card:Clubs9':9, 'card:Diamonds9':9, 'card:Hearts9':9, 'card:Spades9':9, 'card:Clubs10':10, 'card:Diamonds10':10, 'card:Hearts10':10, 'card:Spades10':10, 'card:ClubsJ':10, 'card:DiamondsJ':10, 'card:HeartsJ':10, 'card:SpadesJ':10, 'card:ClubsQ':10, 'card:DiamondsQ':10, 'card:HeartsQ':10, 'card:SpadesQ':10, 'card:ClubsK':10, 'card:DiamondsK':10, 'card:HeartsK':10, 'card:SpadesK':10}

player_cards = []
computer_cards = []

card_1_value = 100
card_2_value = 100
card_3_value = 100
card_4_value = 100
card_5_value = 100
card_6_value = 100

money = 0
bet = 0

bet_locked = False

card_1_flipped = False
card_2_flipped = False
card_3_flipped = False
card_4_flipped = False
card_5_flipped = False
card_6_used = False

ace_is_1 = False
ace_is_11 = False

def set_up():
    #When this is called it resets/sets up the game
    
    global player_cards
    global computer_cards
    player_cards = []
    computer_cards = []
    
    view['card_1_imageview'].image = ui.Image('card:BackGreen5')
    view['card_2_imageview'].image = ui.Image('card:BackGreen5')
    view['card_3_imageview'].image = ui.Image('card:BackGreen5')
    view['card_4_imageview'].image = ui.Image('card:BackGreen5')
    view['card_5_imageview'].image = ui.Image('card:BackGreen5')
    view['card_6_imageview'].image = ui.Image('card:BackGreen5')
    
    global card_1_flipped
    global card_2_flipped
    global card_3_flipped
    global card_4_flipped
    global card_5_flipped
    global card_6_used
    card_1_flipped = False
    card_2_flipped = False
    card_3_flipped = False
    card_4_flipped = False
    card_5_flipped = False
    card_6_used = False
    
    global ace_is_1
    global ace_is_11
    ace_is_1 = False
    ace_is_11 = False
    
    global money
    global bet_locked
    money = 100
    bet_locked = False
    
    view['money_label'].text = ' Total Money: $' + str(money)
    
    view['bet_label'].text = ' Bet = '
    view['bet_textfield'].text = ''
    
    view['reply_label'].text = ''
    
    view['card_6_instructions_label'].text = 'Press this card in order to recieve a third card.'
    
    view['ace_value_label'].text = 'First ace will be worth: '

def randomize_card(card_number = ''):
    #When called this randomizes the card value of the inputted number and verifies that it is not the same as the other values
    global card_1_value
    global card_2_value
    global card_3_value
    global card_4_value
    global card_5_value
    global card_6_value
    
    random_card_value = random.randint(0, 52)
    
    card_unique = False
    
    while card_unique == False:
        while True:
            if not card_number == 'card_1' and random_card_value == card_1_value:
                break
            elif not card_number == 'card_2' and random_card_value == card_2_value:
                break
            elif not card_number == 'card_3' and random_card_value == card_3_value:
                break
            elif not card_number == 'card_4' and random_card_value == card_4_value:
                break
            elif not card_number == 'card_5' and random_card_value == card_5_value:
                break
            elif not card_number == 'card_6' and random_card_value == card_6_value:
                break
            else:
                card_unique = True
                return random_card_value
                break
        random_card_value = random.randint(0, 52)

def ace_button_touch_up_inside(sender):
    global ace_is_1
    global ace_is_11
    
    if sender.name == 'ace_1_button' and ace_is_1 == False and ace_is_11 == False:
        ace_is_1 = True
        view['ace_value_label'].text = view['ace_value_label'].text + str(1)
    elif sender.name == 'ace_11_button' and ace_is_1 == False and ace_is_11 == False:
        ace_is_11 = True
        view['ace_value_label'].text = view['ace_value_label'].text + str(11)

@ui.in_background

def check_for_ace():
    global player_cards
    if card_4_flipped == True and card_5_flipped == True:
        for ace_check in range(0, 2):
           if player_cards[ace_check] == 1:
               view['reply_label'].text = 'Would you like your first ace to be 1 or 11? All subsequent aces will be 1 since two 11s will bring you over 21.'
               while True:
                   if card_1_flipped == True or card_2_flipped == True or card_3_flipped == True:
                       break
                   elif ace_is_1 == True:
                       break
                   elif ace_is_11 == True:
                       player_cards[ace_check] = 11
                       break
    if card_4_flipped == True and card_5_flipped == True and card_6_used == True:
        for ace_check in range(0, 3):
            if player_cards[ace_check] == 1:
                view['reply_label'].text = 'Would you like your first ace to be 1 or 11? All subsequent aces will be 1 since two 11s will bring you over 21.'
                while True:
                    if card_1_flipped == True or card_2_flipped == True or card_3_flipped == True:
                        break
                    elif ace_is_1 == True:
                        break
                    elif ace_is_11 == True:
                        player_cards[ace_check] = 11
                        break

def check_bet():
    global bet
    global bet_locked
    bet = view['bet_textfield'].text
    print(bet)
    try:
        bet = int(bet)
        if bet <= money and bet > 0:
            view['bet_label'].text = ' Bet = ' + str(bet)
            bet_locked = True
            return True
        else:
            return False
    except:
        return False

def flip_card_touch_up_inside(sender):
    global computer_cards_flipped	
    global card_1_flipped
    global card_2_flipped
    global card_3_flipped
    global card_4_flipped
    global card_5_flipped
    global card_6_used
    
    if sender.name == 'card_1_button':
        if bet_locked == False:
            if check_bet():
                view['card_1_imageview'].image = ui.Image(card_1_value)
                card_1_flipped = True
            else:
                view['reply_label'].text = "Please enter a valid bet before flipping the opponent's cards."
        else:
            view['card_1_imageview'].image = ui.Image(card_1_value)
            card_1_flipped = True
    elif sender.name == 'card_2_button':
        if bet_locked == False:
            if check_bet():
                view['card_2_imageview'].image = ui.Image(card_2_value)
                card_2_flipped = True
            else:
                view['reply_label'].text = "Please enter a valid bet before flipping the opponent's cards."
        else:
            view['card_2_imageview'].image = ui.Image(card_2_value)
            card_2_flipped = True
    elif sender.name == 'card_3_button':
        if bet_locked == False:
            if check_bet():
                view['card_3_imageview'].image = ui.Image(card_3_value)
                card_3_flipped = True
            else:
                view['reply_label'].text = "Please enter a valid bet before flipping the opponent's cards."
        else:
            view['card_3_imageview'].image = ui.Image(card_3_value)
            card_3_flipped = True
    elif sender.name == 'card_4_button':
        view['card_4_imageview'].image = ui.Image(card_4_value)
        card_4_flipped = True
        check_for_ace()
    elif sender.name == 'card_5_button':
        view['card_5_imageview'].image = ui.Image(card_5_value)
        card_5_flipped = True
        check_for_ace()
    elif sender.name == 'card_6_button':
        if card_1_flipped == False and card_2_flipped == False and card_3_flipped == False:
            view['card_6_imageview'].image = ui.Image(card_6_value)
            view['card_6_instructions_label'].text = ''
            card_6_used = True
            check_for_ace()

def main_flow():
    
    global card_1_value
    global card_2_value
    global card_3_value
    global card_4_value
    global card_5_value
    global card_6_value
    global player_cards
    global computer_cards
    
    card_1_value = randomize_card(card_number = 'card_1')
    card_2_value = randomize_card(card_number = 'card_2')
    card_3_value = randomize_card(card_number = 'card_3')
    card_4_value = randomize_card(card_number = 'card_4')
    card_5_value = randomize_card(card_number = 'card_5')
    card_6_value = randomize_card(card_number = 'card_6')
    card_1_value = DECK[card_1_value]
    card_2_value = DECK[card_2_value]
    card_3_value = DECK[card_3_value]
    card_4_value = DECK[card_4_value]
    card_5_value = DECK[card_5_value]
    card_6_value = DECK[card_6_value]
    
    computer_cards = [DECK_VALUE[card_1_value], DECK_VALUE[card_2_value], DECK_VALUE[card_3_value]]
    player_cards = [DECK_VALUE[card_4_value], DECK_VALUE[card_5_value], DECK_VALUE[card_6_value]]
    
    check_startup_bet = view['bet_textfield'].text
    if check_startup_bet == '':
        view['reply_label'].text = "Please enter a bet"
    try:
        check_startup_bet = int(check_startup_bet)
    except:
        view['reply_label'].text = "Please enter a bet that is a whole number."

def find_winner():
    #finds the winner
    #process
    global computer_cards
    global player_cards
    
    #find each total
    computer_cards_total = 0
    player_cards_total = 0
    
    for computer_total_index in computer_cards:
        computer_cards_total = computer_cards_total + computer_total_index
    
    for computer_ace_check in computer_cards:
        if computer_ace_check == 1 and computer_cards_total < 12:
            computer_cards_total = computer_cards_total + 10
    
    if card_6_used == True:
        for player_total_index in player_cards:
            player_cards_total = player_cards_total + player_total_index
    else:
        player_cards_total = player_cards[0] + player_cards[1]
    
    #output
    #decide the winner by comparing the totals
    if player_cards_total == computer_cards_total:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    elif player_cards_total > 21 and computer_cards_total > 21:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    elif player_cards_total > computer_cards_total and player_cards_total < 22:
        view['reply_label'].text = "You Won! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return True
    
    elif computer_cards_total < 22:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    else:
        view['reply_label'].text = "You Won! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return True

@ui.in_background

def redraw_cards():
    
    for clean_up in range(0, 2):
        view['reply_label'].text = view['reply_label'].text + '\n...'
        time.sleep(1.5)
    
    global player_cards
    global computer_cards
    player_cards = []
    computer_cards = []
    
    view['card_1_imageview'].image = ui.Image('card:BackGreen5')
    view['card_2_imageview'].image = ui.Image('card:BackGreen5')
    view['card_3_imageview'].image = ui.Image('card:BackGreen5')
    view['card_4_imageview'].image = ui.Image('card:BackGreen5')
    view['card_5_imageview'].image = ui.Image('card:BackGreen5')
    view['card_6_imageview'].image = ui.Image('card:BackGreen5')
    
    global card_1_flipped
    global card_2_flipped
    global card_3_flipped
    global card_4_flipped
    global card_5_flipped
    global card_6_used
    card_1_flipped = False
    card_2_flipped = False
    card_3_flipped = False
    card_4_flipped = False
    card_5_flipped = False
    card_6_used = False
    
    global ace_is_1
    global ace_is_11
    ace_is_1 = False
    ace_is_11 = False
    
    global bet_locked
    bet_locked = False
    
    view['money_label'].text = ' Total Money: $' + str(money)
    
    view['bet_label'].text = ' Bet = '
    view['bet_textfield'].text = ''
    
    view['reply_label'].text = ''
    
    view['card_6_instructions_label'].text = 'Press this card in order to recieve a third card.'
    
    view['ace_value_label'].text = 'First ace will be worth: '
    
    main_flow()

@ui.in_background

def check_touch_up_inside(sender):
    global money
    
    if bet_locked == False:
        if check_bet():
            if card_1_flipped == False:
                flip_card_touch_up_inside(view['card_1_button'])
            if card_2_flipped == False:
                flip_card_touch_up_inside(view['card_2_button'])
            if card_3_flipped == False:
                flip_card_touch_up_inside(view['card_3_button'])
            if card_4_flipped == False:
                flip_card_touch_up_inside(view['card_4_button'])
            if card_5_flipped == False:
                flip_card_touch_up_inside(view['card_5_button'])
            bet_won = find_winner()
            if bet_won:
               money = money + bet
            else:
                money = money - bet
            if money == 0:
                view['money_label'].text = ' Total Money: ' + str(money)
                view['reply_label'].text = "You're out of money. Press restart to play again."
            else:
                redraw_cards()
        else:
            view['reply_label'].text = "Please enter a valid bet before flipping the opponent's cards."
    else:
        if card_1_flipped == False:
            flip_card_touch_up_inside(view['card_1_button'])
        if card_2_flipped == False:
            flip_card_touch_up_inside(view['card_2_button'])
        if card_3_flipped == False:
            flip_card_touch_up_inside(view['card_3_button'])
        if card_4_flipped == False:
            flip_card_touch_up_inside(view['card_4_button'])
        if card_5_flipped == False:
            flip_card_touch_up_inside(view['card_5_button'])
        bet_won = find_winner()
        if bet_won:
           money = money + bet
        else:
            money = money - bet
        if money == 0:
            time.sleep(3)
            view['money_label'].text = ' Total Money: ' + str(money)
            view['reply_label'].text = view['reply_label'].text + "\nYou're out of money. Press restart to play again."
        else:
            redraw_cards()

@ui.in_background

def restart_touch_up_inside(sender):
    #restarts the game
    view['reply_label'].text = 'Restarting'
    for load_restart in range(0, 3):
        view['reply_label'].text = view['reply_label'].text + ' . '
        time.sleep(1/3)
    set_up()
    main_flow()

view = ui.load_view()
view.present('fullscreen')

set_up()
main_flow()
