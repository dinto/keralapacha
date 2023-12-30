from django.urls import path 
from KeralaPachaApp import views

urlpatterns = [ 
    path('', views.Home, name='index'), 
    path('home/',views.Home,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]