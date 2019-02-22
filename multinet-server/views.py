from aiohttp import web, ClientSession

from arango import (
    ArangoClient
)

import json
import logging
logger = logging.getLogger(__name__)

async def index(request):
    logger.debug('Accessing index')
    client = ArangoClient(protocol='http', host='localhost', port=8529) # to be configs
    sys_db = client.db('_system', username='root', password='openSesame')
    dbs = sys_db.databases()
    logger.info('Response: %s' % dbs)
    return web.Response(text=json.dumps(dbs, indent=4))
