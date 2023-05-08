import graphene
from graphene_django import DjangoObjectType
from .models import Band

class BandsType(DjangoObjectType):
    class Meta:
        model = Band
        fields = (
            "id", 
            "name", 
            "country", 
            "city",
            "members",
            "releases",
            "image"
        )

class Query(graphene.ObjectType):

    all_bands = graphene.List(BandsType)

    def resolve_all_bands(root, info):
        return Band.objects.all()



schema = graphene.Schema(query=Query)
