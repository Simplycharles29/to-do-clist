# Generated by Django 4.1.7 on 2023-03-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
