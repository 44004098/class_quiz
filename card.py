# Name: Kiana 

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return 'value={self.value},suit={self.suit}'
    def __str__(self):
        return f"{self.value} of {self.suit}"
    def __eq__(self, other):
        if Card((self.value) = (self.other))
        return True 


    """class representing a simple Neapolitan card. Holds a 
    value and a suit"""
    
