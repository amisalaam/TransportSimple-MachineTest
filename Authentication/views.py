from django.shortcuts import render,redirect
from .forms import RegistrationalForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError 
from mainApp.models import Question,Answer
from mainApp.forms import AnswerForm
# Create your views here.


# HOME PAGE FUNCTIONS
@login_required(login_url='/login')
def home(request):
    questions = Question.objects.exclude(user=request.user).order_by('-posted_date')
    my_questions = Question.objects.filter(user=request.user).order_by('posted_date')
    my_answers = Answer.objects.filter(user=request.user).order_by('posted_date')

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            try:
                new_answer = form.save(commit=False)
                new_answer.user = request.user
                new_answer.question = Question.objects.get(pk=request.POST['question_id'])
                new_answer.save()
                messages.success(request, "Answer submitted successfully.")
                return redirect('home')
            except Question.DoesNotExist:
                messages.error(request, "Question not found.")
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            #FORM VALIDATION ERRORS
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = AnswerForm()

    context = {
        'questions': questions,
        'form': form,
        'my_questions':my_questions,
        'my_answers':my_answers
    }
    return render(request, "home.html", context)



#FUNCTION FOR LOGIN
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid login credentials.')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'signin.html', context)


#FUNCTION FOR REGISTERING A USER
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationalForm(request.POST)
            try:
                if form.is_valid():
                    full_name = form.cleaned_data['full_name']
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']
                    user = Account.objects.create_user(full_name=full_name, email=email, password=password)
                    user.save()
                    login(request, user)  # Log the user in after registration.
                    messages.success(request, 'Registration successful. You are now logged in.')
                    return redirect('home')
            except IntegrityError:
                messages.error(request, 'This email is already registered. Please use a different email.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            form = RegistrationalForm()
        
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
    

#FUNCTION FOR LOGOUT
@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('login')


