from django.urls import path

from .views import HomeView, MyLoginView, RegistrationView, SuccessView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegistrationView.as_view(), name='register'),
    path('success', SuccessView.as_view(), name='success'),

]