import random, os, time

def c():
    os.system('cls')

def s(seconds:float):
    time.sleep(seconds)

class Player:

    instances = []

    def __init__(self, name:str, state= False ,total_value= 0):
        #Values asignation:
        self.name = name
        self.cards = []
        self.state = state
        self.total_value = total_value
        #Extra steps
        Player.instances.append(self)

    #Adds a card to the instace
    def get_new_card(self):
        card = Card()
        #If the value is a list that means it's an ace, check Card class value asignation 
        if isinstance(card.value,list):
            ace_value = int(input("Please select the value of your Ace\n1- value = 1\n2- value = 11\n> "))
            try:
                card.value = card.value[ace_value-1]
            except:
                print("Inexisting option, selecting ace value as 1")
                card.value = card.value[0]
        self.cards.append(card.string_representation)
        self.total_value += card.value
        return card
    
    #This is in a separated function so you can call it when the player wants to stand
    def stop_getting_cards(self):
        self.state = False

    #Checks if the players total value of cards
    def check_value(self):
        total_card_value = 0
        for card in self.cards:
            total_card_value += card.value
        if total_card_value > 21:
            self.state = False

class Card:
    __symbols = ["♥","♦","♣","♠"]
    __figures = ["K","Q","J"]

    def __init__(self,string_representation="",value=0):
        
        #Random value generation 
        random_number = random.randint(2,14)
        #For number cards we assign the value generated 
        if random_number < 11:
            value = random_number
            symbol = random.choice(Card.__symbols)
            #Sorry, i dont know how to shorten the design for every number card, also, i just
            #decided t put the designs here, makes it more easy :)
            number_cards_designs = [f'\n┌─────────┐\n│{value}        │\n│    {symbol}    │\n│         │\n│    {symbol}    │   \n│        {value}│\n└─────────┘\n',
            f'\n┌─────────┐\n│{value}   {symbol}    │\n│         │\n│    {symbol}    │\n│         │   \n│    {symbol}   {value}│\n└─────────┘\n',
            f'\n┌─────────┐\n│{value}        │\n│  {symbol}   {symbol}  │\n│         │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
            f'\n┌─────────┐\n│{value}        │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
            f'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
            f'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
            f'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│{symbol}   {symbol}    │\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
            f'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│{symbol}   {symbol}   {symbol}│\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
            f'\n┌─────────┐\n│{value} {symbol} {symbol}   │\n│  {symbol}   {symbol}  │\n│ {symbol}     {symbol} │\n│  {symbol}   {symbol}  │   \n│   {symbol} {symbol} {value}│\n└─────────┘\n']
            string_representation = number_cards_designs[value-2]
        #For figure cards the value is always 10
        elif random_number > 11:
            value = 10
            symbol = random.choice(Card.__symbols)
            figure = random.choice(Card.__figures)
            string_representation = f'\n┌─────────┐\n│{figure}       {symbol}│\n│    {symbol}    │\n│    {figure}    │\n│    {symbol}    │\n│{symbol}       {figure}│\n└─────────┘         \n'
        #I decided an ACE will define it's value when the instance it's created by the next_turn method from player
        else:
            value = [1,11]
            figure = "A"
            symbol = random.choice(Card.__symbols)
            string_representation = f'\n┌─────────┐\n│{figure}       {symbol}│\n│    {symbol}    │\n│    {figure}    │\n│    {symbol}    │\n│{symbol}       {figure}│\n└─────────┘         \n'
        
        #Asignation of values
        self.string_representation = string_representation
        self.value = value

def main():
    create_new_players()
    while True:
        game_turn()
        players_states = []
        str_win = False
        for player in Player.instances:
            if isinstance(player.state,str):
                c()
                str_win = True
                print(f"{player.name} is the winner!")
                s(5)
                c()
                break
            #This part adds the state of playesrs into a list, if there is 0 False states
            try:#that means there are only standing players so the one closer to 21 wins
             players_states.append(player.state)
            except:
                break
            if players_states.count(False) < 1:
                players_states = True #This has to be boolean pls, so this works
        if str_win:
            break
        if isinstance(players_states,list):
            continue
        elif isinstance(players_states,bool):
            #All the values of the players,0 saves the names, 1 saves the value
            player_values = [[],[]]
            for player in Player.instances:
                 player_values[0].append(player.name)
                 player_values[1].append(player.total_value)
            c()
            #player_values[0].index(player_values[1].index(max(player_values[1])))
            print(f"{player_values[0][player_values[1].index(max(player_values[1]))]} is the winner!")
            s(5)
            c()
            break

#Allows to create infinite amount of players, but usually it will be less than 1
def create_new_players():
    while True:
        print("Select an option:\n1- Create player\n2- Start game")
        choice = int(input("> "))
        if choice < 2:
            s(1)
            c()
            print("Enter the name of the new player:")
            player_name = input("> ")
            s(1)
            c()
            Player(player_name)
            print(f"New player {player_name} was added")
            s(2)
            c()
        else:
            s(1)
            c()
            print("Starting game...")
            s(2)
            c()
            break

#Like a round, it gives a turn to all players with a True state 
def game_turn():
    for player in Player.instances:
        if player.state:
            break

        if player.total_value < 1:
            player.get_new_card()
            player.get_new_card()

        while True:
            print(f"{player.name}, choose an option:\n1- See cards and value\n2- Take a card\n3-Stand")
            choice = int(input("> "))
            s(1)
            c()
            if choice == 1:
                for card in player.cards:
                    print(card)
                print(f"Your total value is {player.total_value}")
                s(7.5)
                c()
            elif choice == 2:
                new_card = player.get_new_card()
                print(f"{new_card.string_representation}\nNew total value of {player.total_value}")
                if player.total_value > 21:
                    del Player.instances[Player.instances.index(player)]
                    print(f"{player.name} has lost!")
                elif player.total_value == 21:
                    player.state = ""
                s(3)
                c()
                break
            elif choice == 3:
                player.state = True
                break
    

if __name__ == "__main__":
    main()