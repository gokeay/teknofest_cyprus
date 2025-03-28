from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum, Count
from django.utils import timezone
import csv
from datetime import datetime, timedelta
from forms.models import (
    T3PersonelVeriler, 
    GonulluDurumVeriler, 
    GonulluSorunVeriler, 
    SorumluVeriler
)
from forms.views import role_required
from accounts.views import log_user_action

@login_required
@role_required(['izleyici', 'admin'])
def dashboard_home(request):
    """Dashboard ana sayfası"""
    log_user_action(request, 'Dashboard Ana Sayfası Görüntülendi', 'Dashboard Home')
    
    # Son 7 günlük verileri getir
    son_7_gun = timezone.now().date() - timedelta(days=7)
    
    t3_veriler_sayisi = T3PersonelVeriler.objects.filter(submitteddate__gte=son_7_gun).count()
    gonullu_durum_sayisi = GonulluDurumVeriler.objects.filter(submitteddate__gte=son_7_gun).count()
    gonullu_sorun_sayisi = GonulluSorunVeriler.objects.filter(submitteddate__gte=son_7_gun).count()
    sorumlu_veriler_sayisi = SorumluVeriler.objects.filter(submitteddate__gte=son_7_gun).count()
    
    # Toplam sipariş sayıları
    toplam_personel_siparis = SorumluVeriler.objects.filter(submitteddate__gte=son_7_gun).aggregate(Sum('personel_yemek_siparis'))['personel_yemek_siparis__sum'] or 0
    toplam_taseron_siparis = SorumluVeriler.objects.filter(submitteddate__gte=son_7_gun).aggregate(Sum('taseron_yemek_siparis'))['taseron_yemek_siparis__sum'] or 0
    toplam_t3_siparis = T3PersonelVeriler.objects.filter(submitteddate__gte=son_7_gun).aggregate(Sum('siparis_sayisi'))['siparis_sayisi__sum'] or 0
    
    context = {
        't3_veriler_sayisi': t3_veriler_sayisi,
        'gonullu_durum_sayisi': gonullu_durum_sayisi,
        'gonullu_sorun_sayisi': gonullu_sorun_sayisi,
        'sorumlu_veriler_sayisi': sorumlu_veriler_sayisi,
        'toplam_personel_siparis': toplam_personel_siparis,
        'toplam_taseron_siparis': toplam_taseron_siparis,
        'toplam_t3_siparis': toplam_t3_siparis,
    }
    
    return render(request, 'dashboard/home.html', context)

@login_required
@role_required(['izleyici', 'admin'])
def t3personel_dashboard(request):
    """T3 personel verileri dashboard"""
    log_user_action(request, 'T3 Personel Dashboard Görüntülendi', 'T3 Personel Dashboard')
    
    # Filtreleme parametreleri
    baslangic_tarihi = request.GET.get('baslangic_tarihi')
    bitis_tarihi = request.GET.get('bitis_tarihi')
    koordinatorluk = request.GET.get('koordinatorluk')
    birim = request.GET.get('birim')
    
    # Temel sorgu
    veriler = T3PersonelVeriler.objects.all().order_by('-submitteddate', '-submittedtime')
    
    # Filtreleri uygula
    if baslangic_tarihi:
        veriler = veriler.filter(submitteddate__gte=baslangic_tarihi)
    if bitis_tarihi:
        veriler = veriler.filter(submitteddate__lte=bitis_tarihi)
    if koordinatorluk:
        veriler = veriler.filter(koordinatorluk__icontains=koordinatorluk)
    if birim:
        veriler = veriler.filter(birim__icontains=birim)
    
    # CSV indirme
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="t3personel_veriler.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['TC', 'İsim', 'Soyisim', 'Koordinatörlük', 'Birim', 'Sipariş Sayısı', 'Tarih', 'Saat'])
        
        for veri in veriler:
            writer.writerow([
                veri.kisi.tc,
                veri.kisi.isim,
                veri.kisi.soyisim,
                veri.koordinatorluk,
                veri.birim,
                veri.siparis_sayisi,
                veri.submitteddate,
                veri.submittedtime
            ])
        
        return response
    
    # Koordinatörlük ve birim listelerini al
    koordinatorlukler = T3PersonelVeriler.objects.values_list('koordinatorluk', flat=True).distinct()
    birimler = T3PersonelVeriler.objects.values_list('birim', flat=True).distinct()
    
    context = {
        'veriler': veriler,
        'koordinatorlukler': koordinatorlukler,
        'birimler': birimler,
        'filtreler': {
            'baslangic_tarihi': baslangic_tarihi,
            'bitis_tarihi': bitis_tarihi,
            'koordinatorluk': koordinatorluk,
            'birim': birim,
        }
    }
    
    return render(request, 'dashboard/t3personel.html', context)

