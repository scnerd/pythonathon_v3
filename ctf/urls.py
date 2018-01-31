from django.urls import path

from . import views

app_name = 'ctf'
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:question_id>', views.question_view, name='question'),
    path('questions/<int:question_id>/hint', views.hint_view, name='hint'),
    path('category/<int:category_id>', views.category_view, name='category'),
    path('dl/all', views.list_downloads, name='list_downloads'),
    path('dl/<int:file_id>', views.file_download, name='download'),
    path('dl/<path:file_id>', views.file_download, name='download_name'),
    path('problems', views.problem_overview, name='problems'),
    path('profiles', views.profile_overview, name='profiles'),
    path('profile', views.user_profile, name='my_profile'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('signup/', views.signup, name='signup'),
]
