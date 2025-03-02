import json
from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core import serializers

# Create your views here.

from django.http import HttpResponse

from .forms import UserProfileForm, RegistrationForm, GenreForm, BookForm, CoverForm, WriterForm, CategoryForm, \
    OrderRequestsForm, OrderbooksForm
from .models import CustomUser, Genre, Books, Cover, Category, Writer, OrderRequests


def test(request):
    if request.user.is_authenticated:
        return render(request, "main/index.html", {'requests':
                                                   OrderRequests.objects.exclude(userrequest=request.user)})
    else:
        return render(request, "main/index.html", {'requests':
                                                   OrderRequests.objects.all()})


@login_required(login_url='/accounts/login/')
def exchange(request):
    return render(request, "main/exchange.html")


@login_required(login_url='/accounts/login/')
def userPage(request):
    return render(request, "main/userPage.html", {
        'books': Books.objects.filter(idAuthorUser=request.user),
        'myOrders': OrderRequests.objects.filter(userrequest=request.user)})


@login_required(login_url='/accounts/login/')
def trade(request):
    return render(request, "main/trade.html")


@login_required(login_url='/accounts/login/')
def testMyTrades(request):
    return render(request, "main/myTrades.html")


@login_required(login_url='/accounts/login/')
def testTrades(request):
    return render(request, "main/trading.html")


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userPage')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'images': CustomUser.objects.all
    }
    return render(request, 'main/edit_profile.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/user-page/')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'images': CustomUser.objects.all
    }
    return render(request, 'main/registration.html', context=context)


@staff_member_required(login_url='/accounts/login/')
def adminPanel(request):
    return render(request, 'main/admin-panel.html')


@login_required(login_url='/accounts/login/')
def addGenre(request):
    if request.user.is_superuser:
        genres = Genre.objects.filter()
    else:
        genres = Genre.objects.filter(idAuthorUser=request.user)
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.idAuthorUser = request.user
            genre.save()
            return redirect('add-janre')
    else:
        form = GenreForm()

    genres_list = [
        {
            'namegenre': genre.namegenre,
            'id': genre.id,
        }
        for genre in genres
    ]

    tHeaders = ["Название"]
    editForm = 'edit_genre'
    deleteForm = 'delete_genre'
    buttonText = 'Добавить жанр'
    return render(request, 'main/add_form.html',
                  {'form': form, 'tHeaders': tHeaders, 'list': genres_list,
                   'editForm': editForm, 'deleteForm': deleteForm, 'buttonText': buttonText})


@login_required(login_url='/accounts/login/')
def edit_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('add-janre')
    else:
        form = GenreForm(instance=genre)

    return render(request, 'main/edit_form.html',
                  {'form': form, 'hText': 'Редактировать жанр', 'elementName': genre,
                   'reverseRoute': 'add-janre'})


@login_required(login_url='/accounts/login/')
def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('add-janre')

    return render(request, 'main/delete_form.html',
                  {'category': genre, 'hText': 'Удалить жанр', 'elementName': genre.namegenre,
                   'reverseRoute': 'add_cover'})


