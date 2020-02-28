from django.urls import path

from core.views import shorten, redirect

urlpatterns = [
    path('shorten', shorten),
    path('<slug:url>', redirect)
]
