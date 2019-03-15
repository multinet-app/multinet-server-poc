import os
import logging
logger = logging.getLogger(__name__)

from arango import ArangoClient
client = ArangoClient(
    host=os.environ["ARANGO_HOST"],
    port=int(os.environ["ARANGO_PORT"]))

def meta_resolve_dict(fields, key, default=None, alias=None):
    if alias:
        fields[key].resolve = lambda obj, *_: obj.get(alias, default)
    else:
        fields[key].resolve = lambda obj, *_: obj.get(key, default)

async def allNodes(root, info, graph, id):
  logging.debug('hello')
  db_name, coll_name = graph.split('/')
  db = client.db(db_name, username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
  coll = db.collection(coll_name)

  cursor = coll.all()
  nodes = [node for node in cursor]
  return nodes

async def allEdges(root, info, graph, id):
  logging.debug('hello')
  db_name, coll_name = graph.split('/')
  db = client.db(db_name, username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
  coll = db.collection(coll_name)

  cursor = coll.all()
  edges = [edge for edge in cursor]
  return edges

async def edgeSource(edge, info):
    logging.debug(info.context)
    return dict(
        _key='SLC',
        name='Salt Lake City International Airport',
        city='Salt Lake City',
        state='UT',
        country='USA',
        lat=5.0,
        long=4.3,
        vip=false
    )

async def edgeTarget(edge, info):
    logging.debug(info.context)
    return dict(
        _key='SLC',
        name='Salt Lake City International Airport',
        city='Salt Lake City',
        state='UT',
        country='USA',
        lat=5.0,
        long=4.3,
        vip=false
    )
