from django.urls import path

urlpatterns = [
    path('shorten', shorten),
    path('<slug:url>', redirect)
]
