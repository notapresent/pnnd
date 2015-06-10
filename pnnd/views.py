from django.shortcuts import render, get_object_or_404

from .models import MainPage


def main(request):
    ctx = MainPage.get_context()
    return render(request, 'home.html', ctx)
