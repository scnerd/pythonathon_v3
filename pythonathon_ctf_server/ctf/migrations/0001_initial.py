# Generated by Django 2.0 on 2017-12-20 16:15

import ctf.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('full_text', models.TextField()),
                ('hint', models.TextField()),
                ('hint_cost', models.IntegerField()),
                ('answer', models.TextField()),
                ('case_sensitive', models.BooleanField()),
                ('points', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ctf.Category')),
                ('requires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_required_by', to='ctf.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('success', models.BooleanField()),
                ('used_hint', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='ctf.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='requires',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_required_by', to='ctf.Question'),
        ),
    ]