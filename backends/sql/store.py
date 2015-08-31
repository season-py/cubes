from utils.ext import ExtMeta
from store import Store

class SqlStore(Store, metaclass=ExtMeta):

    _ext_type = 'store'

    def __init__(self):
        pass
