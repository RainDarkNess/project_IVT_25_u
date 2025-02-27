from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse

from .forms import UserProfileForm, RegistrationForm, GenreForm, BookForm, CoverForm, WriterForm, CategoryForm
from .models import CustomUser, Genre, Books


def test(request):
    return render(request, "main/index.html")


@login_required(login_url='/accounts/login/')
def exchange(request):
    return render(request, "main/exchange.html")


@login_required(login_url='/accounts/login/')
def userPage(request):
    return render(request, "main/userPage.html")


@login_required(login_url='/accounts/login/')
def trade(request):
    return render(request, "main/trade.html")


@login_required(login_url='/accounts/login/')
def testMyTrades(request):
    return render(request, "main/myTrades.html")


@login_required(login_url='/accounts/login/')
def testTrades(request):
    return render(request, "main/trading.html")


@login_required
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


@staff_member_required
def adminPanel(request):
    return render(request, 'main/admin-panel.html')


@login_required
def addGenre(request):
    genres = Genre.objects.all()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-janre')
    else:
        form = GenreForm()

    return render(request, 'main/add_genre.html', {'form': form, 'genres': genres})


@login_required
def edit_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('add-janre')
    else:
        form = GenreForm(instance=genre)

    return render(request, 'main/edit_genre.html', {'form': form, 'genre': genre})


@login_required
def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('add-janre')

    return render(request, 'main/delete_genre.html', {'genre': genre})


@login_required
def addBook(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book = book_form.save()
            book.save()
            return redirect('book_list')
    else:
        book_form = BookForm()

    return render(request, 'main/add_book.html', {'book_form': book_form})


@login_required
def addCover(request):
    if request.method == 'POST':
        cover_form = CoverForm(request.POST, request.FILES)

        if cover_form.is_valid():
            cover = cover_form.save()
            cover.save()
            return redirect('add_book')
    else:
        cover_form = CoverForm()

    return render(request, 'main/add_cover.html', {'cover_form': cover_form})


@login_required
def bookList(request):
    books = Books.objects.all()  # Получаем все книги из базы данных
    return render(request, 'main/book_list.html', {'books': books})


@login_required
def deleteBook(request, book_id):
    book = get_object_or_404(Books, idbooks=book_id)
    if request.method == 'POST':
        book.delete()  # Удаляем книгу
        return redirect('book_list')  # Перенаправляем на список книг

    return render(request, 'main/delete_book.html', {'book': book})


@login_required
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


@login_required
def addAuthor(request):
    form = WriterForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            cover = form.save()
            cover.save()
            return redirect('add_book')
    else:
        form = WriterForm()

    return render(request, 'main/add_author.html', {'form': form})


@login_required
def addAuthor(request):
    form = WriterForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            author = form.save()
            author.save()
            return redirect('add_book')
    else:
        form = WriterForm()

    return render(request, 'main/add_author.html', {'form': form})


@login_required
def addCategory(request):
    form = CategoryForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            category = form.save()
            category.save()
            return redirect('add_book')
    else:
        form = CategoryForm()

    return render(request, 'main/add_category.html', {'form': form})
