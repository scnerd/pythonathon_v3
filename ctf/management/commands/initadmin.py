from django.core.management.base import BaseCommand
from ctf.models import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            password = 'admin'
            email = ''
            print('Creating account for %s' % (username,))
            admin = User.objects.create_superuser(username=username, email=email, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no users exist')
