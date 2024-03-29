from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import UrlModel
from core.serializers import UrlSerializer


class RedirectView(APIView):
    """The view for redirect a short url to the original one"""

    serializer_class = UrlSerializer

    def get(self, request, url):
        """redirects to the requested url

        Arguments:
            request: the request made by user and
                     used to get the post bosy
            url: the url entered by user in url

        Returns:
                HTTP 302 Response redirect to the original url
                HTTP 404 Response if url doesn't exist
        """

        original_url = get_object_or_404(UrlModel, short_url=url).original_url
        return HttpResponseRedirect(redirect_to=original_url)


class ShortenView(APIView):
    """The View for Creating a new short url"""

    serializer_class = UrlSerializer

    def post(self, request):
        """creats a new short url

        Arguments:
            request: the request made by user and
                     used to get the post bosy
        Returns:
            HTTP 201 Response with the new url if no errors
            HTTP 400 Response if the data is invalid
        """

        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
