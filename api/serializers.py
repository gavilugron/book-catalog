from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'description',
            'author',
            'isbn',
            'published_date',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']