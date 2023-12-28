from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('works/<str:work_id>/', views.work_view, name='work-view'),
    path('concepts/<str:concept>/', views.concept_view, name='concept-view'),
]