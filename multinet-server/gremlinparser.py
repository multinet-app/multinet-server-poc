import logging
logger = logging.getLogger(__name__)

def switch_parse(data):
    if isinstance(data, dict):
        parser = registry.get(data.get('@type', None), parse_value)
        return parser(data if data.get('@value', None) is None else data['@value'])
    else:
        return data

def parse_response(data):
    logger.debug('parse response: %s' % data)
    core_data = data['result']['data']
    return switch_parse(core_data)

def parse_list(data):
    logger.debug('parse_list: %s' % data)
    for item in data:
        logger.debug('item: %s' % item)
    return [switch_parse(item) for item in data]

def parse_vertex(data):
    logger.debug('parse_vertex: %s' % data)
    return dict(
        id=switch_parse(data['id']),
        label=data['label'],
        properties={key:parse_list(value) for (key, value) in data['properties'].items()}
    )

def parse_vertex_property(data):
    logger.debug('parse_vertex_property: %s' % data)
    return dict(
        id=switch_parse(data['id']),
        label=switch_parse(data['label']),
        value=switch_parse(data['value'])
    )

def parse_value(data):
    return data


registry = {
    'g:List': parse_list,
    'g:Vertex': parse_vertex,
    'g:VertexProperty': parse_vertex_property,
    'g:Int64': parse_value
}
