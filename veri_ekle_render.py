from accounts.models import User
from forms.models import T3PersonelAtama

veriler = [
    {"tc": "12121212121", "isim": "Emirhan", "soyisim": "Ali zafer", "role": "t3 personel", "koord": "TEKNOFEST  Operasyon Koordinatörlüğü", "birim": "[]"},
    {"tc": "10781611746", "isim": "Fatma", "soyisim": "Nur tip", "role": "t3 personel", "koord": "TEKNOFEST   Fuar Koordinatörlüğü", "birim": "[]"},
    {"tc": "14268042726", "isim": "Zahide", "soyisim": "Sara yılmaz", "role": "t3 personel", "koord": "Kurumsal İletişim  Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı']"},
    {"tc": "13120019760", "isim": "Ebrar", "soyisim": "Özata", "role": "t3 personel", "koord": "Mimari Tasarım  Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik']"},
    {"tc": "13532141066", "isim": "Şevval", "soyisim": "Çelik", "role": "t3 personel", "koord": "TEKNOFEST  Yarışmalar Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt']"},
    {"tc": "68443094468", "isim": "Muhammet", "soyisim": "Ali demir", "role": "t3 personel", "koord": "Bursiyer Koordinatörülüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff']"},
    {"tc": "69016104232", "isim": "Bahar", "soyisim": "Kılıç", "role": "t3 personel", "koord": "İdari İşler Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik']"},
    {"tc": "60898371170", "isim": "Tuğçe", "soyisim": "Alemdar", "role": "t3 personel", "koord": "Satış ve Pazarlama  Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör']"},
    {"tc": "17384601662", "isim": "Esma", "soyisim": "Aslan", "role": "t3 personel", "koord": "Kurumsal Yapılanma Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları']"},
    {"tc": "12955082888", "isim": "Ayşenur", "soyisim": "Yavuz", "role": "t3 personel", "koord": "Deneyap Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları', 'Güvenlik']"},
    {"tc": "41683520324", "isim": "Burak", "soyisim": "Altıntaş", "role": "t3 personel", "koord": "Girişim Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları', 'Güvenlik', 'Part Time Personel']"},
    {"tc": "20404768528", "isim": "Emre", "soyisim": "Verim", "role": "t3 personel", "koord": "Ulaşım Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları', 'Güvenlik', 'Part Time Personel', 'TSK']"},
    {"tc": "23318519934", "isim": "Gökhan", "soyisim": "Çaylak", "role": "t3 personel", "koord": "Eğitim Ar-Ge", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları', 'Güvenlik', 'Part Time Personel', 'TSK', 'Sahne Teknik']"},
    {"tc": "20291303482", "isim": "Havva", "soyisim": "Nur tekin", "role": "t3 personel", "koord": "Bilişim Koordinatörlüğü", "birim": "['Çadır,Podyum,Kumaş,Halı', 'Planetaryum Teknik', 'Kapı Kayıt', 'Scaff', 'Elektrik', 'Aksa Jeneratör', 'Güvenlik Ekipmanları', 'Güvenlik', 'Part Time Personel', 'TSK', 'Sahne Teknik', 'Pilot event']"},
]

for v in veriler:
    password = f"{v['isim'][0].lower()}{v['isim'][1].upper()}{v['tc'][-6:]}"
    user, created = User.objects.get_or_create(
        tc=v["tc"],
        defaults={
            "isim": v["isim"],
            "soyisim": v["soyisim"],
            "role": v["role"]
        }
    )
    if created:
        user.set_password(password)
        user.save()

    T3PersonelAtama.objects.create(
        kisi=user,
        koordinatorluk=v["koord"],
        birim=v["birim"]
    )