@login_required(login_url='/accounts/login/')
def addBook(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.idAuthorUser = request.user
            book.save()
            return redirect('book_list')
    else:
        book_form = BookForm()

    return render(request, 'main/add_book.html', {'book_form': book_form})


@login_required(login_url='/accounts/login/')
def addCover(request):
    if request.user.is_superuser:
        covers = Cover.objects.filter()
    else:
        covers = Cover.objects.filter(idAuthorUser=request.user)

    if request.method == 'POST':
        cover_form = CoverForm(request.POST, request.FILES)

        if cover_form.is_valid():
            cover = cover_form.save(commit=False)
            cover.idAuthorUser = request.user
            cover.save()
            return redirect('add_cover')
    else:
        cover_form = CoverForm()

    covers_list = [
        {
            'cover': cover.cover,
            'img': cover.img.url if cover.img else None,
            'descriptioncover': cover.descriptioncover,
            'id': cover.idcover,
        }
        for cover in covers
    ]

    tHeaders = ["Название", "Картинка", "Описание"]
    editForm = 'edit_cover'
    deleteForm = 'delete_cover'
    buttonText = 'Добавить обложку'
    return render(request, 'main/add_form.html',
                  {'form': cover_form, 'tHeaders': tHeaders, 'list': covers_list,
                   'editForm': editForm, 'deleteForm': deleteForm, 'buttonText': buttonText})


@login_required(login_url='/accounts/login/')
def editCover(request, cover_id):
    cover = get_object_or_404(Cover, idcover=cover_id)
    if request.method == 'POST':
        form = CoverForm(request.POST, request.FILES, instance=cover)
        if form.is_valid():
            form.save()
            return redirect('add_cover')
    else:
        form = CoverForm(instance=cover)

    return render(request, 'main/edit_form.html',
                  {'form': form, 'hText': 'Редактировать категорию', 'elementName': cover,
                   'reverseRoute': 'add_cover'})


@login_required(login_url='/accounts/login/')
def deleteCover(request, cover_id):
    cover = get_object_or_404(Cover, idcover=cover_id)
    if request.method == 'POST':
        cover.delete()
        return redirect('add_cover')

    return render(request, 'main/delete_form.html',
                  {'category': cover, 'hText': 'Удалить категорию', 'elementName': cover.cover,
                   'reverseRoute': 'add_cover'})


@login_required(login_url='/accounts/login/')
def bookList(request):
    if request.user.is_superuser:
        books = Books.objects.filter()
    else:
        books = Books.objects.filter(idAuthorUser=request.user)
    return render(request, 'main/book_list.html', {'books': books})


@login_required(login_url='/accounts/login/')
def showUsersBooks(request):
    books = Books.objects.filter(idAuthorUser=request.user)
    data = []

    for book in books:
        book_data = {
            'idbooks': str(book.idbooks),
            'author': str(book.idwriter.lastname + ' ' + book.idwriter.firstname),
            'name': str(book.name),
            'description': str(book.description),
            'img': book.idcover.img.url if book.idcover and book.idcover.img else None,
        }
        data.append(book_data)
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='/accounts/login/')
def deleteBook(request, book_id):
    book = get_object_or_404(Books, idbooks=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'main/delete_form.html',
                  {'category': book, 'hText': 'Удалить книгу', 'elementName': book.name,
                   'reverseRoute': 'add_category'})


@login_required(login_url='/accounts/login/')
def editBook(request, book_id):
    book = get_object_or_404(Books, idbooks=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'main/edit_book.html', {'form': form, 'book': book})


@login_required(login_url='/accounts/login/')
def addAuthor(request):
    if request.user.is_superuser:
        authors = Writer.objects.filter()
    else:
        authors = Writer.objects.filter(idAuthorUser=request.user)
    form = WriterForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            author = form.save(commit=False)
            author.idAuthorUser = request.user
            author.save()
            return redirect('add_book')
    else:
        form = WriterForm()

    author_list = [
        {
            'fio': author.lastname + " " + author.firstname,
            'id': author.idwriter,
        }
        for author in authors
    ]

    tHeaders = ["ФИО"]
    editForm = 'edit_author'
    deleteForm = 'delete_author'
    buttonText = 'Добавить автора'
    return render(request, 'main/add_form.html',
                  {'form': form, 'tHeaders': tHeaders, 'list': author_list,
                   'editForm': editForm, 'deleteForm': deleteForm, 'buttonText': buttonText})


@login_required(login_url='/accounts/login/')
def editAuthor(request, author_id):
    author = get_object_or_404(Writer, idwriter=author_id)
    if request.method == 'POST':
        form = WriterForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = WriterForm(instance=author)

    return render(request, 'main/edit_form.html',
                  {'form': form, 'hText': 'Редактировать автора', 'elementName': author,
                   'reverseRoute': 'add_author'})


