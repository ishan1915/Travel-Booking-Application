from django.urls import path,include
from .views import *
urlpatterns = [
    path('login/',loginview,name='login'),
    path('signup/',signup_view,name='signup'),

    path('logout/',logout_view,name='logout'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('edit_profile/',profile_edit,name='edit_profile'),
    path('booking/',create_booking,name='booking'),
    path('booking_history',booking_history,name='booking_history'),
    path("booking/cancel/<int:booking_id>/", cancel_booking, name="cancel_booking"),

    #api 

    path('booking_detail/',booking_detail,name='booking_detail'),
    path('booking/all/',booking_all,name='booking_all'),
    path('api/login/',login_apiview,name='login_api'),
    path('api/signup/',usercreate,name='apisignup'),
    path('api/profile/',create_profileapi,name='create_profileapi'),
]
