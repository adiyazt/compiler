"""
URL configuration for compiler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from online.views import authreg, api_auth, api_reg, home, compiler, save_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authreg, name='authreg'),
    path('api_reg/', api_reg, name='api_reg'),
    path('api_auth/', api_auth, name='api_auth'),
    path('home/', home, name='home'),
    path('compiler/', compiler, name='compiler'),
    path('save_file/', save_file, name='save_file'),
]
