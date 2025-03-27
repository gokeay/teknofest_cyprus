from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('gonullu/', views.gonullu_form, name='gonullu_form'),
    path('gonullu/durum/', views.gonullu_durum_form, name='gonullu_durum_form'),
    path('gonullu/sorun/', views.gonullu_sorun_form, name='gonullu_sorun_form'),
    path('t3personel/', views.t3personel_form, name='t3personel_form'),
    path('sorumlu/', views.sorumlu_form, name='sorumlu_form'),
] 