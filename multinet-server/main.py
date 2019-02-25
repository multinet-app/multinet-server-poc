import os
import logging
logger = logging.getLogger(__name__)

from aiohttp import web
from routes import setup_routes
from arango import ArangoClient

import config
config.init()

logger.debug('Initializing app')
app = web.Application()
app['arango'] = ArangoClient(
    host=os.environ["ARANGO_HOST"],
    port=int(os.environ["ARANGO_PORT"]))
logger.debug('Setting up routes')
setup_routes(app)
logger.info('Starting web server')
web.run_app(app)
