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
from django.urls import path, include

urlpatterns = [
                path("exchange/", views.exchange, name="exchange"),
                path('', views.test),
                path('accounts/', include('django.contrib.auth.urls')),
                path('user-page/', views.userPage, name="userPage"),
                path('myTrades/', views.testMyTrades),
                path('trading/', views.testTrades),
                path('edit-profile/', views.edit_profile, name='edit_profile'),
                path('register/', views.register, name='register'),
                path('add-janre/', views.addGenre, name='add-janre'),
                path('admin-panel/', views.adminPanel, name='admin-panel'),
                path('edit-genre/<int:genre_id>/', views.edit_genre, name='edit_genre'),
                path('delete-genre/<int:genre_id>/', views.delete_genre, name='delete_genre'),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
