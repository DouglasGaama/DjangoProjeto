"""LajesTocantins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Lajes.views import index, produtos, lajetreliçada, lajecovencional, lajebidirecional, postes, pingadeira, eps, contato, empresa, galeria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('lajetreliçada/', lajetreliçada),
    path('produtos/', produtos),
    path('lajecovencional/', lajecovencional),
    path('lajebidirecional/', lajebidirecional),
    path('postes/', postes),
    path('pingadeira/', pingadeira),
    path('eps/', eps),
    path('contato/', contato),
    path('empresa/', empresa),
    path('galeria/', galeria),
]
