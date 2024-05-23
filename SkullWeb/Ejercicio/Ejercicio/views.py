from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Empleado

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def employees(request):
    return render(request, 'employees.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    employees_list = employees.objects.all()
    datos = {
        'employees': employees_list
    }
    return render(request, 'Ejercicio/home.html', datos)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página principal con el nombre de usuario como parámetro en la URL
            return redirect(f'/inicio/?usuario={username}')
            # O redirigir a la página principal y almacenar el nombre de usuario en cookies/sesiones
            # request.session['username'] = username
            # return redirect('/inicio/')
        else:
            # Manejar el caso en que la autenticación falla
            pass
    return render(request, 'login.html')
