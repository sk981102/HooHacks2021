# Generated by Django 3.1.7 on 2021-03-28 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_surveycovid_others'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveycovid',
            name='type_id',
        ),
        migrations.RemoveField(
            model_name='surveyother',
            name='type_id',
        ),
        migrations.AddField(
            model_name='surveyother',
            name='others',
            field=models.TextField(db_column='other_concerns', default=''),
        ),
        migrations.AlterModelTable(
            name='surveycovid',
            table='survey_covid',
        ),
        migrations.AlterModelTable(
            name='surveyother',
            table='survey_other',
        ),
        migrations.DeleteModel(
            name='Survey1',
        ),
    ]
