from accounts.models import User
from forms.models import T3PersonelAtama

veriler = [
    {
        "tc": "12121212121",
        "isim": "Emirhan",
        "soyisim": "Ali zafer",
        "role": "t3 personel",
        "koord": "TEKNOFEST  Operasyon Koordinatörlüğü",
        "password": "TFCyprus1.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "10781611746",
        "isim": "Fatma",
        "soyisim": "Nur tip",
        "role": "t3 personel",
        "koord": "TEKNOFEST   Fuar Koordinatörlüğü",
        "password": "TEKNOFEST2025",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "14268042726",
        "isim": "Zahide",
        "soyisim": "Sara yılmaz",
        "role": "t3 personel",
        "koord": "Kurumsal İletişim  Koordinatörlüğü",
        "password": "TFCyprus1.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "13120019760",
        "isim": "Ebrar",
        "soyisim": "Özata",
        "role": "t3 personel",
        "koord": "Mimari Tasarım  Koordinatörlüğü",
        "password": "Ebrar123.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "13532141066",
        "isim": "Şevval",
        "soyisim": "Çelik",
        "role": "t3 personel",
        "koord": "TEKNOFEST  Yarışmalar Koordinatörlüğü",
        "password": "TY123456",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "68443094468",
        "isim": "Muhammet",
        "soyisim": "Ali demir",
        "role": "t3 personel",
        "koord": "Bursiyer Koordinatörülüğü",
        "password": "alidmr684",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "69016104232",
        "isim": "Bahar",
        "soyisim": "Kılıç",
        "role": "t3 personel",
        "koord": "İdari İşler Koordinatörlüğü",
        "password": "bK104232",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "60898371170",
        "isim": "Tuğçe",
        "soyisim": "Alemdar",
        "role": "t3 personel",
        "koord": "Satış ve Pazarlama  Koordinatörlüğü",
        "password": "TFCyprus1.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "17384601662",
        "isim": "Esma",
        "soyisim": "Aslan",
        "role": "t3 personel",
        "koord": "Kurumsal Yapılanma Koordinatörlüğü",
        "password": "TFCyprus1.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "12955082888",
        "isim": "Ayşenur",
        "soyisim": "Yavuz",
        "role": "t3 personel",
        "koord": "Deneyap Koordinatörlüğü",
        "password": "F129550A",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "41683520324",
        "isim": "Burak",
        "soyisim": "Altıntaş",
        "role": "t3 personel",
        "koord": "Girişim Koordinatörlüğü",
        "password": "B123456789",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "20404768528",
        "isim": "Emre",
        "soyisim": "Verim",
        "role": "t3 personel",
        "koord": "Ulaşım Koordinatörlüğü",
        "password": "Everim554546",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "23318519934",
        "isim": "Gökhan",
        "soyisim": "Çaylak",
        "role": "t3 personel",
        "koord": "Eğitim Ar-Ge",
        "password": "G233185",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "20291303482",
        "isim": "Havva",
        "soyisim": "Nur tekin",
        "role": "t3 personel",
        "koord": "Bilişim Koordinatörlüğü",
        "password": "havvanur.tekin",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "22766503472",
        "isim": "Gamze",
        "soyisim": "Tuzene",
        "role": "t3 personel",
        "koord": "Deneyap Kart Koordinatörlüğü",
        "password": "Deneyapkart1453.",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    },
    {
        "tc": "43744403324",
        "isim": "Beyza Nur",
        "soyisim": "Akkoyunlu",
        "role": "t3 personel",
        "koord": "Satış Pazarlama Koordinatörlüğü",
        "password": "Be202333",
        "birim": ["T3 Personel", "İl ve Deneyap Sorumlusu"]
    }
]

for v in veriler:
    user, created = User.objects.get_or_create(
        tc=v["tc"],
        defaults={
            "isim": v["isim"],
            "soyisim": v["soyisim"],
            "role": v["role"]
        }
    )
    if created:
        user.set_password(v["password"])
        user.save()

    for birim in v["birim"]:
        T3PersonelAtama.objects.create(
            kisi=user,
            koordinatorluk=v["koord"],
            birim=birim
        )
