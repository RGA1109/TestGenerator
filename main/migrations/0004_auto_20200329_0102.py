# Generated by Django 3.0.3 on 2020-03-29 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200322_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='tests_id',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='question_id',
        ),
        migrations.CreateModel(
            name='TestToQuestion',
            fields=[
                ('TtoQ_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Questions')),
                ('tests_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Tests')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsToTags',
            fields=[
                ('QtoT_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Questions')),
                ('tag_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Tags')),
            ],
        ),
    ]
