
class Cube(object):

    @classmethod
    def from_metadata(cls, metadata, store):
        assert name in metadata
        dimensions_links = metadata.pop('dimensions', [])
        aggregates = metadata.pop('aggregates', [])
        measures = metadata.pop('measures', [])

    def __init__(self):
        pass
