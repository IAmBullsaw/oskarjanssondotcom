import unittest
from card import Card

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card('title','description','text',[('image_path','alt text')],True)

    def test_id(self):
        # Check it is the first one created
        current_id = Card._cid
        card = Card('title','description','text',[('image_path','alt text')],True)
        self.assertEqual(card._id, current_id,'Failed first')
        current_id = Card._cid
        card = Card('title','description','text',[('image_path','alt text')],True)
        self.assertEqual(card._id, current_id, 'Failed second')

    def test_init_fail(self):
        with self.assertRaises(TypeError):
            Card(1,'description','text',[('image_path','alt text')],True)
        with self.assertRaises(TypeError):
            Card('title',1,'text',[('image_path','alt text')])
        with self.assertRaises(TypeError):
            Card('title','description',1,[('image_path','alt text')],True)
        with self.assertRaises(TypeError):
            Card('title','description','text',1,True)
        with self.assertRaises(TypeError):
            Card('title','description','text','',True)
        with self.assertRaises(TypeError):
            Card('title','description','text',[('image_path','alt text')],'haha')
        with self.assertRaises(TypeError):
            Card('title','description','text',[('image_path','alt text')],True,'hej')

    def test_unread(self):
        self.assertEqual(self.card._unread,True)
        self.assertEqual(self.card.is_unread(),True)
        self.card.toggle_unread()
        self.assertEqual(self.card._unread,False)
        self.assertEqual(self.card.is_unread(),False)
        self.card.toggle_unread()
        self.assertEqual(self.card._unread,True)
        self.assertEqual(self.card.is_unread(),True)

    def test_getters(self):
        self.assertEqual(self.card.get_header_image(),('image_path','alt text'))
        # By definition indexes out of range returns default image
        self.assertEqual(self.card.get_image_at(42),('default.png','Missing image.'))

if __name__ == '__main__':
    unittest.main()
