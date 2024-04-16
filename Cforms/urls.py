from django.urls import path
from . import views

# app_name = "Cforms"

urlpatterns = [
    # path("", views.custom_login, name='custom_login'),
    # path('login/',views.login_page, name='login_page'),
    path('login/',views.log, name='log'),
    path("index/",views.index, name='index'),
    path('createuser/',views.signup, name='signup'),
    path('logout/',views.log_out, name='log_out')
]
