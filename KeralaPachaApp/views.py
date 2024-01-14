from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from KeralaPachaApp.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib import messages
from django.contrib.auth.models import User,Group
from KeralaPachaApp.models import *
# Create your views here.

@login_required(login_url='login')
def Home(request): 
    return render(request,'index.html',{})

@unauthenticated_user
def SignupPage(request,*args,**kwargs):
    try:        
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')

            if pass1!=pass2:
                messages.error(request,'Your password and confrom password are not Same!!')
                #return HttpResponse("Your password and confrom password are not Same!!")
            else:                
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')               
        return render(request,'Authentication/signup.html') 
    except:
        return render(request,'Authentication/signup.html')    

@unauthenticated_user
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return redirect('login')
           # return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Authentication/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def master(request): 
    return render(request,'master.html',{})

@login_required(login_url='login')
def orders(request): 
    return render(request,'orders.html',{})

@login_required(login_url='login')
def hr(request): 
    return render(request,'hr.html',{})

@login_required(login_url='login')
def reports(request): 
    return render(request,'reports.html',{})

@login_required(login_url='login')
def LabourDetails(request): 
    Labour_Detail= Labour_Details.objects.all()
    return render(request,'LabourDetails.html',{'Employees':Labour_Detail})

@login_required(login_url='login')
def SalaryType(request): 
    Salary_type= Salary_Type.objects.all()
    return render(request,'Salary_Type.html',{'Salary_Type':Salary_type})

@login_required(login_url='login')
def LabourSalary(request): 
    salary= Labour_Salary.objects.all()
    return render(request,'LabourSalary.html',{'Employees_salary':salary})

@login_required(login_url='login')
def VehicleCost(request): 
    VehicleCost= Vehicle_Cost.objects.all()
    return render(request,'VehicleCost.html',{'VehicleCost':VehicleCost})

@login_required(login_url='login')
def VehicleDetail(request): 
    VehicleDetail= Vehicle_Details.objects.all()
    return render(request,'VehicleDetail.html',{'VehicleDetail':VehicleDetail})


@login_required(login_url='login')
def company(request): 
    CompanyDetail= Company.objects.all()
    return render(request,'Company.html',{'CompanyDetail':CompanyDetail})

@login_required(login_url='login')
def customer(request): 
    Customers= Customer.objects.all()
    return render(request,'Customer.html',{'Customers':Customers})

@login_required(login_url='login')
def products(request): 
    products= Product.objects.all()
    return render(request,'Products.html',{'products':products})

@login_required(login_url='login')
def Order_status(request): 
    orderstatus= order_status.objects.all()
    return render(request,'order_status.html',{'orderstatus':orderstatus})

@login_required(login_url='login')
def Payment_status(request): 
    paymentstatus= payment_status.objects.all()
    return render(request,'payment_status.html',{'paymentstatus':paymentstatus})
