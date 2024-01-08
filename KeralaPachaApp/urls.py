from django.urls import path 
from KeralaPachaApp import views
from django.contrib import admin

urlpatterns = [ 
    path('', views.Home, name='index'), 
    path('home/',views.Home,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('master/',views.master,name='master'),
    path('orders/',views.orders,name='orders'),
    path('hr/',views.hr,name='hr'),
    path('reports/',views.reports,name='reports'),
]



admin.site.site_header = 'KeralaPacha Administration dashboard'                   
admin.site.index_title = 'KeralaPacha'                 
admin.site.site_title = 'SuperNova Administration'