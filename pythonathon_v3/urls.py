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

from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from oauth2_provider.decorators import protected_resource
from django.http import HttpResponse
import json


@protected_resource()
def get_user(request):
    user = request.user
    return HttpResponse(
        json.dumps({
            'username': user.username,
            'email': user.email}),
        content_type='application/json')


urlpatterns = [
    path('', include('ctf.urls')),
    path('admin/', admin.site.urls),
    path('o/whoami/', get_user),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('account/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ctf:index'), name='logout'),
]