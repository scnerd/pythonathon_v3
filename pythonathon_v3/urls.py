"""pythonathon_v3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import json
import logging
import os

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import include, path
from graphene_django.views import GraphQLView
from oauth2_provider.decorators import protected_resource

log = logging.getLogger()


@protected_resource()
def get_user(request):
    user = request.user
    log.warning("WHOAMI returned user {}".format(user.username))
    return HttpResponse(
        json.dumps({
            'username': user.username,
            'email': user.email}),
        content_type='application/json')


logout_ctxt = {
    'jupyterhub_logout_url': os.environ.get('JUPYTERHUB_LOGOUT_URL', '/notebook/hub/logout'),
}

urlpatterns = [
    path('', include('ctf.urls')),
    path('admin/', admin.site.urls),
    path('o/whoami/', get_user),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(extra_context=logout_ctxt), name='logout'),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]