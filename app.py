import sys
import handlers
import tcelery
from tornado import web
from tornado import ioloop
from tornado import httpserver
from tornado import log
from tornado import options
from settings import SETTINGS
from utils.urlmap import urlmap
from tasks.celery import app

tcelery.setup_nonblocking_producer(celery_app=app)
handlers.initiate()
log.logging.basicConfig(level=log.logging.INFO)


def runserver():
    log.logging.info(urlmap.handlers)
    application = web.Application(urlmap.handlers[0], **SETTINGS)
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8887)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    runserver()
