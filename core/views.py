from rest_framework.decorators import api_view


@api_view(http_method_names=['GET'])
def resolve(request):
    pass


@api_view(http_method_names=['POST'])
def shorten(request):
    pass
