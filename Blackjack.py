import random

class Player:
    def __init__(self,name:str,money:float,cards=[]):
        #Assertions
        assert money >= 0, "money attribute can't be negative"
        
        #Values asignation:
        self.name = name
        self.money = money
        self.cards = cards

class Card:
    __symbols = ["♥","♦","♣","♠"]
    __figures = ["K","Q","J"]

    def __init__(self,string_representation="",value=0):
        random_number = random.randint(2,14)
        #For number cards we assign the value generated 
        if random_number < 11:
            value = random_number
            symbol = random.choice(Card.__symbols)
            #Sorry, i dont know how to shorten the design for every number card, also, i just
            #decided t put the variable here, makes it more easy
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
        
        #Asigantion of values
        self.string_representation = string_representation
        self.value = value

carta1 = Card()
print(carta1.string_representation)