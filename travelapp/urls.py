from django.urls import path,include
from .views import *
urlpatterns = [
    path('login/',loginview,name='login'),
    path('dashboard/',dashboard_view,name='dashboard'),
]
