from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse


def test(request):
    return render(request, "main/index.html")


def exchange(request):
    return render(request, "main/exchange.html")


def userPage(request):
    return render(request, "main/userPage.html")


def trade(request):
    return render(request, "main/trade.html")


def testMyTrades(request):
    return render(request, "main/myTrades.html")


def testTrades(request):
    return render(request, "main/trading.html")
