from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from KeralaPachaApp.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib import messages
from django.contrib.auth.models import User,Group
# Create your views here.
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
