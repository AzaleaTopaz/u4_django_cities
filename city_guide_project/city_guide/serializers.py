from rest_framework import serializers
from .models import City, Attraction, Review

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    cities = serializers.HyperlinkedRelatedField(
    view_name = 'city-detail',
    read_only = True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source='city'
    )

    class Meta:
        model = Attraction
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
    many = True,
    read_only=True

    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'city-detail'
                                                     )

    class Meta:
        model = City
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
    view_name = 'attraction-detail',
    many = True,
    read_only = True
        )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset = Attraction.objects.all(),
        source='attractions'
    )

    class Meta:
        model = Review
        fields = '__all__'


