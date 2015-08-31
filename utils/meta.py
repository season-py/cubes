import json


def read_model_metadata(model=None, encoding='utf-8'):
    assert (model and isinstance(model, str))
    model_metadata = {}
    with open(model, encoding=encoding) as fd:
        model_metadata = json.load(fd)
    return model_metadata
