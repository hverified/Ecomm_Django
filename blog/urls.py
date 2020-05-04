from django.urls import path
from .views import blogIndexView


urlpatterns = [
    path('', blogIndexView),
]
