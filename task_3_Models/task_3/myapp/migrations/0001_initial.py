# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answeredQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAnswer', models.TextField()),
                ('questionPassed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.CharField(max_length=100)),
                ('correctAnswer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('phaseNum', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='answeredquestions',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.question'),
        ),
        migrations.AddField(
            model_name='answeredquestions',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]