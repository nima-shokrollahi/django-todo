from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request,"login successfully")
            return redirect('/')
        else:
            messages.warning(request,"username or password is wrong")
    form = AuthenticationForm
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = UserCreationForm
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.warning(request, "logout is complete")
        return redirect('/')
