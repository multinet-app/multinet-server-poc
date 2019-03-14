import logging
logger = logging.getLogger(__name__)

def node_id(node, info):
  logging.debug(node)
  logging.debug(info.context.get('arango'))
  return node['id']

def allNodes(*args):
  return [
    dict(id='55'),
    dict(id='66')
  ]
