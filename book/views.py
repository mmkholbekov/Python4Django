from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hi_view(request):
    return HttpResponse('<h1>Hi Django</h1>')


def book_view(request):
    book = models.New.objects.all()
    return render(request, 'book.html', {'book': book})
