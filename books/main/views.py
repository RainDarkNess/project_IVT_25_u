from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse

from .forms import UserProfileForm, RegistrationForm, GenreForm
from .models import CustomUser, Genre


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


@staff_member_required
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


@staff_member_required
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


@staff_member_required
def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('add-janre')

    return render(request, 'main/delete_genre.html', {'genre': genre})
