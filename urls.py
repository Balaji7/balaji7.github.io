from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("table", views.table, name='table'),
    path("form", views.form, name='form'),
    path("tab1", views.tab1, name='tab1'),
    path("pt_data", views.pt_data, name='pt_data'),
    path("updatepage/<int:id>", views.updatepage, name='updatepage'),
    path("pt_update", views.pt_update, name='pt_update'),
    path("delete/<int:id>", views.delete, name='delete'),
    path("search_results", views.search_results, name='search_results'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("signup_page", views.signup_page, name='signup_page'),
    path("login_page", views.login_page, name='login_page'),
    path("logout", views.logout, name='logout'),

    
]