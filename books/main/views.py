from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse


def test(request):
    return render(request, "main/index.html")

def test(request):
    return render(request, "main/userPage.html")