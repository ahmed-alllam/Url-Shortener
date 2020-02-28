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

    def validate_short_url(self, short_url):
        """validates the passed short url"""

        # raises error if the slug entered by user exists and
        # can't even be added a num to its end

        if UrlModel.objects.filter(short_url=short_url):
            num = 2
            while UrlModel.objects.filter(short_url=short_url):
                if num == 1000:
                    raise serializers.ValidationError('this short url cant be registered')
                short_url = short_url + '-' + num
                num = num + 1

            self.validated_data['short_url'] = short_url

    def create(self, validated_data):
        """creates a new url to the db"""

        # if user didn't pass url generate a new one
        short_url = validated_data.get('short_url', '')
        if not short_url:
            short_url = generate_url()

        url_instance = UrlModel(short_url=short_url, **validated_data)
        url_instance.save()

        return url_instance
