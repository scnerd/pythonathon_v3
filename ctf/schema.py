import graphene
from graphene_django import DjangoObjectType

from . import models

UserModel = models.get_user_model()


def current_user(info):
    usr = info.context.user
    return usr if usr.is_authenticated else None


def add_current_user(f):
    import functools
    @functools.wraps(f)
    def inner(self, info):
        return f(self, current_user(info), info)

    return inner


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        only_fields = ('id', 'username')

    @add_current_user
    def resolve_solutions(self, usr, info):
        # Don't allow viewing of other users' solutions
        if usr.id == self.id:
            return [sol for sol in self.solutions.all() if sol.question.is_viewable(usr)]
        return []

    @add_current_user
    def resolve_questions_attempted(self, usr, info):
        return [q for q in self.questions_attempted.all() if q.is_viewable(usr)]


class Category(DjangoObjectType):
    class Meta:
        model = models.Category
        only_fields = ('id', 'name', 'competition', 'questions')

    @add_current_user
    def resolve_questions(self, usr, info):
        return [q for q in self.questions.all() if q.is_viewable(usr)]


class Question(DjangoObjectType):
    class Meta:
        model = models.Question
        only_fields = ('id', 'name', 'full_text', 'points', 'hint', 'category', 'requires', 'files', 'solvers', 'case_sensitive')

    @add_current_user
    def resolve_hint(self, usr, info):
        self.mark_hint_used(usr)
        return self.hint


class Attempt(DjangoObjectType):
    class Meta:
        model = models.Solution
        only_fields = ('id', 'name', 'fullText', 'points', 'hint', 'question', 'user')


class File(DjangoObjectType):
    class Meta:
        model = models.File
        only_fields = ('id', 'name', 'questions')


class Competition(DjangoObjectType):
    class Meta:
        model = models.Competition
        only_fields = ('id', 'name', 'start', 'end', 'categories', 'competitors')

    @add_current_user
    def resolve_categories(self, usr, info):
        return [cat for cat in self.categories.all() if cat.is_viewable(usr)]


class Query(graphene.ObjectType):
    users = graphene.List(User)
    competitions = graphene.List(Competition)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_competitions(self, info):
        return models.Competition.objects.all()


schema = graphene.Schema(query=Query)
