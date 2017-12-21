from django.urls import path

from . import views

app_name = 'ctf'
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:question_id>', views.question_view, name='question'),
    path('category/<int:category_id>', views.category_view, name='category'),
    path('problems', views.problem_overview, name='problems'),
    path('submit_solution/<int:question_id>', views.submit_solution, name='solve'),
    path('profile', views.user_profile, name='my_profile'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
]
