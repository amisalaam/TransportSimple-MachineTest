from django.shortcuts import render,redirect
from .forms import RegistrationalForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainApp.models import Question
# Create your views here.

@login_required(login_url='/login')
def home(request):
    question = Question.objects.all().order_by('posted_date')

    context={
        'question':question
    }
    return render(request,"home.html",context)




def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                print(email,password)
                user = authenticate(request, email=email, password=password)

                print(user)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid login credentials.')
        else:
            form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'signin.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationalForm(request.POST)
            if form.is_valid():
                full_name=form.cleaned_data['full_name']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                user = Account.objects.create_user(full_name=full_name,email=email,  password=password)
    
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            form = RegistrationalForm()
        context={
            'form':form
        }
        return render (request,'register.html',context)
    


@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('login')


