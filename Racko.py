import random
#shuffle cardstack
def shuffle(cardstack):
    random.shuffle(cardstack)
    return cardstack
#check whether rack is racko
def check_racko(rack):
    rack_copy = rack[:]
    rack_copy.sort()
    rack_copy.reverse()
    if rack == rack_copy:
        return True
    return False
#remove and return the top card of a cradstack
def get_top_card(card_stack):
    return card_stack.pop(0)
#make initial deal
def deal_initial_hands(deck):
    computer_hand = []
    player_hand = []
    for i in range(1,11):
        computer_hand.append(get_top_card(deck))
        player_hand.append(get_top_card(deck))
    return (computer_hand, player_hand)
#print rack out from slot 10 to 1
def print_top_to_bottom(rack):
    for i in range(0,len(rack)):
        print rack[i]
#add card to the top of discard stack
def add_card_to_discard(card, discard):
    discard.insert(0, card)
    return discard
#find the card wanted to be replaced and replace it with new one
def find_and_replace(new_card, card_to_be_replaced, hand, discard):
    card_detected = False
    i = 0
    while not card_detected:
        if i < 10 and hand[i] == card_to_be_replaced:
            hand[i] = new_card
            add_card_to_discard(card_to_be_replaced, discard)
            card_detected = True
        elif i < 10:
            i += 1
        else:
            card_to_be_replaced = input("The card you input is not in your hand, please input again: ")
            i = 0
    return hand
#check whether yes or no choices made by player is valid or not
def choice_check(player_answer):
    answer_is_right = True
    if player_answer != 'y' and player_answer != 'n':
        answer_is_right = False
    while not answer_is_right:
        player_answer = raw_input("Please input y or n\n")
        if player_answer == 'y' or player_answer == 'n':
            answer_is_right = True
    return player_answer

#used in computer_play function to replace cards
def computer_replace(cardstack, computer_hand, i, discard):
        new_card = cardstack.pop(0)
        card_to_be_replaced = computer_hand[i]
        computer_hand[i] = new_card
        add_card_to_discard(card_to_be_replaced, discard)
        return computer_hand
    
#AI part, decide whether new card needs to be used and if yes, assign it according to its value
def computer_play(computer_hand, deck, discard):
    discard_card = discard[0]
    deck_card = deck[0]
    #card from discard stack first
    if discard_card >= 50 and computer_hand[0] < 55:
        computer_hand = computer_replace(discard, computer_hand, 0, discard)
    elif discard_card <= 10 and computer_hand[9] > 6:
        computer_hand = computer_replace(discard, computer_hand, 9, discard)
    elif discard_card in range(45,55) and (computer_hand[1] not in range(49,55)):
        computer_hand = computer_replace(discard, computer_hand, 1, discard)
    elif discard_card in range(39,49) and (computer_hand[2] not in range(43,49)):
        computer_hand = computer_replace(discard, computer_hand, 2, discard)
    elif discard_card in range(32,43) and (computer_hand[3] not in range(37,43)):
        computer_hand = computer_replace(discard, computer_hand, 3, discard)
    elif discard_card in range(26,37) and (computer_hand[4] not in range(31,37)):
        computer_hand = computer_replace(discard, computer_hand, 4, discard)
    elif discard_card in range(20,31) and (computer_hand[5] not in range(25,31)):
        computer_hand = computer_replace(discard, computer_hand, 5, discard)
    elif discard_card in range(14,25) and (computer_hand[0] not in range(19,25)):
        computer_hand = computer_replace(discard, computer_hand, 6, discard)
    elif discard_card in range(8,19) and (computer_hand[0] not in range(13,19)):
        computer_hand = computer_replace(discard, computer_hand, 7, discard)
    elif discard_card in range(2,13) and (computer_hand[0] not in range(7,13)):
        computer_hand = computer_replace(discard, computer_hand, 8, discard)
    #if discard card doesn't satisfy condition, check card from deck
    elif deck_card >= 50 and computer_hand[0] < 55:
        computer_hand = computer_replace(deck, computer_hand, 0, discard)
    elif deck_card <= 10 and computer_hand[9] > 6:
        computer_hand = computer_replace(deck, computer_hand, 9, discard)
    elif deck_card in range(45,55) and (computer_hand[1] not in range(49,55)):
        computer_hand = computer_replace(deck, computer_hand, 1, discard)
    elif deck_card in range(39,49) and (computer_hand[2] not in range(43,49)):
        computer_hand = computer_replace(deck, computer_hand, 2, discard)
    elif deck_card in range(32,43) and (computer_hand[3] not in range(37,43)):
        computer_hand = computer_replace(deck, computer_hand, 3, discard)
    elif deck_card in range(26,37) and (computer_hand[4] not in range(31,37)):
        computer_hand = computer_replace(deck, computer_hand, 4, discard)
    elif deck_card in range(20,31) and (computer_hand[5] not in range(25,31)):
        computer_hand = computer_replace(deck, computer_hand, 5, discard)
    elif deck_card in range(14,25) and (computer_hand[0] not in range(19,25)):
        computer_hand = computer_replace(deck, computer_hand, 6, discard)
    elif deck_card in range(8,19) and (computer_hand[0] not in range(13,19)):
        computer_hand = computer_replace(deck, computer_hand, 7, discard)
    elif deck_card in range(2,13) and (computer_hand[0] not in range(7,13)):
        computer_hand = computer_replace(deck, computer_hand, 8, discard)
    #if card from deck doesn't satisfy, then discard it
    else:
        card = deck.pop(0)
        discard = add_card_to_discard(card, discard)
    return computer_hand


