import graphene

import bands.schema
import users.schema

class Query(bands.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(bands.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
