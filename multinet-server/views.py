from aiohttp import web, ClientSession

from aiogremlin import DriverRemoteConnection, Graph

import json
import logging
logger = logging.getLogger(__name__)

async def index(request):
    logger.debug('Accessing index')
    remote_connection = await DriverRemoteConnection.open('ws://localhost:8182/gremlin', 'graph')
    g = Graph().traversal().withRemote(remote_connection)
    vertices = await g.V().toList()
    vertices = [str(v) for v in vertices]
    logger.info('Response: %s' % vertices)
    return web.Response(text=json.dumps(vertices, indent=4))
