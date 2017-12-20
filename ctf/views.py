from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):
    latest_solutions = Solution.objects.order_by('-timestamp')[:5]
    context = {
        'latest_solution_list': latest_solutions,
    }
    return render(request, 'ctf/index.html', context)


@login_required()
def question_view(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'ctf/question.html', {'question': q})


@login_required()
def submit_solution(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    user = request.user
    provided_answer = request.POST['answer']
    print(provided_answer)
    pass