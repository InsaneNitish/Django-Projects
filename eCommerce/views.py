from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from eCommerce.models import *

def homepage(request):
    product=Product.objects.all()
    return render(request,"homepage.html",{"product":product})

@login_required(login_url='login')
def logged(request,username):
    product=Product.objects.all()
    userData=User.objects.get(username=username)
    return render(request,"logged.html",{"userData":userData,"product":product})

def search(request,key):
    product=Product.objects.get(tag=key)
    return render(request,"search.html",{"product": product})

def product_detail(request,product_id):
    product=Product.objects.get(product_id=product_id)
    return render(request,"product_detail.html",{"product":product})

@csrf_protect
def userlogin(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         print(username,password)
         user=authenticate(request,username=username,password=password)
         if user is not None:
              login(request,user)
              return redirect('logged',username)
         else:
              return HttpResponse("Username or password is incorrect!!!!!")
    return render(request,"login.html")

@csrf_protect
def signup(request):
    if request.method=='POST':
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password1=request.POST.get('password')
            password2=request.POST.get('passwordConfirm')
            if password1!=password2:
                 return HttpResponse("Password Did not matched ! Please go back re-enter information very carefully")
            else:
                  my_user=User.objects.create_user(username=username,email=email,password=password1)
                  my_user.save()
                  return redirect('login')
    return render(request,"signup.html")
def LogoutPage(request):
     logout(request)
     return redirect('homepage')
# Create your views here.
