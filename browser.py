from utils.ext import ExtMeta


class Browser(object, metaclass=ExtMeta):
    def __init__(self, cube=None, store=None):
        self.cube = cube
        self.store = store

    def aggerate(self, aggregates=None, drilldowns=None, cuts=None, 
                 order=None, page=None, page_size=None, **options):
        if aggregates:
            map(self.cube., aggregates)

    def fact(self):
        pass

class Cell(object):

    pass
