from collections import defaultdict


def load_module(path):
    __import__(path)
        
class ExtMeta(type):

    _collections = defaultdict(lambda: defaultdict(lambda: None))

    def __new__(cls, name, bases, dct):
        cls_instance = type.__new__(cls, name, bases, dct)
        if '_ext_type' in dct:
            cls_mod = cls_instance.__module__.split('.')[-2]
            cls_name = dct['_ext_type']
            ExtMeta._collections[cls_mod][cls_name] = cls_instance
        return cls_instance

class ExtManager(object, metaclass=ExtMeta):

    def __init__(self):
        self._collections = ExtManager._collections

    def get(self, _type, _ext_type):
        mod = self._collections[_type][_ext_type]
        if not mod:
            load_module('.'.join(['backends', _type, _ext_type]))
        return self._collections[_type][_ext_type]

extmanager = ExtManager()
