from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('list/', views.pantry_list, name='pantry_list')
]
