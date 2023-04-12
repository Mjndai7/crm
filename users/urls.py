from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.HomeView.as_view(), name='dashboard'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
]