import logging
logger = logging.getLogger(__name__)

import resolvers

from graphql import build_schema, extend_schema, parse

schema = build_schema("""
    type Query {
        allNodes(graph: String!, id: String=""): [Node!]!
        allEdges(graph: String!, id: String=""): [Edge!]!
    }

    interface Attributes {
        key: String
    }

    type Node {
        key: String!
        outgoing(edges: [String]): [Edge!]
        incoming(edges: [String]): [Edge!]
        attributes: Attributes!
    }

    type Edge {
        key: String!
        source: Node!
        target: Node!
        attributes: Attributes!
    }
""")

schema = extend_schema(schema, parse("""
    type airports implements Attributes {
        key: String
        name: String
        city: String
        state: String
        country: String
        lat: Float
        long: Float
        vip: Boolean
    }

    type flights implements Attributes {
        key: String
        Year: Int
        Month: Int
        Day: Int
        DayOfWeek: Int
        DepTime: Int
        ArrTime: Int
        DepTimeUTC: String
        ArrTimeUTC: String
        UniqueCarrier: String
        FlightNum: Int
        TailNum: String
        Distance: Int
    }
"""))

fields = schema.query_type.fields
fields['allNodes'].resolve = resolvers.allNodes
fields['allEdges'].resolve = resolvers.allEdges

schema.get_type('Attributes').resolve_type = lambda entity, *_: entity['_id'].split('/')[0]

fields = schema.get_type('Node').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
fields['outgoing'].resolve = resolvers.nodeOutgoing
fields['incoming'].resolve = resolvers.nodeIncoming
fields['attributes'].resolve = resolvers.attributes

fields = schema.get_type('airports').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
resolvers.meta_resolve_dict(fields, 'name')
resolvers.meta_resolve_dict(fields, 'city')
resolvers.meta_resolve_dict(fields, 'state')
resolvers.meta_resolve_dict(fields, 'country')
resolvers.meta_resolve_dict(fields, 'lat')
resolvers.meta_resolve_dict(fields, 'long')
resolvers.meta_resolve_dict(fields, 'vip')

fields = schema.get_type('Edge').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
fields['source'].resolve = resolvers.edgeSource
fields['target'].resolve = resolvers.edgeTarget
fields['attributes'].resolve = resolvers.attributes

fields = schema.get_type('flights').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
resolvers.meta_resolve_dict(fields, 'Year')
resolvers.meta_resolve_dict(fields, 'Month')
resolvers.meta_resolve_dict(fields, 'Day')
resolvers.meta_resolve_dict(fields, 'DayOfWeek')
resolvers.meta_resolve_dict(fields, 'DepTime')
resolvers.meta_resolve_dict(fields, 'ArrTime')
resolvers.meta_resolve_dict(fields, 'DepTimeUTC')
resolvers.meta_resolve_dict(fields, 'ArrTimeUTC')
resolvers.meta_resolve_dict(fields, 'UniqueCarrier')
resolvers.meta_resolve_dict(fields, 'FlightNum')
resolvers.meta_resolve_dict(fields, 'TailNum')
resolvers.meta_resolve_dict(fields, 'Distance')
