"""
URL configuration for myapp project.

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
from core.views import home, headphones, music, musicDe, musicEn, musicFr, carhome, car_toyota, car_honda, car_renault, week

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('music/', music, name='music'),
    path('music/de/', musicDe, name='musicDe'),
    path('music/en/', musicEn, name='musicEn'),
    path('music/fr/', musicFr, name='musicFr'),

    path('car/', carhome, name='carhome'),
    path('car/toyota', car_toyota, name='car_toyota'),
    path('car/honda', car_honda, name='car_honda'),
    path('car/renault', car_renault, name='car_renault'),
    
    path('week/', week, name='week'),

    path('headphones/', headphones, name='headphones')
]

