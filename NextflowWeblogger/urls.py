"""NextflowWeblogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Logger import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listen/', views.listen, name='listen'),
    path('', views.index, name='index'),
    path('run/<runId>',
        views.show_run, name='show_run'),
    path('run/<runId>/<h1>/<h2>',
        views.show_process, name='show_process'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]
