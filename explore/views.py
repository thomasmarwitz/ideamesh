from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Work, LlamaConcept, OpenAlexConcept 


def index(request):
    return HttpResponse("Hello, world. You're at the keyword explorer index.")

def concept_view(request, concept):
    works = Work.objects.filter(llama_concepts__name=concept)  # Adjust the filter as needed
    return render(request, 'concept_view.html', {'works': works, 'concept': concept})

def work_view(request, work_id):
    work = Work.objects.get(id=work_id)
    return render(request, 'work_view.html', {'work': work})