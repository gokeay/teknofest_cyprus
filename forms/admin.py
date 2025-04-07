from django.contrib import admin
from .models import (
    T3PersonelAtama, 
    T3PersonelVeriler, 
    GonulluDurumVeriler, 
    GonulluSorunVeriler, 
    SorumluVeriler,
    SistemAyarlari
)

@admin.register(T3PersonelAtama)
class T3PersonelAtamaAdmin(admin.ModelAdmin):
    list_display = ('kisi', 'koordinatorluk', 'birim')
    search_fields = ('kisi__isim', 'kisi__soyisim', 'koordinatorluk', 'birim')
    list_filter = ('koordinatorluk',)

@admin.register(T3PersonelVeriler)
class T3PersonelVerilerAdmin(admin.ModelAdmin):
    list_display = ('kisi', 'koordinatorluk', 'birim', 'ogle_yemek_sayisi', 'aksam_yemek_sayisi', 'submitteddate', 'submittedtime')
    search_fields = ('kisi__username', 'kisi__first_name', 'kisi__last_name', 'koordinatorluk', 'birim')
    list_filter = ('submitteddate', 'koordinatorluk', 'birim')
    date_hierarchy = 'submitteddate'

@admin.register(GonulluDurumVeriler)
class GonulluDurumVerilerAdmin(admin.ModelAdmin):
    list_display = ('kisi', 'gun', 'saat', 'alan', 'submitteddate', 'submittedtime')
    search_fields = ('kisi__isim', 'kisi__soyisim', 'alan', 'aciklama')
    list_filter = ('gun', 'alan')
    date_hierarchy = 'gun'

@admin.register(GonulluSorunVeriler)
class GonulluSorunVerilerAdmin(admin.ModelAdmin):
    list_display = ('kisi', 'gun', 'saat', 'alan', 'submitteddate', 'submittedtime')
    search_fields = ('kisi__isim', 'kisi__soyisim', 'alan', 'aciklama')
    list_filter = ('gun', 'alan')
    date_hierarchy = 'gun'

@admin.register(SorumluVeriler)
class SorumluVerilerAdmin(admin.ModelAdmin):
    list_display = ('kisi', 'gun', 'personel_yemek_siparis', 'taseron_yemek_siparis', 'submitteddate', 'submittedtime')
    search_fields = ('kisi__isim', 'kisi__soyisim')
    list_filter = ('gun',)
    date_hierarchy = 'gun'

@admin.register(SistemAyarlari)
class SistemAyarlariAdmin(admin.ModelAdmin):
    list_display = ('anahtar', 'deger', 'aciklama')
    search_fields = ('anahtar', 'deger', 'aciklama')
