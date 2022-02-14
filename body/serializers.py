from dataclasses import fields
from pyexpat import model
from urllib import request
from rest_framework import serializers
from .models import Person, Review

# person serializer
class PersonSerializer(serializers.ModelSerializer):
    # photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = "__all__"
    
    def get_photo_url(self, person):
        request = self.context.get('request')
        photo_url = person.photo.url            
        return request.build_absolute_uri(photo_url)

# review serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"