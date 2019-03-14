import logging
logger = logging.getLogger(__name__)

import models

from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLList
)

node = GraphQLObjectType(
  name='Node',
  fields={
    'id': GraphQLField(
      type=GraphQLString,
      resolver=models.node_id
    )
  }
)

schema = GraphQLSchema(
  query=GraphQLObjectType(
    name='RootQueryType',
    fields={
      'allNodes': GraphQLField(
        type=GraphQLList(node),
        resolver=models.allNodes
      )
    }
  )
  # mutation=GraphQLObjectType(...),
  # subscription=GraphQLObjectType(...)
)
