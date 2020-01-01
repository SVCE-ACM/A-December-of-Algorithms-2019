def check_for_validity(hand):
    suits = ['s','c','d','h']
    values = ['a'] + [str(i) for i in range(2,11)] + ['j','q','k']
    deck = []
    #building a deck
    for value in values:
        for suit in suits:
            deck.append(value + suit)
    try:
        if len(hand) != 5:
            raise
        for card in hand:
            #popping cards out of the deck
            deck.remove(card)
    except:
        #exception will be raised if two or more same cards are present
        return False
    else:
        return True
    
mydict = {'a' : 0, '2' : 1, '3' : 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6, '8' : 7, '9' : 8, '10' : 9, 'j' : 10, 'q' : 11, 'k' : 12}
mylist = ['']*13
suits = []
hand = input("ENTER HAND CONSIDERING 1 DECK(space separated cards): ").strip().split(' ')
valid = check_for_validity(hand)
if valid:
    for card in hand:
        mylist[mydict[card[:-1]]] += card[-1]
        if card[-1] not in suits:
            suits.append(card[-1])
    
    while True:
        if mylist.count('') == 8:
            mylist.append(mylist[0])
            c = 0 
            for ele in mylist:
                if ele != '':
                    c += 1
                elif c < 5 and c > 0:
                    c = 0
            
            if c == 5 and len(suits) == 1:
                print('Straight Flush')

            elif len(suits) == 1:
                print('Flush')

            elif c >= 5:
                print('Straight')

            else:
                print('High Card')

            break
        else:
            four = False
            three = False
            two = False
            count_of_two = 0
            for ele in mylist:
                if len(ele) == 4:
                    four = True
                elif len(ele) == 3:
                    three = True
                elif len(ele) == 2:
                    two = True
                    count_of_two += 1
            if four:
                print('Four of a kind')

            elif three and two:
                print('Full house')

            elif three:
                print('Three of a kind')

            elif two and count_of_two == 2:
                print('Two pairs')

            else:
                print('One pair')

            break
else:
    print('INVALID INPUT')