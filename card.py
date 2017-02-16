class Card:
    """ The class to hold the information for a project or similar """
    _cid = 0
    def _get_new_id():
        """ Return a new id """
        Card._cid = Card._cid + 1
        return Card._cid - 1

    def __init__(self, title, description, text, images, unread = False, cid = None ):
        """ Checks for correct parameter types and sets images to default if none passed """
#        message = 'Failed to initialize Card: '
        # Assert types are correct
        if not isinstance(title, str):
#            logging.error(message + 'title is not a str')
            raise TypeError
        if not isinstance(description, str):
#            logging.error(message + 'description is not a str')
            raise TypeError
        if not isinstance(text, list):
#            logging.error(message + 'text is not a list')
            raise TypeError
        if not isinstance(images, list):
#            logging.error(message + 'images is not a list')
            raise TypeError
        if not isinstance(unread, bool):
#            logging.error(message + 'unread is not a bool')
            raise TypeError
        if cid is not None and not isinstance(cid, int):
#            logging.error(message + 'cid is not a int')
            raise TypeError

        self._id = Card._get_new_id() if cid is None else cid
        self._title = title
        self._description = description
        self._text = text
        self._unread = unread

        # If we pass an empty list of images, we set it to default image.
        self._images = images if len(images) > 0 else [('default.png','Header image.')]

    def to_dict(self):
        d = {}
        d['_id'] = self._id
        d['_title'] = self._title
        d['_description'] = self._description
        d['_text'] = self._text
        d['_unread'] = self._unread
        d['_images'] = self._images
        return d

    def get_header_image(self):
        """ Header image is always the first image """
        return self._images[0]

    def get_image_at(self, index):
        """ if index is out of range then return Default image """
        return self._images[index] if index < len(self._images) else ('default.png','Missing image.')

    def is_unread(self):
        return self._unread

    def is_read(self):
        return not is_unread()

    def toggle_unread(self):
        self._unread = not self._unread