@login_required
@role_required(['izleyici', 'admin'])
def gonullu_durum_dashboard(request):
    """Gönüllü durum verileri dashboard"""
    log_user_action(request, 'Gönüllü Durum Dashboard Görüntülendi', 'Gönüllü Durum Dashboard')
    
    # Filtreleme parametreleri
    baslangic_tarihi = request.GET.get('baslangic_tarihi')
    bitis_tarihi = request.GET.get('bitis_tarihi')
    alan = request.GET.get('alan')
    
    # Temel sorgu
    veriler = GonulluDurumVeriler.objects.all().order_by('-submitteddate', '-submittedtime')
    
    # Filtreleri uygula
    if baslangic_tarihi:
        veriler = veriler.filter(submitteddate__gte=baslangic_tarihi)
    if bitis_tarihi:
        veriler = veriler.filter(submitteddate__lte=bitis_tarihi)
    if alan:
        veriler = veriler.filter(alan__icontains=alan)
    
    # CSV indirme
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="gonullu_durum_veriler.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['TC', 'İsim', 'Soyisim', 'Gün', 'Saat', 'Alan', 'Açıklama', 'Tarih', 'Saat'])
        
        for veri in veriler:
            writer.writerow([
                veri.kisi.tc,
                veri.kisi.isim,
                veri.kisi.soyisim,
                veri.gun,
                veri.saat,
                veri.alan,
                veri.aciklama,
                veri.submitteddate,
                veri.submittedtime
            ])
        
        return response
    
    # Alan listesini al
    alanlar = GonulluDurumVeriler.objects.values_list('alan', flat=True).distinct()
    
    context = {
        'veriler': veriler,
        'alanlar': alanlar,
        'filtreler': {
            'baslangic_tarihi': baslangic_tarihi,
            'bitis_tarihi': bitis_tarihi,
            'alan': alan,
        }
    }
    
    return render(request, 'dashboard/gonullu_durum.html', context)

@login_required
@role_required(['izleyici', 'admin'])
def gonullu_sorun_dashboard(request):
    """Gönüllü sorun verileri dashboard"""
    log_user_action(request, 'Gönüllü Sorun Dashboard Görüntülendi', 'Gönüllü Sorun Dashboard')
    
    # Filtreleme parametreleri
    baslangic_tarihi = request.GET.get('baslangic_tarihi')
    bitis_tarihi = request.GET.get('bitis_tarihi')
    alan = request.GET.get('alan')
    
    # Temel sorgu
    veriler = GonulluSorunVeriler.objects.all().order_by('-submitteddate', '-submittedtime')
    
    # Filtreleri uygula
    if baslangic_tarihi:
        veriler = veriler.filter(submitteddate__gte=baslangic_tarihi)
    if bitis_tarihi:
        veriler = veriler.filter(submitteddate__lte=bitis_tarihi)
    if alan:
        veriler = veriler.filter(alan__icontains=alan)
    
    # CSV indirme
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="gonullu_sorun_veriler.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['TC', 'İsim', 'Soyisim', 'Gün', 'Saat', 'Alan', 'Açıklama', 'Tarih', 'Saat'])
        
        for veri in veriler:
            writer.writerow([
                veri.kisi.tc,
                veri.kisi.isim,
                veri.kisi.soyisim,
                veri.gun,
                veri.saat,
                veri.alan,
                veri.aciklama,
                veri.submitteddate,
                veri.submittedtime
            ])
        
        return response
    
    # Alan listesini al
    alanlar = GonulluSorunVeriler.objects.values_list('alan', flat=True).distinct()
    
    context = {
        'veriler': veriler,
        'alanlar': alanlar,
        'filtreler': {
            'baslangic_tarihi': baslangic_tarihi,
            'bitis_tarihi': bitis_tarihi,
            'alan': alan,
        }
    }
    
    return render(request, 'dashboard/gonullu_sorun.html', context)

@login_required
@role_required(['izleyici', 'admin', 'sorumlu'])
def sorumlu_dashboard(request):
    """Sorumlu verileri dashboard"""
    log_user_action(request, 'Sorumlu Dashboard Görüntülendi', 'Sorumlu Dashboard')
    
    # Filtreleme parametreleri
    baslangic_tarihi = request.GET.get('baslangic_tarihi')
    bitis_tarihi = request.GET.get('bitis_tarihi')
    
    # Temel sorgu
    veriler = SorumluVeriler.objects.all().order_by('-submitteddate', '-submittedtime')
    
    # Filtreleri uygula
    if baslangic_tarihi:
        veriler = veriler.filter(submitteddate__gte=baslangic_tarihi)
    if bitis_tarihi:
        veriler = veriler.filter(submitteddate__lte=bitis_tarihi)
    
    # CSV indirme
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sorumlu_veriler.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['TC', 'İsim', 'Soyisim', 'Gün', 'Personel Yemek Siparişi', 'Taşeron Yemek Siparişi', 'Tarih', 'Saat'])
        
        for veri in veriler:
            writer.writerow([
                veri.kisi.tc,
                veri.kisi.isim,
                veri.kisi.soyisim,
                veri.gun,
                veri.personel_yemek_siparis,
                veri.taseron_yemek_siparis,
                veri.submitteddate,
                veri.submittedtime
            ])
        
        return response
    
    # Toplam sipariş sayıları
    toplam_personel_siparis = veriler.aggregate(Sum('personel_yemek_siparis'))['personel_yemek_siparis__sum'] or 0
    toplam_taseron_siparis = veriler.aggregate(Sum('taseron_yemek_siparis'))['taseron_yemek_siparis__sum'] or 0
    
    context = {
        'veriler': veriler,
        'toplam_personel_siparis': toplam_personel_siparis,
        'toplam_taseron_siparis': toplam_taseron_siparis,
    }
    
    return render(request, 'dashboard/sorumlu.html', context)