def main():
    #create deck list from 1 to 60
    deck = []
    for i in range(1, 61):
        deck.append(i)
    #shuffle deck
    deck = shuffle(deck)
    #assign initial deals to computer and player respectively
    hand = deal_initial_hands(deck)
    computer_hand = hand[0]
    player_hand = hand[1]
    #print player's hand
    print "Your initial hand is:\n"
    print_top_to_bottom(player_hand)
    print "\n"
    #creat an empty discard pile and assign top card from deck as first discard card
    discard = []
    discard.append(get_top_card(deck))
    #check whether any hand racko or not
    while not(check_racko(computer_hand) or check_racko(player_hand)):
        #reveal top card from discard pile
        print "The first card in discard pile is", discard[0],"."
        #ask player if they want use the card and check the answer is valid or not
        player_answer = raw_input("Do you want the card from discard pile?(y or n)\n")
        player_answer = choice_check(player_answer)               
        if player_answer == 'y':
            new_card = discard.pop(0)
            #ask player which card they want to replace and replace the card
            card_to_be_replaced = input("Which card you want to be replaced?\n")
            player_hand = find_and_replace(new_card, card_to_be_replaced, player_hand, discard)
            #display the player's card
            print "Your current hand is:"
            print_top_to_bottom(player_hand)
        elif player_answer == 'n':
            new_card = deck.pop(0)
            #reveal top card from deck pile
            print "The top card from deck is", new_card
            #ask player if they want to use the card and check answer's validity
            second_answer = raw_input("Do you want this card?(y or n)\n")
            second_answer = choice_check(second_answer)
            if second_answer == 'y':
                #ask which card is to be replaced and replace it with new card
                card_to_be_replaced = input("Which card you want to be replaced?\n")
                player_hand = find_and_replace(new_card, card_to_be_replaced, player_hand, discard)
                print "Your current hand is:"
                print_top_to_bottom(player_hand)
            else:
                #discard the card from deck
                discard.append(new_card)
                print "Your current hand is:"
                print_top_to_bottom(player_hand)
        #check it there is any card in deck before computer's move
        if len(deck) == 0:
            deck = shuffle(discard)
            discard = []
            discard.append(deck.pop(0))
        #computer functions as programed
        computer_hand = computer_play(computer_hand, deck, discard)
        #check if deck is empty again, if yes, shuffle the discard pile as new deck
        if len(deck) == 0:
            deck = shuffle(discard)
            discard = []
            discard.append(deck.pop(0))
    #check who wins as loop ends
    if check_racko(player_hand):
        print "You win!"
    else:
        print "You lose! Let's try again!"
    #print computer's final hand
    print "Final computer hand is:\n", computer_hand
    
           
if __name__ == '__main__':
    main()
    


