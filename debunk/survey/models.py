from django.db import models



class SurveyCovid(models.Model):
    concern_id = models.AutoField(primary_key=True)
    vaccine_type = models.BooleanField(db_column='vaccine_type')
    second_shot = models.BooleanField(db_column='second_shot')
    side_effect = models.BooleanField(db_column='side_effect')
    children = models.BooleanField(db_column='children')
    others=models.TextField(db_column="others",default="")

    class Meta:
        db_table = 'survey_covid'


class SurveyOther(models.Model):
    concern_id = models.AutoField(primary_key=True)
    autism = models.BooleanField(db_column='autism')
    cancer = models.BooleanField(db_column='cancer')
    choice = models.BooleanField(db_column='choice')
    gov = models.BooleanField(db_column='gov')
    others = models.TextField(db_column="others", default="")

    class Meta:
        db_table = 'survey_other'
