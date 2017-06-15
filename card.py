class Card:
    """ The class to hold the information for a project or similar """
    def __init__(self, cid, title, description, headerhref, headeralt, content):
        """ Checks for correct parameter types and sets images to default if none passed """
        # message = 'Failed to initialize Card: '
        # TODO: remake these
        """
        # Assert types are correct
        if not isinstance(title, str):
            logging.error(message + 'title is not a str')
            raise TypeError
        if not isinstance(description, str):
            logging.error(message + 'description is not a str')
            raise TypeError
        if not isinstance(text, list):
            logging.error(message + 'text is not a list')
            raise TypeError
        if not isinstance(images, list):
            logging.error(message + 'images is not a list')
            raise TypeError
        if not isinstance(unread, bool):
            logging.error(message + 'unread is not a bool')
            raise TypeError
        if cid is not None and not isinstance(cid, int):
            logging.error(message + 'cid is not a int')
            raise TypeError
        """

        self._id = cid
        self._title = title
        self._description = description
        self._content = content
        self._headerhref = headerhref
        self._headeralt = headeralt

    def to_dict(self):
        d = {}
        d['_id'] = self._id
        d['_title'] = self._title
        d['_description'] = self._description
        d['_headerhref'] = self._headerhref
        d['_headeralt'] = self._headeralt
        d['_content'] = self._content
        return d

    def get_header_image(self):
        """ Header image is always the first image """
        return self._headerhref
