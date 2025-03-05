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

                path('trading/', views.create_order_request, name="trading"),
                path('trading-from-page/<int:book_id>/', views.create_order_request_from_page, name="trading_from_page"),
                path('trading-edit/<int:trade_id>/', views.editTrade, name="trading_edit"),
                path('trading-delete/<int:trade_id>/', views.deleteTrade, name="trading_delete"),

                path('create-trade/<int:trade_id>/', views.createTrade, name="create_trade"),
                path('view-trade/<int:trade_id>/', views.viewTrade, name="view_trade"),
                path('trade-delete/<int:trade_id>/', views.deleteTradeBooks, name="trade_delete"),
                path('trade-delete-end-exit/<int:trade_id>/', views.deleteAndExitFromTradeBooks,
                     name="delete_and_exit_from_trade_books"),
                path('out-from-trade/<int:trade_id>/', views.outFromTrade, name="out_from_trade"),

                path('action-trade/<int:trade_id>/', views.actionTrade, name="action_trade"),

                path('show-books/', views.showUsersBooks, name="show_books"),

                path('edit-profile/', views.edit_profile, name='edit_profile'),
                path('register/', views.register, name='register'),
                path('admin-panel/', views.adminPanel, name='admin-panel'),
                path('add-book/', views.addBook, name='add_book'),
                path('books/', views.bookList, name='book_list'),
                path('book-list-admin/', views.bookListAdmin, name='book-list-admin'),
                path('user-page-view/<int:user_id>/', views.userPageView, name='user-page-view'),

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
