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
  db_name, coll_name = graph.split('/')
  db = client.db(db_name, username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
  coll = db.collection(coll_name)

  cursor = coll.all()
  nodes = [node for node in cursor]
  return nodes

async def allEdges(root, info, graph, id):
  db_name, coll_name = graph.split('/')
  db = client.db(db_name, username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
  coll = db.collection(coll_name)
  info.context['database'] = db_name

  cursor = coll.all()
  edges = [edge for edge in cursor][0:5]
  return edges

async def edgeSource(edge, info):
    db = client.db(info.context['database'], username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
    coll_name, key = edge['_from'].split('/')
    coll = db.collection(coll_name)
    logging.debug("%s %s %s" % (info.context['database'], coll_name, key))
    return coll.get(key)

async def edgeTarget(edge, info):
    db = client.db(info.context['database'], username='root', password=os.environ['MULTINET_ROOT_PASSWORD'])
    coll_name, key = edge['_to'].split('/')
    coll = db.collection(coll_name)
    logging.debug("%s %s %s" % (info.context['database'], coll_name, key))
    return coll.get(key)
