from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm, RegistrForm
from personal_area.views import index
from django.contrib.auth.decorators import login_required
from sotuvapp.models import UserDetail
# Create your views here.


#ro'yxatdan o'tish
def sign_up(request):
    if request.method == 'POST':
        registr_form = RegistrForm(request.POST)

        if registr_form.is_valid():
            first_name = registr_form.cleaned_data['first_name']
            last_name  = registr_form.cleaned_data['last_name']
            email      = registr_form.cleaned_data['email'] 
            username   = registr_form.cleaned_data['username']
            password1  = registr_form.cleaned_data['password1']
            password2  = registr_form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Foydalanuvchi nomi ro'yxatdan o'tgan! ")
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Elektron pochta avvaldan mavjud!")
                else:
                    user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)         
                    user.save()
                    UserDetail.objects.create(user=user).save()
                    
            else:
                messages.info(request, "Parollar bir xil kiritilmadi!")
                return redirect('sign_up')
            
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)
            return redirect('/')
    else:
        registr_form = RegistrForm()
        return render(request, 'accounts/sign_up.html', {'form':registr_form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            username   = login_form.cleaned_data['username']
            password   = login_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request,"Login yoki Parol xato!")
                return redirect('sign_in')
    else:
        login_form = LoginForm()
        return render(request, 'accounts/sign_in.html', {'form':login_form})

    