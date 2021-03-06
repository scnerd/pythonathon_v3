# Generated by Django 2.0.1 on 2018-01-17 21:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctf', '0010_auto_20180102_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hasseenhint',
            name='question',
        ),
        migrations.RemoveField(
            model_name='hasseenhint',
            name='user',
        ),
        migrations.RemoveField(
            model_name='file',
            name='question',
        ),
        migrations.AddField(
            model_name='competition',
            name='competitors',
            field=models.ManyToManyField(related_name='competitions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='files',
            field=models.ManyToManyField(related_name='questions', to='ctf.File'),
        ),
        migrations.AddField(
            model_name='question',
            name='has_seen_hint',
            field=models.ManyToManyField(related_name='hints_used', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='solvers',
            field=models.ManyToManyField(related_name='questions_attempted', through='ctf.Solution', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='HasSeenHint',
        ),
    ]
