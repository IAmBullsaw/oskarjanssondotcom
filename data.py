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

    def add_card(self):
        title = input('Title: ')
        description = input('Description: ')
        text = []
        done = False
        print("enter 'q' when done...\n")
        while not done:
            inp = input('Text: ')
            if inp in ['q',':q']:
                done = True
            else:
                text.append(inp)
        print('Choose picture: ')
        header = 'default.png'
        print('default chosen. (To be implemented...)')
        print('\nThis is your current card:')
        print('0: Title:',title)
        print('1: Description',description)
        print('Text:')
        for i,part in enumerate(text):
            print(i+2,': ',part)
        print('Are you done? (y/e/q)')
        ans = input()
        if ans in ['y','yes','yeah','yup']:
            self._cards.append(Card(title, description, text, [header], True, len(self._cards) ))
            return True
        elif ans in ['e','edit','change']:
            ans = input('what to edit? (enter number): ')
            if ans is '0':
                print('i need to implement this')
            elif ans is '1':
                print('i really need to implement this')
        elif ans in ['q',':q','quit']:
            return False
            

if __name__ == '__main__':
    fd = input('Where is the file with all them cards?: ')
    d = Data()
    d.load_JSON(fd)
    ans = input('Wanna add a card? (y/n): ')
    import readline
    if ans in ['y','yes','yeah','yup']:
        added = d.add_card()
        if added:
            print('Saving...')
            d.save_JSON(d.get_cards(),fd)
        else:
            print('Aborting...')
    else:
        print('Bye')
