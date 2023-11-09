"""
URL configuration for FinalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eCommerce import views
from django.conf import settings
import os
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.homepage,name="homepage"),
    path('logged/<str:username>/',views.logged,name="logged"),
    path('search/',views.search,name="search"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('user-login/',views.userlogin,name="login"),
    path('logout/',views.LogoutPage,name="logout"),
    path('signup/',views.signup,name="signup")
]


