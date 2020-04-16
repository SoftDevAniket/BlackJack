import random

#  Global Variables
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

playing = True


# Classes For the Game

#Card Class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __str__(self):
        return self.rank + " of " + self.suit
    
#Deck Class
class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    
    def __str__(self):
        Deck_string = ""
        for card in self.deck:
                Deck_string += "\n"+card.__str__()
        return Deck_string

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        Single_card = self.deck.pop()
        return Single_card

#Players Hand Class
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces +=1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1

#Players Chips class
class Chips:
    
    def __init__(self,total):
        self.total = 100  # Here we can assign user input or Default Value
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# Function Definition of functions which will be regularly called 
# Function for taking bets
def take_bet(chips):
        while True:
            try:
                chips.bet = int(input("How much chips do you want to put in?:"))
            except:
                print("Please enter proper integer value")
            else:
                if chips.bet > chips.total:
                        print("Sorry Chips nt available")
                else:
                    break
      
# Funtion to deal new card in Players hand
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Function for User input to hit or stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        i = input("Do you want to Hit or Stand?:")
        if i == "Hit":
            hit(deck,hand)
        elif i == "Stand":
            print("Player decided to stand now dealers turn:")
            playing = False         
        else:
            print("Sorry i do not understand please enter Hit or Stand:")
            continue
        
        break

# Function to show hand of player and one card of dealer
def show_some(player,dealer):
    print("\nDEALERS HAND:")
    print(dealer.cards[1])
    
    print("\n")
    
    print("PLAYERS HANDS:")
    for c in player.cards:
        print(c)
        
   
# Function to show whole hand of player and dealer
def show_all(player,dealer):
    print("\nDEALERS HAND:")
    for c in dealer.cards:
        print(c)
    print("\nDealers Hand value:{}".format(dealer.value))
    
    print("\n")
    
    print("PLAYERS HAND:")
    for c in player.cards:
        print(c)
    print("\nDealers Hand value:{}".format(player.value))
    

# Win lose or Tie scenario case functions
def player_busts(player,dealer,chips):
    print("Player Busts!!!Dealer Wins")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!!!Dealer loses")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer Busts!!!Player Wins")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!!! Player Loses")
    chips.lose_bet()
    
def push(player,dealer):
    print("Player and Dealer Tie !!!! PUSH")

# Game Logic

while True:
    print("Welcome to BLACK JACK ARCADE\n")
    
    
    # Create & shuffle the deck 
    test_deck = Deck()
    test_deck.shuffle()
    
    #Setting Dealer's Hand
    D = Hand()
    D.add_card(test_deck.deal())
    D.add_card(test_deck.deal())
    
    #Setting Player's Hand
    P = Hand()
    P.add_card(test_deck.deal())
    P.add_card(test_deck.deal())
    
    # Set up the Player's chips
    Pchips = Chips(100)
    
    # Prompt the Player for bet
    take_bet(Pchips)
    
    
    # Show cards 
    show_some(P,D)    
    
    while playing:  
        
        # Player Input to Hit or Stand
        hit_or_stand(test_deck,P)
        
        # Show cards 
        show_some(P,D)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if P.value > 21 :
            player_busts(P,D,Pchips)
            break

       # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 or until its value is less the players value
        if P.value <= 21:
            while D.value < 17:
                hit(test_deck,D)
    
        # Show all cards
        show_all(P,D)
        
        # Different win lose scenarios
        if D.value >21 :
            dealer_busts(P,D,Pchips)
        elif D.value > P.value:
            dealer_wins(P,D,Pchips)
        elif P.value > D.value:
            player_wins(P,D,Pchips)
        else:
            push(P,D)


    # Displaying Total chips of players 
    print("Player total chips are:{}".format(Pchips.total))
    
    # Ask to play again
    new_game = input("Do u want to play Again Y or N?:")
    
    if new_game == "Y":
        playing = True
        continue
    else:
        break