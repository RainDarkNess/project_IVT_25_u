"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from main.views import exchange

urlpatterns = [
                  path("exchange/", exchange, name="exchange"),
                  path('', views.test),
                  path('lk_user', views.userPage),
                  path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"),
                       name='login'),
                  path("accounts/password_reset/",
                       auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
                       name='password_reset'),
                  path("accounts/logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),
                       name='logout'),
                  path('accounts/password-reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
                       name='password_reset_done'),
                  path('accounts/password-reset-confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_done.html"),
                       name='password_reset_confirm'),
                  path('accounts/password-reset-complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
                       name='password_reset_complete'),

                  # path('profile/<str:username>/', views.profile, name='profile'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
