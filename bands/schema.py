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
            "image",
            "biography"
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
    filter_albums = graphene.Field(AlbumType, id=graphene.Int())

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
        country = graphene.String(required=False)
        city = graphene.String(required=False)
        image = graphene.String(required=False)
        biography = graphene.String(required=False)

    band = graphene.Field(BandType)

    @classmethod
    def mutate(
        cls,
        root,
        info,
        name,
        id,
        members,
        country,
        city,
        image,
        biography
        ):
        band = Band.objects.get(id=id)
        band.name = name
        if bool(members) is True:
            band.members = members
        if bool(country) is True:
            band.country = country
        if bool(city) is True:
            band.city = city
        if bool(image) is True:
            band.image = image
        if bool(biography) is True:
            band.biography = biography
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

class AlbumCreate(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        band_id = graphene.ID(required=True)
        tracklist = graphene.List(graphene.String,default_value=False)

    album = graphene.Field(AlbumType)

    @classmethod
    def mutate(cls, root, info, title, tracklist, band_id):
        album = Album(
            title=title,
            tracklist=tracklist,
            artist=Band.objects.get(id=band_id)
            )
        album.save()
        return AlbumCreate(album=album)

class AlbumUpdate(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        tracklist = graphene.List(graphene.String,default_value=False)

    album = graphene.Field(AlbumType)

    @classmethod
    def mutate(cls, root, info, title, id, tracklist):
        album = Album.objects.get(id=id)
        album.title = title
        if bool(tracklist) is True:
            album.tracklist = tracklist
        album.save()
        return AlbumUpdate(album=album)

class AlbumDelete(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    album = graphene.Field(AlbumType)

    @classmethod
    def mutate(cls, root, info, id):
        album = Album.objects.get(id=id)
        album.delete()
        return AlbumDelete(album=album)

class Mutation(graphene.ObjectType):

    create_band = BandCreate.Field()
    update_band = BandUpdate.Field()
    delete_band = BandDelete.Field()
    create_album= AlbumCreate.Field()
    update_album = AlbumUpdate.Field()
    delete_album = AlbumDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
