app_name = 'acount'

from django.contrib import admin
from django.urls import path
import acount.views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('accounts/login/',acount.views.login_request,name='Login'),
    path('accounts/signup/',acount.views.register,name='Registro'),
    path('accounts/logout/', LogoutView.as_view(template_name='acount/logout.html'), name='Logout'),
    path('accounts/profile/edit', acount.views.editarPerfil, name="EditarPerfil"),
    path('accounts/profile/avatar',acount.views.editarAvatar,name="EditarAvatar"),
    path('accounts/profile', acount.views.verPerfil, name="VerPerfil"),

]