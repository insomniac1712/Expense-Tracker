from django.contrib import admin
from django.urls import include, path
from .import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name = 'index'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('categories/',views.category_list,name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='myapp/login.html'), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("api/", include("myapp.api.urls")),
]