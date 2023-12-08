from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from eCommerce.models import *

@login_required(login_url='login')
def homepage(request):
    product=Product.objects.all()
    return render(request,"homepage.html",{"product":product})

@login_required(login_url='login')
def logged(request,username):
    product=Product.objects.all()
    userData=User.objects.get(username=username)
    return render(request,"logged.html",{"userData":userData,"product":product})

@login_required(login_url='login')
def search(request):
    if request.method=='POST':
         key=request.POST.get('search')
    else:
         return HttpResponse("Enter something to search!")
    product=Product.objects.filter(product_tag__icontains=key)
    return render(request,"search.html",{"product": product})

@login_required(login_url='login')
def product_detail(request,product_id):
    product=Product.objects.get(product_id=product_id)
    products=Product.objects.all()
    return render(request,"product_detail.html",{"product":product,"products":products})

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

#listing products category wise 
def gadgetslist(request):
     products=Product.objects.filter(product_category__icontain="gadgets")
     return render(request,"gadgets.html",{{"products" : products}})
def shoeslist(request):
     products=Product.objects.filter(product_category__icontain="shoes")
     return render(request,"shoes.html",{{"products" : products}})
def clothslist(request):
     products=Product.objects.filter(product_category__icontain="cloths")
     return render(request,"cloths.html",{{"products" : products}})
def furniturelist(request):
     products=Product.objects.filter(product_category__icontain="furniture")
     return render(request,"furniture.html",{{"products" : products}})
def grocerylist(request):
     products=Product.objects.filter(product_category__icontain="grocery")
     return render(request,"grocery.html",{{"products" : products}})


#add to cart functionality
def add_to_cart(request):
     return
     
# Create your views here.
