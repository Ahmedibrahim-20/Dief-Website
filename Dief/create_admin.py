import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dief.settings')
django.setup()

from django.contrib.auth.models import User

NEW_USERNAME = "admin2026"
NEW_PASSWORD = "MyStrongPassword2026!" 
NEW_EMAIL = "admin@example.com"

user, created = User.objects.get_or_create(username=NEW_USERNAME, defaults={'email': NEW_EMAIL})
user.set_password(NEW_PASSWORD)
user.is_superuser = True
user.is_staff = True
user.save()

if created:
    print("New Superuser created successfully!")
else:
    print("Password for existing user was updated successfully!")
