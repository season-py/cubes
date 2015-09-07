import backends
from configparser import ConfigParser
from collections import defaultdict
from utils.meta import read_model_metadata
from utils.ext import extmanager 
from cube import Cube, Dimension


class Workspace(object):

    _cubes = defaultdict(lambda: None)
    _stores = defaultdict(lambda: None)
    _config = defaultdict(lambda: defaultdict(lambda: None))

    def __init__(self, slicer_conf='slicer.ini'):
        self._init_slicer(conf=slicer_conf)
        self._init_stores()
        self._import_model()

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
            self._stores[store_key] = self._register_store(store_key, dict(_.items(store)))

    def _register_store(self, store_key, conf):
        store_type = conf['type']
        store_conf = conf['url']
        return extmanager.get(store_type, 'store')(store_key, store_conf)

    def _import_model(self, model='models.json'):
        metadata = read_model_metadata(model=model)
        for d_metadata in metadata['dimensions']:
            Dimension.from_metadata(d_metadata)
        for c_metadata in metadata['cubes']:
            cube = Cube.from_metadata(c_metadata, ctx=self)
            self._cubes[cube.name] = cube

    def browser(self, cube_name):
        cube = self._cubes[cube_name]
        if not cube:
            pass
        store_type = cube.store
        return extmanager.get(store_type, 'browser', cube=cube)

    def list_cubes(self):
        return list(self._cubes.keys())

