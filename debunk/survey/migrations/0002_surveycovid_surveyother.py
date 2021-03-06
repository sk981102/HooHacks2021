# Generated by Django 3.1.7 on 2021-03-28 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyOther',
            fields=[
                ('concern_id', models.AutoField(primary_key=True, serialize=False)),
                ('autism', models.BooleanField(db_column='autism')),
                ('cancer', models.BooleanField(db_column='cancer')),
                ('choice', models.BooleanField(db_column='choice')),
                ('gov', models.BooleanField(db_column='gov')),
                ('type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.survey1')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyCovid',
            fields=[
                ('concern_id', models.AutoField(primary_key=True, serialize=False)),
                ('vaccine_type', models.BooleanField(db_column='vaccine_type')),
                ('second_shot', models.BooleanField(db_column='second_shot')),
                ('side_effect', models.BooleanField(db_column='side_effect')),
                ('children', models.BooleanField(db_column='children')),
                ('type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.survey1')),
            ],
        ),
    ]
