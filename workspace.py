from configparser import ConfigParser
from collections import defaultdict
from utils.meta import read_model_metadata


class Workspace(object):

    _stores = defaultdict(lambda: None)
    _config = defaultdict(lambda: defaultdict(lambda: None))

    def __init__(self, conf='slicer.ini'):
        self._init_slicer(conf=conf)
        self._init_stores()

    def _init_slicer(self, conf=None):
        _ = ConfigParser()
        if isinstance(_, str):
            _.read(conf)
        for sec in _.sections():
            for opt, val in _.items(sec):
                self._config[sec][opt] = val

    def _init_stores(self, conf='stores.ini'):
        _ = ConfigParser()
        stores = self._config['workspace']['stores_files'] or conf
        _.read(stores)
        for store in _.sections():
            store_key = store.split(' ')[-1]
            self._config['store'][store_key] = dict(_.items(store))

    def _register_store(self, name, conf):
        pass

    def _import_model(self, model='models.json'):
        read_model_metadata(model=model)

    def browser(self, cube):
        pass

    def list_cubes(self):
        pass
