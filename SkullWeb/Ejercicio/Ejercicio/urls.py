from django.contrib import admin
from django.urls import path
from Ejercicio.views import index, about, login_view, service, contact, employees, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('index.html',index, name='index'),
    path('about.html', about, name='about'),
    path('service.html', service, name='service'),
    path('contact.html', contact, name='contact'),
    path('employees.html', employees, name='employees'),
    path('register.html', register, name='register'),
    path('login/', login_view, name='login'),
]
