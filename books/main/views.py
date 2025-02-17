from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.http import HttpResponse



# для отправки формы обмена книгами
# def exchange_books(request):
#     if request.method == "POST":
#         # Обрабатываем данные формы
#         author_surname = request.POST.get("author_surname")
#         author_name = request.POST.get("author_name")
#         book_title = request.POST.get("book_title")
#         isbn = request.POST.get("isbn")
#         publish_year = request.POST.get("publish_year")
#         genres = request.POST.getlist("genre")
#         desired_genres = request.POST.getlist("desired_genre")
#
#         # Здесь можно добавить сохранение в базу данных
#         return JsonResponse({"status": "success", "message": "Форма успешно отправлена"})
#
#     return JsonResponse({"status": "error", "message": "Только POST-запросы разрешены"})

def test(request):
    return render(request, "main/index.html")

def userPage(request):
   return render(request, "main/userPage.html")

def trade(request):
   return render(request, "main/trade.html")

def exchange(request):
   return render(request, "main/exchange.html")