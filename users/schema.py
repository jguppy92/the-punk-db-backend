import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude = ('password', )

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    logged_in_user = graphene.Field(UserType)

    def resolve_all_users(self, info):
        return get_user_model().objects.all()

    @login_required
    def resolve_logged_in_user(self, info):
        return info.context.user

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, username, password):
        user = get_user_model()
        new_user = user(email=email, username=username)
        new_user.set_password(password)
        new_user.save()
        return CreateUser(user=new_user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
