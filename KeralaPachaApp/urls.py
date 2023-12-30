from django.urls import path 
from KeralaPachaApp import views

urlpatterns = [ path('', views.Home, name='index'), ]