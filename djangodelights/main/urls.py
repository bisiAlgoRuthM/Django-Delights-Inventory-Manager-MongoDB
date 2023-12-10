from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('add_ingredient/', views.add_ingredent, name = 'add_ingredient'),
    path('add_menu_item/', views.add_menu_item, name = 'add_menu_item'),
    path('add_recipe_requirement/', views.add_recipe_requirement, name = 'add_recipe_requirement'),
    path('purchase_page/', views.purchase_page, name = 'purchase_page'),
    path('purchase_success/', views.purchase_success, name='purchase_success'),
    path('success/', views.success_page, name='success_page')
]