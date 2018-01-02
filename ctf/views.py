# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import *
from .forms import *


def viewable_questions(user):
    return [q for q in Question.objects.all() if q.is_viewable(user)]


def index(request):
    latest_solutions = Solution.objects.filter(success=True).order_by('-timestamp')[:5]
    context = {
        'latest_solution_list': latest_solutions,
    }
    return render(request, 'ctf/index.html', context)
    # return redirect('ctf:problems')


@login_required()
def question_view(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    user = request.user
    if not q.is_viewable(user):
        return HttpResponseForbidden()

    sol = None
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            print("=" * 20 + answer)
            correct = q.check_answer(answer)
            sol = Solution(question=q, user=user, submission=answer, success=correct)
            sol.save()

            if correct:
                messages.add_message(request, messages.SUCCESS, 'That was correct, good job!')
            else:
                messages.add_message(request, messages.WARNING, 'Incorrect answer')
                sol = None
    else:
        sol = q.solved_by(user)
        form = SubmissionForm()

    context = {
        'question': q,
        'solution': sol,
        'form': form
    }
    return render(request, 'ctf/question.html', context)


@login_required()
def problem_overview(request):
    questions = viewable_questions(request.user)
    categories = {q.category for q in questions}
    cats = [(category,
             len(category.questions.all()),
             len([q for q in category.questions.all() if q.solved_by(request.user)])
             )
            for category in sorted(categories, key=lambda c: c.order)]
    context = {'categories': cats}
    return render(request, 'ctf/problems.html', context)


@login_required()
def category_view(request, category_id):
    cat = get_object_or_404(Category, id=category_id)
    questions = sorted([q for q in cat.questions.all() if q.is_viewable(request.user)], key=lambda q: q.order)
    question_solution_pairs = [(q, q.solved_by(request.user)) for q in questions]
    context = {
        'category': cat,
        'question_solution_pairs': question_solution_pairs,
    }

    return render(request, 'ctf/category.html', context)


@login_required()
def profile_overview(request):
    context = {}
    users = get_user_model().objects.all()
    users = list(sorted(users, key=lambda u: sum(sol.net_score for sol in u.solutions.all()), reverse=True))
    context['users'] = [(u,
                         len({sol.question for sol in u.solutions.all()}),
                         sum(sol.net_score for sol in u.solutions.all()))
                        for u in users]
    return render(request, 'ctf/profiles.html', context)


@login_required()
def user_profile(request, user_id=None):
    if user_id is None:
        user_id = request.user.id
    user = get_object_or_404(get_user_model(), id=user_id)
    solutions = user.solutions.order_by('-timestamp')
    context = {
        'user': user,
        'is_self': user == request.user,
        'solutions': solutions,
    }
    return render(request, 'ctf/profile.html', context)


def signup(request):
    if not request.user.is_anonymous:
        redirect('ctf:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ctf:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)