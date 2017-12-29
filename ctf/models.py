from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Question(models.Model):
    name = models.TextField()
    full_text = models.TextField()
    hint = models.TextField(blank=True, null=True)
    hint_cost = models.IntegerField(default=0)
    answer = models.TextField(blank=True)
    case_sensitive = models.BooleanField(default=False)
    points = models.IntegerField(default=1)

    requires = models.ForeignKey('Question', on_delete=models.SET_NULL, related_name='questions_required_by', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='questions', null=True)

    def check_answer(self, answer):
        target = self.answer
        if not self.case_sensitive:
            target = self.answer.lower()
            answer = answer.lower()
        return target.strip() == answer.strip()

    def solved_by(self, user):
        res = self.solutions.filter(user=user, success=True)[:1]
        return res[0] if res else None

    def __str__(self):
        return "Question {}: '{}'".format(self.id, self.name)


class File(models.Model):
    name = models.TextField()
    content = models.FileField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return "File {}: '{}'".format(self.id, self.name)


class Category(models.Model):
    name = models.TextField()

    requires = models.ForeignKey('Question', on_delete=models.SET_NULL, related_name='categories_required_by', blank=True, null=True)
    competition = models.ForeignKey('Competition', on_delete=models.SET_NULL, related_name='categories', blank=True, null=True)

    def __str__(self):
        return "Category {}: '{}'".format(self.id, self.name)


class HasSeenHint(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='used_hints')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='hinted_users')


class Solution(models.Model):
    submission = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    success = models.BooleanField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='solutions')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='solutions')

    @property
    def net_score(self):
        if not self.success:
            return 0
        hints = self.user.used_hints.filter(question=self.question)
        return self.question.points - (self.question.hint_cost if len(hints) else 0)


class Competition(models.Model):
    name = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
