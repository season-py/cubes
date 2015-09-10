# coding=utf-8
# author=haishan09@gmail.com
import copy


class ModelAttrError(Exception):
    pass

def create_modelobj(obj, cls=None):
    if isinstance(obj, str):
        if hasattr(cls, '_instances'):
            return cls._instances[obj]
        else:
            return cls(name=obj)
    elif isinstance(obj, dict):
        return cls.from_metadata(dim)


class ModelObj(object):

    @classmethod
    def from_metadata(cls, metadata):
        if 'name' in metadata:
            name = metadata['name']
            if name not in cls._instances:
                instance = cls(**metadata)
                cls._instances[name] = instance
            else:
                instance = cls._instances[name]
        else:
            instance = cls(**metadata)
        return instance

    def __init__(self, **kwargs):
        if 'metadata' in kwargs:
            self.metadata = kwargs['metadata']
        else:
            self.metadata = kwargs
        for key, val in kwargs.items():
            if key in self._attributes:
                setattr(self, key, val)
            else:
                raise ModelAttrError('object {0} has no attribute "{1}"'.format(self.__class__.__name__, key))
        self._init_lazy()

    def _init_lazy(self):
        self.label = self.label or self.name
        if self.dimensions:
            self.dimensions = map(lambda d: create_modelobj(d, cls=Dimension), self.dimensions)
        if self.measures:
            self.measures = map(lambda m: create_modelobj(m, cls=Measure), self.measures)
        if self.levels:
            self.levels = map(lambda l: create_modelobj(l, cls=Level), self.levels)

    def __getattr__(self, key):
        if key.startswith('__') and key.endswith('__'):
            val = super(ModelObj).__getattr__(key)
        try:
            val = getattr(self.__dict__, key)
        except AttributeError:
            val = None
        return val

    def clone(self):
        return self.from_metadata(copy.deepcopy(self.metadata))

    def __eq__(self, other):
        return self.metadata == other.metadata


class Dimension(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'levels', 
                   'hierarchies', 'category', 'master', 
                   'description'}

class Level(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'attributes'}

class Hierarchy(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'levels'}


class Measure(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'function', 
                   'order', 'aggregates', 'expression',
                   'window_size', 'description', 'format'}


class Cube(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'store', 
                   'fact', 'dimensions', 'measures', 
                   'aggregates', 'mappings', 'joins'}

