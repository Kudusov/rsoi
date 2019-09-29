from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    title = serializers.CharField()
    author = serializers.CharField()
    publish_year = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('author', instance.author)
        instance.publish_year = validate_data.get('publish_year', instance.publish_year)
        instance.save()
        
        return instance

    def validate_title(self, value):
        '''
        if 'война' not in value.lower():
            raise serializers.ValidationError("В названии книги не содержится слово война")
        return value
        '''
        return value

    def validate_publish_year(self, value):
        if value < 0:
            raise serializers.ValidationError("published year must be positive")

        return value