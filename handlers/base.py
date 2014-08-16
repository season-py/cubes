from tornado import web


class AccessDeny(Exception):
    pass


class Context(dict):

    def __getattr__(self, key):
        if not key.startswith('__'):
            return self[key]
        else:
            super(Context, self).__getattr__(key)

    def __setattr__(self, key, value):
        self[key] = value


class BaseHandler(web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def prepare(self):
        self.context = Context()
