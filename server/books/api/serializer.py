from rest_framework import serializers
from books.models import Book

#takes in the data and transforms into the json format so it's understandable  to the frontend
class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'description'
        )

