# Project Description

class InputAlreadyExists(Exception):
    pass
    
class Flashcard:
    def __init__(self, card, definition):
        self.card = card
        self.definition = definition

    def check(self, answer):
        if self.definition == answer:
            print(f'Correct!')
        else:
            print(f'Wrong. The right answer is "{self.definition}".')

    def __str__(self, seperator = '\n'):
        return f'Card:{seperator}{self.card}{seperator}Definition:{seperator}{self.definition}'

class Flashcards:
    def __init__(self, number_cards):
        self.cards = dict()
        self.build_deck(number_cards)
        self.check_cards(number_cards)

    def check_cards(self, number_cards):
        for i in range(number_cards):
            answer = input(f'Print the definition of "{self.cards[i].card}":\n')
            found = False
            for card in self.cards.values():
                if card.definition == answer and card.card != self.cards[i].card:
                    print(f'Wrong. The right answer is "{self.cards[i].definition}", but your definition is correct for "{card.card}".')
                    found = True
            if not found:
                self.cards[i].check(answer)
        

    def build_deck(self, number_of_cards):
        for i in range(number_of_cards):
            #print(f'The term for card #{i+1}:')
            #card_term = input()
            term = self.check_term_present(i)
            definition = self.check_definition_present(i)
            new_card = Flashcard(term, definition)
            self.cards[i] = new_card

    def check_term_or_definition_exists(self, identifier, value):
        if self.cards:
            if identifier == 'term':
                for card in self.cards.values():
                    if card.card == value:
                        raise InputAlreadyExists
                return value
            elif identifier == 'definition':
                for card in self.cards.values():
                    if card.definition == value:
                        raise InputAlreadyExists
                return value
        else:
            return value

    def check_term_present(self, i):
        print(f'The term for card #{i+1}:')
        while True:
            try:
                card_term = input()
                self.check_term_or_definition_exists('term', card_term)
                return card_term
            except InputAlreadyExists:
                print(f'The term "{card_term}" already exists. Try again:')
                continue
            
    def check_definition_present(self, i):
        print(f'The definition for card #{i+1}:')
        while True:
            try:
                card_definition = input()
                self.check_term_or_definition_exists('definition', card_definition)
                return card_definition
            except InputAlreadyExists:
                print(f'The definition "{card_definition}" already exists. Try again:')
                continue


def main():
    cards_number = int(input(f'Input the number of cards:\n'))
    deck = Flashcards(cards_number)      
main()
