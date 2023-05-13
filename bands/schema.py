import graphene
from graphene_django import DjangoObjectType
from .models import Band, Album

class BandType(DjangoObjectType):
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

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = (
            "id",
            "title",
            "country",
            "image",
            "year",
            "variants",
            "tracklist",
            "genre",
            "on_sale",
            "artist"
        )

class Query(graphene.ObjectType):

    all_bands = graphene.List(BandType)
    all_albums = graphene.List(AlbumType)

    def resolve_all_bands(self, info):
        return Band.objects.all()
    def resolve_all_albums(self, info):
        return Album.objects.all()



schema = graphene.Schema(query=Query)
