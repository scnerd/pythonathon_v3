from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class _NamedObj:
    def __repr__(self):
        return "<{} '{}'>".format(type(self).__name__, self.name)

    def __str__(self):
        return self.name


class Question(models.Model, _NamedObj):
    name = models.TextField()
    full_text = models.TextField()
    hint = models.TextField()
    hint_cost = models.IntegerField()
    answer = models.TextField()
    case_sensitive = models.BooleanField()
    points = models.IntegerField()

    requires = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questions_required_by')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='questions')


class Category(models.Model, _NamedObj):
    name = models.TextField()
    requires = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='categories_required_by')


class Solution(models.Model):
    submission = models.TextField()
    timestamp = models.DateTimeField()
    success = models.BooleanField()
    used_hint = models.BooleanField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='solutions')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='solutions')