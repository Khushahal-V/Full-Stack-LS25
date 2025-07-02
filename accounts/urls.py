from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('dashboard') if request.user.is_authenticated else redirect('register')),
    path('register/', views.register_view, name='register'),
    path('verify/<uuid:token>/', views.verify_view, name='verify'),  # ✅ FIXED
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
