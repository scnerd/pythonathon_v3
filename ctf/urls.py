from django.urls import path

from . import views

app_name = 'ctf'
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:question_id>', views.question_view, name='question'),
    path('submit_solution/<int:question_id>', views.submit_solution, name='solve'),
]