# Generated by Django 3.1.7 on 2021-03-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210328_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveycovid',
            name='others',
            field=models.TextField(db_column='others', default=''),
        ),
        migrations.AlterField(
            model_name='surveyother',
            name='others',
            field=models.TextField(db_column='others', default=''),
        ),
    ]
