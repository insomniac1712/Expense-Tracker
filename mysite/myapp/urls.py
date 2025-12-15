from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('categories/',views.category_list,name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
]