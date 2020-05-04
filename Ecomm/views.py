from django.shortcuts import render
from django.http import HttpResponse


def indexView(request):
    return render(request, 'index.html')