@login_required(login_url='/accounts/login/')
def deleteAuthor(request, author_id):
    author = get_object_or_404(Writer, idwriter=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('add_category')

    return render(request, 'main/delete_form.html',
                  {'category': author, 'hText': 'Удалить автора',
                   'elementName': author.lastname + " " + author.firstname,
                   'reverseRoute': 'add_author'})


@login_required(login_url='/accounts/login/')
def addCategory(request):
    if request.user.is_superuser:
        categorises = Category.objects.all()
    else:
        categorises = Category.objects.filter(idAuthorUser=request.user)

    if request.method == 'POST':
        categorises_form = CategoryForm(request.POST, request.FILES)

        if categorises_form.is_valid():
            category = categorises_form.save(commit=False)
            category.idAuthorUser = request.user
            category.save()
            return redirect('add_category')
    else:
        categorises_form = CategoryForm()

    categories_list = [
        {
            'category': category.category,
            'id': category.idcategory,
        }
        for category in Category.objects.all()
    ]

    tHeaders = ["Категория"]
    editForm = 'edit_category'
    deleteForm = 'delete_category'
    buttonText = 'Добавить категорию'
    return render(request, 'main/add_form.html',
                  {'form': categorises_form, 'tHeaders': tHeaders, 'list': categories_list,
                   'editForm': editForm, 'deleteForm': deleteForm, 'buttonText': buttonText})


@login_required(login_url='/accounts/login/')
def editCategory(request, category_id):
    category = get_object_or_404(Category, idcategory=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'main/edit_form.html',
                  {'form': form, 'hText': 'Редактировать категорию', 'elementName': category,
                   'reverseRoute': 'add_category'})


@login_required(login_url='/accounts/login/')
def deleteCategory(request, category_id):
    category = get_object_or_404(Category, idcategory=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('add_category')

    return render(request, 'main/delete_form.html',
                  {'category': category, 'hText': 'Удалить категорию', 'elementName': category.category,
                   'reverseRoute': 'add_category'})


def create_order_request(request):
    if request.method == 'POST':
        form = OrderRequestsForm(request.POST)
        if form.is_valid():
            requestBook = form.save(commit=False)
            requestBook.userrequest = request.user
            requestBook.dateorder = datetime.today()
            requestBook.save()
            return redirect('userPage')
    else:
        initial_data = {
            'namebookrequest': '',
            'address': request.user.address,
            'userrequest': request.user,
            'dateorder': datetime.today(),
        }
        form = OrderRequestsForm(initial=initial_data)

    return render(request, 'main/trading.html', {'form': form})


def create_order_request_from_page(request, book_id):
    book = get_object_or_404(Books, idbooks=book_id)
    if request.method == 'POST':
        form = OrderRequestsForm(request.POST)
        if form.is_valid():
            requestBook = form.save(commit=False)
            requestBook.userrequest = request.user
            requestBook.dateorder = datetime.today()
            requestBook.save()
            return redirect('userPage')
    else:
        initial_data = {
            'namebookrequest': '',
            'booktorequest': book,
            'category': book.idcategory,
            'address': request.user.address,
            'userrequest': request.user,
            'dateorder': datetime.today(),
        }
        form = OrderRequestsForm(initial=initial_data)

    return render(request, 'main/trading.html', {'form': form})


@login_required(login_url='/accounts/login/')
def editTrade(request, trade_id):
    order = get_object_or_404(OrderRequests, idorder=trade_id)
    if request.method == 'POST':
        form = OrderRequestsForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('userPage')
    else:
        form = OrderRequestsForm(instance=order)

    return render(request, 'main/edit_form.html',
                  {'form': form, 'hText': 'Редактировать заявку',
                   'elementName': str(order.dateorder) + ' с книгой ' + str(order.booktorequest.name),
                   'reverseRoute': 'userPage'})


@login_required(login_url='/accounts/login/')
def deleteTrade(request, trade_id):
    order = get_object_or_404(OrderRequests, idorder=trade_id)
    if request.method == 'POST':
        order.delete()
        return redirect('userPage')

    return render(request, 'main/delete_form.html',
                  {'category': order, 'hText': 'Удалить зявку от ' + str(order.dateorder) + ' с книгой '
                                               + str(order.booktorequest.name),
                   'elementName': '',
                   'reverseRoute': 'userPage'})


@login_required(login_url='/accounts/login/')
def createTrade(request, trade_id):
    order = get_object_or_404(OrderRequests, idorder=trade_id)
    if request.method == 'POST':
        form = OrderbooksForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('userPage')
    else:
        initial_data = {
            'bookone': order.booktorequest,
            'addressrequester': order.address,
            'status': 1,
            'dateorder': datetime.today(),
            'idorder': trade_id
        }
        form = OrderbooksForm(instance=order, initial=initial_data)

    return render(request, 'main/trade.html', {'form': form, 'order': order})
