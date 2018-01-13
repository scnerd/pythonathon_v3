from django.core.management.base import BaseCommand
from oauth2_provider.models import Application
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Application.objects.count() == 0:
            print("Initializing JupyterHub OAuth parameters")
            id_path = os.environ.get('OAUTH_CLIENT_ID_PATH')
            secret_path = os.environ.get('OAUTH_CLIENT_SECRET_PATH')
            app_name = 'jupyterhub'
            skip_auth = True
            redirect = os.environ['OAUTH_CALLBACK_URL']
            client_type = Application.CLIENT_CONFIDENTIAL
            grant_type = Application.GRANT_AUTHORIZATION_CODE
            if id_path and secret_path and os.path.exists(id_path) and os.path.exists(secret_path):
                print("Couldn't find existing ID and SECRET, generating new ones")
                client_id = open(id_path).read().strip()
                client_secret = open(secret_path).read().strip()
                jup = Application(
                    name=app_name,
                    redirect_uris=redirect,
                    client_type=client_type,
                    authorization_grant_type=grant_type,
                    skip_authorization=skip_auth,
                    client_id=client_id,
                    client_secret=client_secret,
                )
                jup.save()
            elif id_path and secret_path:
                print("Couldn't find existing ID and SECRET, generating new ones")
                jup = Application(
                    name=app_name,
                    redirect_uris=redirect,
                    client_type=client_type,
                    authorization_grant_type=grant_type,
                    skip_authorization=skip_auth,
                )
                jup.save()
                open(id_path, 'w').write(jup.client_id)
                open(secret_path, 'w').write(jup.client_secret)
            else:
                print("Provide both OAUTH_CLIENT_ID_PATH and OAUTH_CLIENT_SECRET_PATH in order to auto-generate these values")
        else:
            print('JupyterHub application is only created if no existing application exists')
