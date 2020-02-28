import uuid

from rest_framework import serializers

from core.models import UrlModel


def generate_url():
    """generates a new unique url slug"""

    slug = uuid.uuid4().get_hex()[:6]

    while UrlModel.objects.filter(short_url=slug):
        slug = uuid.uuid4().get_hex()[:6]

    return slug


class UrlSerializer(serializers.ModelSerializer):
    """Serializers for url model"""

    short_url = serializers.CharField(max_length=6)

    class Meta:
        model = UrlModel
        exclude = 'id'

    def create(self, validated_data):
        """creates a new url to the db"""

        # if user didn't pass url generate a new one
        short_url = validated_data.get('short_url', '')
        if not short_url:
            short_url = generate_url()
        else:
            # if the slug entered by user exists, add a number
            # to it to make it unique
            if UrlModel.objects.filter(short_url=short_url):
                num = 2
                while UrlModel.objects.filter(short_url=short_url):
                    short_url = short_url + '-' + num
                    num = num + 1

        url_instance = UrlModel(short_url=short_url, **validated_data)
        url_instance.save()

        return url_instance
