import logging
logger = logging.getLogger(__name__)

import resolvers

from graphql import build_schema, extend_schema, parse

schema = build_schema("""
    type Query {
        allNodes(graph: String!, id: String=""): [Node!]!
        allEdges(graph: String!, id: String=""): [Edge!]!
    }

    type Node {
        key: String!
        outgoing(edges: [String]): [Edge!]
        incoming(edges: [String]): [Edge!]
    }

    type Edge {
        key: String!
        source: Node!
        target: Node!
    }
""")

schema = extend_schema(schema, parse("""
    extend type Node {
        name: String
        city: String
        state: String
        country: String
        lat: Float
        long: Float
        vip: Boolean
    }

    extend type Edge {
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

fields = schema.get_type('Node').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
fields['outgoing'].resolve = resolvers.nodeOutgoing
fields['incoming'].resolve = resolvers.nodeIncoming

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
