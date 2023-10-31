from django.shortcuts import render,redirect
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Answer




#FUNCTION FOR ASK A QUESTION
@login_required
def ask_question(request):
    try:
        if request.method == 'POST':
            form = QuestionForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Question submitted successfully.")
                return redirect('home')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = QuestionForm(request.user)

        return render(request, 'ask_question.html', {'form': form})
    except PermissionDenied:
        messages.error(request, "Permission denied. Please log in to ask a question.")
        
        return redirect('login') 


#FUNCTION FOR LIKE ANSWER
@login_required
def like_answer(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
        answer.like(request.user)
        messages.success(request, "Answer liked successfully.")
    except Answer.DoesNotExist:
        messages.error(request, "Answer not found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
    
    return redirect('home')


#FUNCTION FOR UNLIKE ANSWER
@login_required
def unlike_answer(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
        answer.unlike(request.user)
        messages.success(request, "Answer unliked successfully.")
    except Answer.DoesNotExist:
        messages.error(request, "Answer not found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")

    return redirect('home')

