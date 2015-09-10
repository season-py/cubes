from browser import Browser


class SqlBrowser(Browser):

    _ext_type = 'browser'

    def __init__(self, cube=None, store=None):
        super(SqlBrowser, self).__init__(cube=cube, store=store)

    def aggregate(self):
        pass
