import graphene
from graphene_django import DjangoObjectType
from .models import Bands

class BandsType(DjangoObjectType):
    class Meta:
        model = Bands
        fields = ("id", "name", "country", "city")

class Query(graphene.ObjectType):

    all_bands = graphene.List(BandsType)

    def resolve_all_bands(root, info):
        return Bands.objects.all()



schema = graphene.Schema(query=Query)
