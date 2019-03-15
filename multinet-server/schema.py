import logging
logger = logging.getLogger(__name__)

import resolvers

from graphql import build_schema

schema = build_schema("""
    type Query {
        allNodes(graph: String!, id: String=""): [Node!]!
    }

    type Node {
        key: String!
    }
""")

fields = schema.query_type.fields
fields['allNodes'].resolve = resolvers.allNodes

fields = schema.get_type('Node').fields
resolvers.meta_resolve_dict(fields, 'key', alias='_key')
