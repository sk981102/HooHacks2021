# Generated by Django 3.1.7 on 2021-03-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_surveycovid_surveyother'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveycovid',
            name='others',
            field=models.TextField(db_column='other_concerns', default=''),
        ),
    ]
