from rest_framework import generics, mixins
from books.models import Book
from .serializer import bookSerializer

class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # to specify the type of key in the json output
    resource_name = 'books'
    serializer_class = bookSerializer

    serializer_class = bookSerializer

    #returns all the book objects in the database
    def get_queryset(self):
        return Book.objects.all()

    #implements creating and saving a new model instance
    def post(self, request, *args, **karwgs):
        return self.create(request, *args, **karwgs)
