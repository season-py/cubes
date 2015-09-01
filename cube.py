# coding=utf-8
# author=haishan09@gmail.com


class ModelAttrError(Exception):
    pass


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
            self.dimensions = [self._create_dimension(d) for d in self.dimensions]
        if self.measures:
            self.measures = [self._create_measure(m) for m in self.measures]

    def _create_dimension(self, dim):
        if isinstance(dim, unicode):
            return Dimension._instances[dim]
        elif isinstance(dim, dict):
            return Dimension.from_metadata(dim)

    def _create_measure(self, measure):
        if isinstance(measure, unicode):
            return Measure._instances[measure]
        elif isinstance(measure, dict):
            return Measure.from_metadata(measure)

    def __getattr__(self, key):
        if key.startswith('__') and key.endswith('__'):
            val = super(ModelObj).__getattr__(key)
        try:
            val = getattr(self.__dict__, key)
        except AttributeError:
            val = None
        return val


class Dimension(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'levels', 
                   'hierarchies', 'category', 'master', 
                   'description'}


class Measure(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'function'}


class Cube(ModelObj):

    _instances = {}
    _attributes = {'name', 'label', 'store', 
                   'fact', 'dimensions', 'measures', 
                   'aggregates', 'mappings', 'joins'}

