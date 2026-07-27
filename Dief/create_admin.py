import os
import sys
import django


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dief.settings')

try:
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
        print("--> Superuser created successfully!")
    else:
        print("--> Password for existing user was updated successfully!")

except Exception as e:
    print(f"--> Error running create_admin script: {e}")
