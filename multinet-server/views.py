from aiohttp import web, ClientSession

from gremlinparser import parse_response

import json
import logging
logger = logging.getLogger(__name__)

async def index(request):
    logger.debug('Accessing index')
    async with ClientSession() as session:
        resp = await session.post("http://localhost:8182", data=json.dumps(dict(gremlin="system.graphs()")))
        raw_data = await resp.json()
        data = parse_response(raw_data)
        logger.info('Response: %s' % data)
    return web.Response(text=json.dumps(data, indent=4))
