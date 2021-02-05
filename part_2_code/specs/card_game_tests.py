import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
            self.card1 = Card("Hearts", 1)
            self.card2 = Card("Clubs", 3)
            self.cardgame = CardGame
            self.cards = [self.card1, self.card2]

    
    def test_check_for_ace(self):
        result = self.cardgame.check_for_ace(self, self.card2)
        self.assertEqual(False, result)
        

    def test_highest_card(self):
        result = self.cardgame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, result)
    
    def test_cards_total(self):
        result = self.cardgame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 4", result)
    
        
        
    

        
