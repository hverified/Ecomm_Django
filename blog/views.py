from django.shortcuts import render
from django.http import HttpResponse


def blogIndexView(request):

    return render(request, "blog/index.html")
