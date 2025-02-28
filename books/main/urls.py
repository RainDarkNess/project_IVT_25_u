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
                path('admin-panel/', views.adminPanel, name='admin-panel'),
                path('add-book/', views.addBook, name='add_book'),
                path('books/', views.bookList, name='book_list'),
                path('edit-book/<int:book_id>/', views.editBook, name='edit_book'),
                path('delete-book/<int:book_id>/', views.deleteBook, name='delete_book'),

                path('add-janre/', views.addGenre, name='add-janre'),
                path('edit-genre/<int:genre_id>/', views.edit_genre, name='edit_genre'),
                path('delete-genre/<int:genre_id>/', views.delete_genre, name='delete_genre'),

                path('add-cover/', views.addCover, name='add_cover'),
                path('edit-cover/<int:cover_id>/', views.editCover, name='edit_cover'),
                path('delete-cover/<int:cover_id>/', views.deleteCover, name='delete_cover'),

                path('add-author/', views.addAuthor, name='add_author'),
                path('edit-author/<int:author_id>/', views.editAuthor, name='edit_author'),
                path('delete-author/<int:author_id>/', views.deleteAuthor, name='delete_author'),

                path('add-category/', views.addCategory, name='add_category'),
                path('edit-category/<int:category_id>/', views.editCategory, name='edit_category'),
                path('delete-category/<int:category_id>/', views.deleteCategory, name='delete_category'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
