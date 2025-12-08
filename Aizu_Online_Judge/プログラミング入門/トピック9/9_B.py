while True:
    cards = input()

    if '-' in cards: 
        break

    shuffle_count = int(input())
    
    for i in range(shuffle_count):
        h = int(input())
        new_cards = cards[h:] + cards[0:h]
        cards = new_cards
    
    print(new_cards)