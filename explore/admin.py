from django.contrib import admin

from .models import Work, LlamaConcept, OpenAlexConcept, Element

admin.site.register(Work)
admin.site.register(LlamaConcept)
admin.site.register(OpenAlexConcept)
admin.site.register(Element)