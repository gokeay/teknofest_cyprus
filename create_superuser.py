import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yemek_otomasyonu.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# TC numarası ile admin kullanıcısı var mı kontrol et, yoksa oluştur
if not User.objects.filter(tc="11111111112").exists():
    User.objects.create_superuser(
        tc="11111111112",  # TC numarasını kullanıcı adı olarak kullanıyoruz
        email="admin@example.com",  # E-posta isteğe bağlı, genellikle boş bırakılabilir
        password="alskZM10.",
        first_name="Admin",
        last_name="User",
    )
    print("Superuser created with TC: 11111111112, password: alskZM10.")
else:
    print("Superuser already exists.")
