import json
from card import Card
class Data:
    def __init__(self):
        self._cards = []

    def load_JSON(self,filename):
        """ Load entire Json db"""
        f = open(filename)
        data = json.load(f)
        self._cards = []
        for c in data:
            self._cards.append(Card(c['_id'], c['_title'], c['_description'], c['_headerhref'], c['_headeralt'], c['_content']))

    def get_cards(self):
        return self._cards
