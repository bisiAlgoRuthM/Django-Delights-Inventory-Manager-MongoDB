from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('add_ingredient/', views.add_ingredent, name = 'add_ingredient')
]