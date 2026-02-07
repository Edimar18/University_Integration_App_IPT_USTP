from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('academics/', views.academics, name='academics'),
    path('library/', views.library, name='library'),
    path('finance/', views.finance, name='finance'),
    path('settings/', views.settings, name='settings'),


]