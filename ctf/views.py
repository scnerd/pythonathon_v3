from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):
    latest_solutions = Solution.objects.order_by('-timestamp')[:5]
    context = {
        'latest_solution_list': latest_solutions,
    }
    return render(request, 'ctf/index.html', context)
    # return redirect('ctf:problems')


@login_required()
def question_view(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    user = request.user
    solution = q.solved_by(user)
    context = {
        'question': q,
        'solution': solution,
    }
    return render(request, 'ctf/question.html', context)


@login_required()
def submit_solution(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    user = request.user
    provided_answer = request.POST['answer']
    sol = Solution(question=q, user=user, submission=provided_answer, success=q.check_answer(provided_answer))
    sol.save()

    return redirect('ctf:question', question_id=question_id)


@login_required()
def problem_overview(request):
    cats = [(category,
             len(category.questions.all()),
             len([q for q in category.questions.all() if q.solved_by(request.user)])
             )
            for category in Category.objects.all()]
    context = {'categories': cats}
    return render(request, 'ctf/problems.html', context)


@login_required()
def category_view(request, category_id):
    cat = get_object_or_404(Category, id=category_id)
    print(cat.questions.all())
    question_solution_pairs = [(q, q.solved_by(request.user)) for q in cat.questions.all()]
    print(question_solution_pairs)
    context = {
        'category': cat,
        'question_solution_pairs': question_solution_pairs,
    }

    return render(request, 'ctf/category.html', context)
