#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

import copy
import uuid

from rest_framework import serializers

from core.models import UrlModel


def generate_url():
    """generates a new unique url slug"""

    slug = uuid.uuid4().hex[:6]

    while UrlModel.objects.filter(short_url=slug):
        slug = uuid.uuid4().hex[:6]

    return slug


class UrlSerializer(serializers.ModelSerializer):
    """Serializers for url model"""

    short_url = serializers.CharField(max_length=6, required=False)

    class Meta:
        model = UrlModel
        exclude = ('id',)

    def to_internal_value(self, data):
        if '://' not in data['original_url']:  # no url scheme
            new_data = copy.deepcopy(data)
            new_data['original_url'] = 'http://' + data['original_url']
            return super().to_internal_value(new_data)
        return super().to_internal_value(data)

    def validate_short_url(self, short_url):
        """validates the passed short url"""

        # raises error if the slug entered by user exists and
        # can't even be added a num to its end

        url = short_url  # just an alias
        if UrlModel.objects.filter(short_url=url):
            num = 2
            while UrlModel.objects.filter(short_url=url):
                if num == 100:
                    raise serializers.ValidationError('this short url cant be registered')
                url = short_url + '-' + str(num)
                num = num + 1

        return url

    def create(self, validated_data):
        """creates a new url to the db"""

        # if user didn't pass url generate a new one
        short_url = validated_data.pop('short_url', '')
        if not short_url:
            short_url = generate_url()

        url_instance = UrlModel(short_url=short_url, **validated_data)
        url_instance.save()

        return url_instance
