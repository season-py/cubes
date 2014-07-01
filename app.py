import handlers
from tornado import web
from tornado import ioloop
from tornado import httpserver
from tornado import log
from tornado import options
from settings import SETTINGS
from utils.urlmap import urlmap

handlers.initiate()
log.logging.basicConfig(level=log.logging.DEBUG)

def runserver():
    log.logging.info(urlmap.handlers)
    application = web.Application(urlmap.handlers[1], **SETTINGS)
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888) 
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    runserver()
