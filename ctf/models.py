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
    hint = models.TextField(blank=True, null=True)
    hint_cost = models.IntegerField(default=0)
    answer = models.TextField(blank=True)
    case_sensitive = models.BooleanField(default=False)
    points = models.IntegerField(default=1)

    requires = models.ForeignKey('Question', on_delete=models.SET_NULL, related_name='questions_required_by', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='questions', null=True)


class Category(models.Model, _NamedObj):
    name = models.TextField()
    requires = models.ForeignKey('Question', on_delete=models.SET_NULL, related_name='categories_required_by', blank=True, null=True)


class Solution(models.Model):
    submission = models.TextField()
    timestamp = models.DateTimeField()
    success = models.BooleanField()
    used_hint = models.BooleanField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='solutions')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='solutions')

    @property
    def net_score(self):
        if not self.success:
            return 0
        return self.question.points - (self.question.hint_cost if self.used_hint else 0)
