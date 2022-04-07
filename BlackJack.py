from random import* 

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*6*4
shuffle(deck)
deck = sample(deck,312) #6decks (52*6)
# print(deck)

def deal(deck): 
    hand = []
    for i in range(2):
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

dealer_hand = deal(deck)
# print(dealer_hand)

player_hand = deal(deck)
# print(player_hand)

# print(deck)

def total(hand):
    total = 0 
    for card in hand:
        if card == "J" or card == "Q" or card == "K": 
            total += 10
        elif card =="A":
            if total >= 11: total +=1
            else: total += 1
        else: total += card
    return total 

def print_results(dealer_hand, player_hand): 
    print("Dealer has:" + str(total(dealer_hand)))
    print("Player has:" + str(total(player_hand)))

def count(dealer_hand,player_hand):
    if total(player_hand) == 21: 
        print_results(dealer_hand, player_hand)
        print("Black Jack")
    elif total(dealer_hand) == 21: 
        print_results(dealer_hand, player_hand)
        print("Dealer Black Jack")
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Push")
    elif total(player_hand) > 21: 
        print_results(dealer_hand,player_hand)
        print("Player Bust")
    elif total(dealer_hand) > 21: 
        print_results(dealer_hand, player_hand)
        print("Dealer Bust")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Player Win")
    else: 
        print_results(dealer_hand, player_hand)
        print("Play Again?")

count(dealer_hand,player_hand)

while player_hand > 21: 
    input ("Would you like to [Hit][Stand]or[Fold]?")

def hit(hand): 
    hand = player_hand
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return(hand)

player_hand = hit(hand)
print(player_hand)