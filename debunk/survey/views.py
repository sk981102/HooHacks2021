from django.shortcuts import render, get_object_or_404
from .forms import RequestForm2, RequestFormOther
from .models import SurveyOther,SurveyCovid
# Create your views here.

def survey1_view(request, *args, **kwargs):
    return render(request, "survey.html", {})

def covid_view(request, *args, **kwargs):
    if request.method == 'POST':
        print("hmm")
        form = RequestForm2(request.POST)
        if form.is_valid():
            print("work")
            vaccine_type =form.cleaned_data['vaccine_type']
            second_shot = form.cleaned_data['second_shot']
            side_effect =form.cleaned_data['side_effect']
            children = form.cleaned_data['children']
            others = form.cleaned_data["others"]
            requested = SurveyCovid.objects.create(vaccine_type=vaccine_type,second_shot=second_shot,side_effect=side_effect,children=children,others=others)
            requested.save()
            return render(request, "facts.html", {"form": form.cleaned_data, })
    else:
        form = RequestForm2(request.POST)
    return render(request, "covid.html", {"form": form, })

def other_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = RequestFormOther(request.POST)
        if form.is_valid():
            print("work")
            autism = form.cleaned_data['autism']
            cancer = form.cleaned_data['cancer']
            choice = form.cleaned_data['choice']
            gov = form.cleaned_data['gov']
            others = form.cleaned_data["others"]
            requested = SurveyOther.objects.create(autism=autism,cancer=cancer,choice=choice,gov=gov,others=others)
            requested.save()
            return render(request, "facts2.html", {"form": form.cleaned_data, })
    else:
        form = RequestFormOther(request.POST)
    return render(request, "other.html",{"form": form, })

def facts_view(request, *args, **kwargs):
    return render(request, "facts.html", {})