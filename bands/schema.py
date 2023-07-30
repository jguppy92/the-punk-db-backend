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
    filter_bands = graphene.Field(BandType, id=graphene.Int())
    all_albums = graphene.List(AlbumType)
    filter_albums = graphene.List(AlbumType, id=graphene.Int())

    def resolve_all_bands(self, info):
        return Band.objects.all()
    def resolve_filter_bands(self, info, id):
        return Band.objects.get(pk=id)
    def resolve_all_albums(self, info):
        return Album.objects.all()
    def resolve_filter_albums(self, info, id):
        return Album.objects.filter(artist=id)

class BandCreate(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    band = graphene.Field(BandType)

    @classmethod
    def mutate(cls, root, info, name):
        band = Band(name=name)
        band.save()
        return BandCreate(band=band)

class BandUpdate(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        members = graphene.List(graphene.String,default_value=False)

    band = graphene.Field(BandType)

    @classmethod
    def mutate(cls, root, info, name, id, members):
        band = Band.objects.get(id=id)
        band.name = name
        if bool(members) is True:
            band.members = members
        band.save()
        return BandUpdate(band=band)

class BandDelete(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    band = graphene.Field(BandType)

    @classmethod
    def mutate(cls, root, info, id):
        band = Band.objects.get(id=id)
        band.delete()
        return BandDelete(band=band)

class Mutation(graphene.ObjectType):

    create_band = BandCreate.Field()
    update_band = BandUpdate.Field()
    delete_band = BandDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
