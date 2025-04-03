from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('t3personel/', views.t3personel_dashboard, name='t3personel'),
    path('gonullu/durum/', views.gonullu_durum_dashboard, name='gonullu_durum'),
    path('gonullu/sorun/', views.gonullu_sorun_dashboard, name='gonullu_sorun'),
    path('sorumlu/', views.sorumlu_dashboard, name='sorumlu'),
    path('sistem-ayarlari-guncelle/', views.sistem_ayarlari_guncelle, name='sistem_ayarlari_guncelle'),
] 