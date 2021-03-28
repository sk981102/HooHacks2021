from django import forms
from .models import SurveyCovid, SurveyOther


class RequestFormOther(forms.ModelForm):
    autism = forms.BooleanField(required=False)
    cancer = forms.BooleanField(required=False)
    choice = forms.BooleanField(required=False)
    gov = forms.BooleanField(required=False)
    others = forms.CharField(required=False)

    class Meta:
        model = SurveyOther
        fields = ('autism', 'cancer', 'choice', 'gov', 'others')



class RequestForm2(forms.ModelForm):
    vaccine_type = forms.BooleanField(required=False)
    second_shot = forms.BooleanField(required=False)
    side_effect = forms.BooleanField(required=False)
    children = forms.BooleanField(required=False)
    others = forms.CharField(required=False)

    class Meta:
        model = SurveyCovid
        fields = ('vaccine_type','second_shot','side_effect','children','others')



