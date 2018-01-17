from graphene_django import DjangoObjectType
import graphene

from . import models

UserModel = models.get_user_model()

class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Category(DjangoObjectType):
    class Meta:
        model = models.Category


class Question(DjangoObjectType):
    class Meta:
        model = models.Question


class Attempt(DjangoObjectType):
    class Meta:
        model = models.Solution


class Competition(DjangoObjectType):
    class Meta:
        model = models.Competition


class Query(graphene.ObjectType):
    users = graphene.List(User)
    competitions = graphene.List(Competition)

    def current_user(self, context):
        if context.user.is_authenticated:
            return context.user
        return None

    def resolve_users(self, args, context, info):
        # return UserModel.objects.all()
        return [ self.current_user(context) ]

    # def resolve_categories(self, args, context, info):
    #     usr = self.current_user(context)
    #     return Category.

schema = graphene.Schema(query=Query)