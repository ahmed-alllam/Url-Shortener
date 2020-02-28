from django.urls import path

from core.views import RedirectView, ShortenView

urlpatterns = [
    path('shorten', ShortenView.as_view(), name='shorten'),
    path('<slug:url>', RedirectView.as_view(), name='redirect')
]
