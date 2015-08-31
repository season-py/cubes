from collections import defaultdict

class ModelAttrError(Exception):
    pass


class ModelObj(object):

    @classmethod
    def from_metadata(cls, metadata):
        return cls(**metadata)

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            if key in self._attributes:
                setattr(self, key, val)
            else:
                raise ModelAttrError('object {0} has no attribute "{1}"'.format(self.__class__.__name__, key))
        self._init_lazy()

    def _init_lazy(self):
        self.label = self.label or self.name
        if self.dimensions:
            self.dimensions = [self._create_dimension(dim) for dim in self.dimensions]
 
    def _create_dimension(self, dim):
        if isinstance(dim, str):
            return self._instances[dim]
        elif isinstance(dim, dict):
            return Dimension.from_metadata(dim)

    def __getattr__(self, key):
        if key.startswith('__') and key.endswith('__'):
            val = super(ModelObj).__getattr__(key)
        try:
            val = getattr(self.__dict__, key)
        except AttributeError, e:
            val = None
        return val


class Dimension(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'levels', 'hierarchies', 'master', 'description'}


class Measure(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'function'}


class Cube(object):

    _instances = {}
    _attributes = {'name', 'label', 'store', 'fact', 'dimensions', 'measures', 'aggregates', 'mappings', 'joins'}

