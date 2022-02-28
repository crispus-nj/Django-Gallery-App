from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('photo/<str:pk>/', views.photo, name='photo'),
    path('add-photo/', views.add_photo, name='add-photo')
]

