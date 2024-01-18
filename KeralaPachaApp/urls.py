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
    path('hr/LabourDetails/',views.LabourDetails,name='LabourDetails'),
    path('hr/SalaryType/',views.SalaryType,name='SalaryType'),
    path('hr/LabourSalary/',views.LabourSalary,name='LabourSalary'),
    path('hr/VehicleCost/',views.VehicleCost,name='VehicleCost'),
    path('hr/VehicleDetail/',views.VehicleDetail,name='VehicleDetail'),
    path('master/company/',views.company,name='company'),
    path('master/customer/',views.customer,name='customer'),
    path('master/products/',views.products,name='products'),
    path('master/order_status/',views.Order_status,name='order_status'),
    path('master/payment_status/',views.Payment_status,name='payment_status'),
    path('orders/order_placing',views.OrderTake,name='OrderTake'),
    path('orders/orders_details',views.orders_details,name='orders_details'),
    
    
    
]



admin.site.site_header = 'KeralaPacha Administration dashboard'                   
admin.site.index_title = 'KeralaPacha'                 
admin.site.site_title = 'KeralaPacha Administration'