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
            self._cards.append(Card(c['_title'], c['_description'], c['_text'], c['_images'], c['_unread'], c['_id']))

    def save_JSON(self,cards,filename):
        l = []
        for c in cards:
            l.append(c.to_dict())

        with open(filename,'w') as f:
            json.dump(l,f)

    def get_cards(self):
        return self._cards
