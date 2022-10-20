from email.mime import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def register_user(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'cuenta a sido creado para "' + user + '"')
            return redirect('member:login')

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'nombre de usuario o contraseña incorrecta')

    return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    return redirect('member:login')



