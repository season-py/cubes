
class ModelAttrError(Exception):
    pass

class ModelObj(object):

    @classmethod
    def from_metadata(cls, metadata):
        return cls(**metadata)

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            if key in self.attributes:
                setattr(self, key, val)
            else:
                raise ModelAttrError('object {0} has no attribute "{1}"'.format(self.__class__.__name__, key))

class Dimension(ModelObj):
    attributes = {'name', 'label', 'levels', 'hierarchies', 'master', 'description'}


class Measure(ModelObj):
    attributes = {'name', 'label', 'levels', 'hierarchies', 'master', 'description'}


class Cube(object):
    attributes = {'name', 'label', 'levels', 'hierarchies', 'master', 'description'}

