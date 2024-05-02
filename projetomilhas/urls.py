from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('capitania/', admin.site.urls), #admin page
    path('capitania/', views.capitania, name='capitania'), #admin page
    path('', views.home, name='home'),   #initial page
]
