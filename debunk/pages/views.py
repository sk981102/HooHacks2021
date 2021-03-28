from django.shortcuts import render
from survey.models import SurveyCovid,SurveyOther

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def analysis_view(request, *args, **kwargs):
    labels = ["Covid", "Others"]

    queryset = SurveyCovid.objects.all()
    queryset2 = SurveyOther.objects.all()
    data=[len(queryset),len(queryset2)]

    v1,v2,v3,v4=0,0,0,0
    for q in queryset:
        if q.vaccine_type:
            v1+=1
        if q.second_shot:
            v2+=1
        if q.side_effect:
            v3+=1
        if q.children:
            v4+=1
    covid_labels=["Different Vaccines","Second Dose","Side Effect", "Children"]
    covid_data = [v1,v2,v3,v4]

    v1,v2,v3,v4=0,0,0,0
    for q in queryset2:
        if q.autism:
            v1+=1
        if q.cancer:
            v2+=1
        if q.choice:
            v3+=1
        if q.gov:
            v4+=1
    other_labels=["Cause Autism","Cause Cancer","Just a Choice", "Don't Trust Government"]
    other_data = [v1,v2,v3,v4]
    print(covid_data)

    return render(request, "analysis.html", {
        'labels': labels,
        'data': data,
        'covid_labels': covid_labels,
        'covid_data': covid_data,
        'other_labels': other_labels,
        'other_data': other_data,
    })
