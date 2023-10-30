from django.shortcuts import render,redirect
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = QuestionForm(request.user)

    return render(request, 'ask_question.html', {'form': form})