from django.urls import path
from . import views
urlpatterns =[
    path('log_in/', views.log_in , name="logar"),
    path('sign_up', views.sign_up, name="sing_up")
]