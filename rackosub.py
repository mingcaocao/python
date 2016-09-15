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

def computer_replace_condition(card, computer_hand, i):
    return card < computer_hand[i] and card > computer_hand[i+1] and
         card > computer_hand[i+2] and card > computer_hand[i+3]

def computer_replace(cardstack, computer_hand, i, discard):
        new_card = cardstack.pop(0)
        card_to_be_replaced = computer_hand[i]
        computer_hand[i] = new_card
        add_card_to_discard(card_to_be_replaced, discard)
        return computer_hand
    

def computer_play(computer_hand, deck, discard):
    discard_card = discard[0]
    deck_card = deck[0]
    if (discard_card >= 50 and discard_card > computer_hand[0]) or
       (discard_card > computer_hand[0] and discard_card > computer_hand[1]
        and discard_card > computer_hand[2]):
        computer_hand = computer_replace(discard, computer_hand, 0, discard)
    elif (discard_card <= 10 and discard_card < computer_hand[9]) or
         (discard_card < computer_hand[9] and discard_card < computer_hand[8]
          and discard_card < computer_hand[7]):
        computer_hand = computer_replace(discard, computer_hand, 9, discard)
    elif computer_replace_condition(discard_card, computer_hand, 0):
        computer_hand = computer_replace(discard, computer_hand, 1, discard)
    elif computer_replace_condition(discard_card, computer_hand, 1):
        computer_hand = computer_replace(discard, computer_hand, 2, discard)
    elif computer_replace_condition(discard_card, computer_hand, 2):
        computer_hand = computer_replace(discard, computer_hand, 3, discard)
    elif computer_replace_condition(discard_card, computer_hand, 3):
        computer_hand = computer_replace(discard, computer_hand, 4, discard)
    elif computer_replace_condition(discard_card, computer_hand, 4):
        computer_hand = computer_replace(discard, computer_hand, 5, discard)
    elif computer_replace_condition(discard_card, computer_hand, 5):
        computer_hand = computer_replace(discard, computer_hand, 6, discard)
    elif computer_replace_condition(discard_card, computer_hand, 6):
        computer_hand = computer_replace(discard, computer_hand, 7, discard)
    elif discard_card < computer_hand[7] and discard_card > computer_hand[8]
         and discard_card > computer_hand[9]:
        computer_hand = computer_replace(discard, computer_hand, 8, discard)
    elif (deck_card >= 50 and deck_card > computer_hand[0]) or
         (deck_card > computer_hand[0] and deck_card > computer_hand[1]
          and deck_card > computer_hand[2]):
        computer_hand = computer_replace(deck, computer_hand, 0, discard)
    elif (deck_card <= 10 and deck_card < computer_hand[9]) or
         (deck_card < computer_hand[9] and deck_card < computer_hand[8]
          and deck_card < computer_hand[7]):
        computer_hand = computer_replace(deck, computer_hand, 9, discard)
    elif computer_replace_condition(deck_card, computer_hand, 0):
        computer_hand = computer_replace(deck, computer_hand, 1, discard)
    elif computer_replace_condition(deck_card, computer_hand, 1):
        computer_hand = computer_replace(deck, computer_hand, 2, discard)
    elif computer_replace_condition(deck_card, computer_hand, 2):
        computer_hand = computer_replace(deck, computer_hand, 3, discard)
    elif computer_replace_condition(deck_card, computer_hand, 3):
        computer_hand = computer_replace(deck, computer_hand, 4, discard)
    elif computer_replace_condition(deck_card, computer_hand, 4):
        computer_hand = computer_replace(deck, computer_hand, 5, discard)
    elif computer_replace_condition(deck_card, computer_hand, 5):
        computer_hand = computer_replace(deck, computer_hand, 6, discard)
    elif computer_replace_condition(deck_card, computer_hand, 6):
        computer_hand = computer_replace(deck, computer_hand, 7, discard)
    elif deck_card < computer_hand[7] and deck_card > computer_hand[8]
         and deck_card > computer_hand[9]:
        computer_hand = computer_replace(deck, computer_hand, 8, discard)
    else:
        deck_card = deck.pop(0)
        discard = add_card_to_discard(deck_card, discard)
    return computer_hand


   












        
