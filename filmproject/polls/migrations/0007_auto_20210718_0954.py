# Generated by Django 3.2.5 on 2021-07-18 13:54

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_alter_question_date_published'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participation',
            new_name='Voter',
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 9, 54, 19, 811327)),
        ),
    ]