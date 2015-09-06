from store import Store
from sqlalchemy import create_engine

class SqlStore(Store):

    _ext_type = 'store'

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.engine = None

    def _check_engine(self):
        if not self.engine:
            self.engine = create_engine(self.url)

